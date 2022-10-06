from twisted.internet.defer import inlineCallbacks

from EGGS_labrad.clients import GUIClient
from EGGS_labrad.config.device_db import device_db
from EGGS_labrad.clients.ARTIQ_client.DDS_gui import DDS_gui

DDSID = 659313
EXPID = 659314


class DDS_client(GUIClient):
    """
    Client for all Urukuls.
    """

    name = "Urukuls Client"
    servers = {'aq': 'ARTIQ Server'}


    def getgui(self):
        if self.gui is None:
            self.gui = DDS_gui(self.urukul_list)
        return self.gui

    @inlineCallbacks
    def initClient(self):
        # parse device_db for TTLs
        self.urukul_list = {}
        self._getDevices(device_db)

        # variables for storing dds state when we try to rescue
        self.before_rescue_params = None

        # connect to signals
        yield self.aq.signal__dds_changed(DDSID)
        yield self.aq.addListener(listener=self.updateDDS, source=None, ID=DDSID)
        yield self.aq.signal__exp_running(EXPID)
        yield self.aq.addListener(listener=self.experimentRunning, source=None, ID=EXPID)

    def _getDevices(self, device_db):
        # get devices
        for name, params in device_db.items():
            if 'class' not in params:
                continue
            elif params['class'] == 'CPLD':
                self.urukul_list[name] = {}
            elif params['class'] == 'AD9910':
                # assign ad9910 channels to urukuls
                urukul_name = params["arguments"]["cpld_device"]
                if urukul_name not in self.urukul_list:
                    self.urukul_list[urukul_name] = {}
                self.urukul_list[urukul_name][name] = None

    @inlineCallbacks
    def initData(self):
        # get minimum attenuations from registry
        min_attenuations = {}
        yield self.reg.cd(['', 'Clients', 'ARTIQ', 'Urukul'])
        _, restricted_dds_channels = yield self.reg.dir()

        # set limit on channel attenuations
        for dds_channel in restricted_dds_channels:
            min_attenuations[dds_channel] = yield self.reg.get(dds_channel)

        # get data using DDS Get All function on artiq server
        dds_data = yield self.aq.dds_get_all()
        num_boards = int(len(dds_data) / 4)
        dds_data = dds_data.reshape((num_boards, 4, 4))

        # get data for each dds channel on each dds-board
        for board_num, (urukul_name, ad9910_list) in enumerate(self.urukul_list.items()):
            for channel_num, (ad9910_name, ad9910_widget) in enumerate(ad9910_list.items()):
                # check if this channel has a restricted attenuation range
                if ad9910_name in min_attenuations:
                    ad9910_widget.att.setMinimum(min_attenuations[ad9910_name])
                # get values
                freq_mu, ampl_mu, att_mu, sw_status = dds_data[board_num][channel_num]
                # set values
                ad9910_widget.freq.setValue(freq_mu * 1e3 / (0xFFFFFFFF - 1))
                ad9910_widget.ampl.setValue(ampl_mu * 1e2 / 0x3FFF)
                ad9910_widget.att.setValue((255 - (int(att_mu) & 0xFF)) / 8)
                ad9910_widget.rfswitch.setChecked(sw_status)

    def initGUI(self):
        # rescue ion
        self.gui.rescue_button.clicked.connect(lambda status: self.rescueIon(status))

        # connect an urukul group
        for urukul_name, ad9910_list in self.gui.urukul_list.items():
            button = getattr(self.gui, "{:s}_init".format(urukul_name))
            button.clicked.connect(lambda _name=urukul_name: self.aq.urukul_initialize(_name))

            # connect DDS channels
            for ad9910_name, ad9910_widget in ad9910_list.items():
                ad9910_widget.initbutton.clicked.connect(lambda status, _channel_name=ad9910_name: self.aq.dds_initialize(_channel_name))
                ad9910_widget.freq.valueChanged.connect(lambda freq, _channel_name=ad9910_name:
                                                        self.aq.dds_frequency(_channel_name, freq * 1e6))
                ad9910_widget.ampl.valueChanged.connect(lambda ampl, _channel_name=ad9910_name:
                                                        self.aq.dds_amplitude(_channel_name, ampl / 100))
                ad9910_widget.att.valueChanged.connect(lambda att, _channel_name=ad9910_name:
                                                       self.aq.dds_attenuation(_channel_name, att))
                ad9910_widget.rfswitch.clicked.connect(lambda status, _channel_name=ad9910_name:
                                                       self.aq.dds_toggle(_channel_name, status))
                ad9910_widget.lock(False)


    # SLOTS
    def updateDDS(self, c, signal):
        """
        Update the DDS widget if its values are modified by another client.
        """
        ad9910_name, param, val = signal
        for urukul_name, ad9910_list in self.urukul_list.items():
            if ad9910_name in ad9910_list:
                ad9910_widget = self.urukul_list[urukul_name][ad9910_name]
                print('update:')
                print('\tparam: {}'.format(param))
                print('\tval: {:d}'.format(int(val)))
                if param == 'onoff':
                    dds_state = int(val)
                    ad9910_widget.rfswitch.blockSignals(True)
                    ad9910_widget.rfswitch.setChecked(dds_state)
                    ad9910_widget.rfswitch.setAppearance(dds_state)
                    ad9910_widget.rfswitch.blockSignals(False)
                elif param == 'att':
                    att_db = (255 - (int(val) & 0xFF)) / 8
                    ad9910_widget.att.blockSignals(True)
                    ad9910_widget.att.setValue(att_db)
                    ad9910_widget.att.blockSignals(False)
                elif param == 'ftw':
                    ad9910_widget.freq.blockSignals(True)
                    ad9910_widget.freq.setValue(val * 1e3 / (0xFFFFFFFF - 1))
                    ad9910_widget.freq.blockSignals(False)
                elif param == 'asf':
                    ad9910_widget.ampl.blockSignals(True)
                    ad9910_widget.ampl.setValue(val * 1e2 / 0x3FFF)
                    ad9910_widget.ampl.blockSignals(False)

    def experimentRunning(self, c, status):
        self.gui.artiq_monitor.setStatus(status)

    @inlineCallbacks
    def rescueIon(self, status):
        """
        Quickly rescues the ion by red-detuning the 397nm beam
        """
        # todo: add rf switch capability
        # todo: test
        widget = self.urukul_list['urukul1_cpld']['urukul1_ch1']
        if status:
            # save current dds values
            self.before_rescue_params = (
                widget.freq.value(),
                widget.ampl.value(),
                widget.att.value(),
                widget.rfswitch.isChecked()
            )

            # set rescuing parameters
            widget.freq.setValue(90)
            widget.ampl.setValue(0.5)
            widget.att.setValue(14)
            # todo: set output on

            # lock widget
            widget.blockSignals(True)
            widget.setDisabled(True)

        elif self.before_rescue_params is not None:
            # reenable widget
            widget.setDisabled(False)
            widget.blockSignals(False)

            # restore values in client
            widget.freq.setValue(self.before_rescue_params[0])
            widget.ampl.setValue(self.before_rescue_params[1])
            widget.att.setValue(self.before_rescue_params[2])
            yield self.aq.dds_toggle('urukul1_ch1', self.before_rescue_params[3])
            widget.rfswitch.setChecked(self.before_rescue_params[3])


if __name__ == "__main__":
    from EGGS_labrad.clients import runClient
    runClient(DDS_client)
