from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel, QGridLayout, QGroupBox, QDoubleSpinBox, QComboBox, QScrollArea, QWidget, QSizePolicy

from EGGS_labrad.clients.Widgets import TextChangingButton, Lockswitch

SHELL_FONT = 'MS Shell Dlg 2'
LABEL_FONT = QFont(SHELL_FONT, pointSize=8)
MAIN_FONT = QFont(SHELL_FONT, pointSize=15)
DISPLAY_FONT = QFont(SHELL_FONT, pointSize=20)


class toptica_channel(QFrame):
    """
    GUI for an individual Toptica Laser channel.
    """

    def __init__(self, piezoControl=True, parent=None):
        super().__init__()
        self.setFrameStyle(0x0001 | 0x0030)
        self.makeLayout(piezoControl)

    def makeLayout(self, piezoControl):
        # create status box
        statusBox = self._createStatusBox()
        self.statusBox.feedbackMode.addItem('Current')
        self.statusBox.feedbackMode.addItem('Temperature')
        if piezoControl:
            self.statusBox.feedbackMode.addItem('Piezo')
        # control boxes
        tempLabels = ('Actual Temperature (K)', 'Set Temperature (K)', 'Min. Temperature (K)', 'Max. Temperature (K)')
        tempBox = self._createControlBox('Temperature Control', 'tempBox', tempLabels)
        currLabels = ('Actual Current (mA)', 'Set Current (mA)', 'Min. Current (mA)', 'Max. Current (mA)')
        currBox = self._createControlBox('Current Control', 'currBox', currLabels)
        piezoBox = None
        # create piezo box
        if piezoControl:
            piezoLabels = ('Actual Voltage (V)', 'Set Voltage (V)', 'Min. Voltage (V)', 'Max. Voltage (V)')
            piezoBox = self._createControlBox('Piezo Control', 'piezoBox', piezoLabels)
        # lay out
        layout = QGridLayout(self)
        layout.minimumSize()
        layout.addWidget(statusBox,    0, 0)
        layout.addWidget(tempBox,      0, 3)
        layout.addWidget(currBox,      0, 4)
        layout.addWidget(piezoBox,     0, 5)

    def _createStatusBox(self):
        box = QWidget()
        box_layout = QGridLayout(box)
        # create labels
        chanLabel = QLabel('Channel:')
        freqLabel = QLabel('Center Frequency:')
        serLabel = QLabel('Serial Number:')
        typeLabel = QLabel('Laser Type:')
        emission_label = QLabel('Emission:')
        feedback_label = QLabel('Feedback:')
        for label in (chanLabel, freqLabel, serLabel, typeLabel, feedback_label, emission_label):
            label.setFont(LABEL_FONT)
            label.setAlignment(Qt.AlignLeft)
        # create displays
        channelDisplay = QLabel('#1')
        freqDisplay = QLabel('729.0012')
        serDisplay = QLabel('002129')
        typeDisplay = QLabel('DL Pro')
        for label in (channelDisplay, freqDisplay, serDisplay, typeDisplay):
            label.setFont(MAIN_FONT)
            label.setAlignment(Qt.AlignRight)
        # emission
        box.emissionButton = TextChangingButton(None)
        # feedback
        box.feedbackEnableButton = TextChangingButton(('On', 'Off'))
        box.feedbackChannel = QComboBox()
        box.feedbackChannel.setFont(QFont(SHELL_FONT, pointSize=10))
        box.feedbackChannel.addItem('Fine In 1')
        box.feedbackChannel.addItem('Fine In 2')
        box.feedbackChannel.addItem('Fast In 3')
        box.feedbackChannel.addItem('Fast In 4')
        box.feedbackMode = QComboBox()
        box.feedbackMode.setFont(QFont(SHELL_FONT, pointSize=10))
        # lay out
        box_layout.addWidget(chanLabel,                 0, 0)
        box_layout.addWidget(channelDisplay,            1, 0)
        box_layout.addWidget(freqLabel,                 2, 0)
        box_layout.addWidget(freqDisplay,               3, 0)
        box_layout.addWidget(serLabel,                  4, 0)
        box_layout.addWidget(serDisplay,                5, 0)
        box_layout.addWidget(typeLabel,                 6, 0)
        box_layout.addWidget(typeDisplay,               7, 0)
        box_layout.addWidget(emission_label,            8, 0)
        box_layout.addWidget(box.emissionButton,        9, 0)
        box_layout.addWidget(feedback_label,            10, 0)
        box_layout.addWidget(box.feedbackEnableButton,  11, 0)
        box_layout.addWidget(box.feedbackChannel,       12, 0)
        box_layout.addWidget(box.feedbackMode,          13, 0)
        # set self attribute and create wrapper
        setattr(self, 'statusBox', box)
        return self._wrapGroup('Status', box)

    def _createControlBox(self, name, objName, label_titles):
        # create holding box
        box = QWidget()
        box_layout = QGridLayout(box)
        # create labels
        actual_label = QLabel(label_titles[0])
        set_label = QLabel(label_titles[1])
        min_label = QLabel(label_titles[2])
        max_label = QLabel(label_titles[3])
        for label in (set_label, min_label, max_label):
            label.setFont(LABEL_FONT)
            label.setAlignment(Qt.AlignLeft)
        # create display
        box.actualValue = QLabel('00.0000')
        box.actualValue.setFont(DISPLAY_FONT)
        box.actualValue.setAlignment(Qt.AlignCenter)
        # create boxes
        box.setBox = QDoubleSpinBox()
        box.minBox = QDoubleSpinBox()
        box.maxBox = QDoubleSpinBox()
        for doublespinbox in (box.setBox, box.minBox, box.maxBox):
            doublespinbox.setDecimals(4)
            doublespinbox.setSingleStep(0.0004)
            doublespinbox.setRange(15, 50)
            doublespinbox.setKeyboardTracking(False)
            doublespinbox.setFont(QFont(SHELL_FONT, pointSize=10))
        # create buttons
        box.lockswitch = Lockswitch()
        box.record_button = TextChangingButton(('Stop Recording', 'Record'))
        # lay out
        box_layout.addWidget(actual_label,          1, 0, 1, 1)
        box_layout.addWidget(box.actualValue,       2, 0, 2, 1)
        box_layout.addWidget(set_label,             4, 0, 1, 1)
        box_layout.addWidget(box.setBox,            5, 0, 1, 1)
        box_layout.addWidget(min_label,             6, 0, 1, 1)
        box_layout.addWidget(box.minBox,            7, 0, 1, 1)
        box_layout.addWidget(max_label,             8, 0, 1, 1)
        box_layout.addWidget(box.maxBox,            9, 0, 1, 1)
        box_layout.addWidget(box.lockswitch,        10, 0, 1, 1)
        box_layout.addWidget(box.record_button,     11, 0, 1, 1)
        # connect signals to slots
        box.lockswitch.toggled.connect(lambda status, parent=objName: self._lock(status, parent))
        box.lockswitch.setChecked(True)
        # create QGroupBox wrapper
        setattr(self, objName, box)
        return self._wrapGroup(name, box)

    def _wrapGroup(self, name, widget):
        wrapper = QGroupBox(name)
        wrapper_layout = QGridLayout(wrapper)
        wrapper_layout.addWidget(widget)
        return wrapper

    def _lock(self, status, objName):
        parent = getattr(self, objName)
        parent.setBox.setEnabled(status)
        parent.minBox.setEnabled(status)
        parent.maxBox.setEnabled(status)


class toptica_gui(QFrame):
    """
    The full Toptica GUI.
    """

    def __init__(self, numChannels=4):
        super().__init__()
        self.setFrameStyle(0x0001 | 0x0030)
        self.channels = {}
        self.setWindowTitle('Toptica GUI')
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.makeLayout(numChannels)

    def makeLayout(self, numChannels):
        layout = QGridLayout(self)
        # scrollable holder for laser channels
        wm_scroll = QScrollArea()
        wm_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        wmChan_widget = QWidget()
        wmChan_layout = QGridLayout(wmChan_widget)
        for i in range(numChannels):
            channel_gui = toptica_channel(piezoControl=True)
            self.channels[i] = channel_gui
            wmChan_layout.addWidget(channel_gui, i, 0, 1, 1)

        # add wavemeter channel holder to qBox
        wm_scroll.setWidget(wmChan_widget)
        wm_scroll.setMinimumWidth(wmChan_widget.sizeHint().width())
        # final layout
        layout.addWidget(wm_scroll)


if __name__ == "__main__":
    from EGGS_labrad.clients import runGUI
    # run toptica channel gui
    #runGUI(toptica_channel)

    # run toptica client gui
    runGUI(toptica_gui)
