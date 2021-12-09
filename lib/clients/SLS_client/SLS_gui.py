# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SLS_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from EGGS_labrad.lib.clients.Widgets import TextChangingButton as _TextChangingButton

class TextChangingButton(_TextChangingButton):
    def __init__(self, button_text=None, parent=None):
        super(TextChangingButton, self).__init__(button_text, parent)
        self.setMaximumHeight(30)


class SLS_gui(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

    def setupUi(self):
        shell_font = 'MS Shell Dlg 2'
        SLS_gui = self
        SLS_gui.setObjectName("SLS_gui")
        SLS_gui.setFrameStyle(0x0001 | 0x0030)
        SLS_gui.setFixedSize(587, 410)
        SLS_gui.setWindowTitle("SLS Client")
        self.sls_label = QtWidgets.QLabel(SLS_gui)
        self.sls_label.setGeometry(QtCore.QRect(160, 10, 271, 41))
        self.sls_label.setObjectName("sls_label")
        self.layoutWidget = QtWidgets.QWidget(SLS_gui)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 70, 131, 236))
        self.layoutWidget.setObjectName("layoutWidget")
        self.PDH_layout = QtWidgets.QGridLayout(self.layoutWidget)
        self.PDH_layout.setContentsMargins(0, 0, 0, 0)
        self.PDH_layout.setObjectName("PDH_layout")
        self.PDH_label = QtWidgets.QLabel(self.layoutWidget)
        self.PDH_label.setObjectName("PDH_label")
        self.PDH_layout.addWidget(self.PDH_label, 1, 1, 1, 1)
        self.PDH_freq = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.PDH_freq.setMinimum(10.0)
        self.PDH_freq.setMaximum(35.0)
        self.PDH_freq.setSingleStep(0.1)
        self.PDH_freq.setObjectName("PDH_freq")
        self.PDH_layout.addWidget(self.PDH_freq, 4, 1, 1, 1)
        self.PDH_freq_label = QtWidgets.QLabel(self.layoutWidget)
        self.PDH_freq_label.setObjectName("PDH_freq_label")
        self.PDH_layout.addWidget(self.PDH_freq_label, 3, 1, 1, 1)
        self.PDH_filter = QtWidgets.QComboBox(self.layoutWidget)
        self.PDH_filter.setObjectName("PDH_filter")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_filter.addItem("")
        self.PDH_layout.addWidget(self.PDH_filter, 10, 1, 1, 1)
        self.PDH_filter_label = QtWidgets.QLabel(self.layoutWidget)
        self.PDH_filter_label.setObjectName("PDH_filter_label")
        self.PDH_layout.addWidget(self.PDH_filter_label, 9, 1, 1, 1)
        self.PDH_phaseoffset = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.PDH_phaseoffset.setMaximum(360.0)
        self.PDH_phaseoffset.setSingleStep(0.1)
        self.PDH_phaseoffset.setObjectName("PDH_phaseoffset")
        self.PDH_layout.addWidget(self.PDH_phaseoffset, 8, 1, 1, 1)
        self.PDH_phasemodulation_label = QtWidgets.QLabel(self.layoutWidget)
        self.PDH_phasemodulation_label.setObjectName("PDH_phasemodulation_label")
        self.PDH_layout.addWidget(self.PDH_phasemodulation_label, 5, 1, 1, 1)
        self.PDH_phasemodulation = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.PDH_phasemodulation.setMaximum(3.0)
        self.PDH_phasemodulation.setSingleStep(0.1)
        self.PDH_phasemodulation.setObjectName("PDH_phasemodulation")
        self.PDH_layout.addWidget(self.PDH_phasemodulation, 6, 1, 1, 1)
        self.PDH_phaseoffset_label = QtWidgets.QLabel(self.layoutWidget)
        self.PDH_phaseoffset_label.setObjectName("PDH_phaseoffset_label")
        self.PDH_layout.addWidget(self.PDH_phaseoffset_label, 7, 1, 1, 1)
        self.PDH_lockswitch = TextChangingButton(('Unlocked', 'Locked'), self.layoutWidget)
        self.PDH_lockswitch.setObjectName("PDH_lockswitch")
        self.PDH_layout.addWidget(self.PDH_lockswitch, 2, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(SLS_gui)
        self.layoutWidget1.setGeometry(QtCore.QRect(440, 70, 131, 326))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.servo_layout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.servo_layout.setContentsMargins(0, 0, 0, 0)
        self.servo_layout.setObjectName("servo_layout")
        self.servo_filter = QtWidgets.QComboBox(self.layoutWidget1)
        self.servo_filter.setObjectName("servo_filter")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_filter.addItem("")
        self.servo_layout.addWidget(self.servo_filter, 18, 1, 1, 1)
        self.servo_set = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.servo_set.setMinimum(-1000000.0)
        self.servo_set.setMaximum(1000000.0)
        self.servo_set.setObjectName("servo_set")
        self.servo_layout.addWidget(self.servo_set, 5, 1, 1, 1)
        self.servo_p = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.servo_p.setMaximum(1000.0)
        self.servo_p.setObjectName("servo_p")
        self.servo_layout.addWidget(self.servo_p, 10, 1, 1, 1)
        self.servo_param = QtWidgets.QComboBox(self.layoutWidget1)
        self.servo_param.setObjectName("servo_param")
        self.servo_param.addItem("")
        self.servo_param.addItem("")
        self.servo_param.addItem("")
        self.servo_layout.addWidget(self.servo_param, 3, 1, 1, 1)
        self.servo_p_label = QtWidgets.QLabel(self.layoutWidget1)
        self.servo_p_label.setObjectName("servo_p_label")
        self.servo_layout.addWidget(self.servo_p_label, 9, 1, 1, 1)
        self.servo_i = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.servo_i.setMaximum(1.0)
        self.servo_i.setSingleStep(0.01)
        self.servo_i.setObjectName("servo_i")
        self.servo_layout.addWidget(self.servo_i, 12, 1, 1, 1)
        self.servo_i_label = QtWidgets.QLabel(self.layoutWidget1)
        self.servo_i_label.setObjectName("servo_i_label")
        self.servo_layout.addWidget(self.servo_i_label, 11, 1, 1, 1)
        self.servo_param_label = QtWidgets.QLabel(self.layoutWidget1)
        self.servo_param_label.setObjectName("servo_param_label")
        self.servo_layout.addWidget(self.servo_param_label, 2, 1, 1, 1)
        self.servo_filter_label = QtWidgets.QLabel(self.layoutWidget1)
        self.servo_filter_label.setObjectName("servo_filter_label")
        self.servo_layout.addWidget(self.servo_filter_label, 17, 1, 1, 1)
        self.servo_label = QtWidgets.QLabel(self.layoutWidget1)
        self.servo_label.setObjectName("servo_label")
        self.servo_layout.addWidget(self.servo_label, 0, 1, 1, 1)
        self.servo_d_label = QtWidgets.QLabel(self.layoutWidget1)
        self.servo_d_label.setObjectName("servo_d_label")
        self.servo_layout.addWidget(self.servo_d_label, 13, 1, 1, 1)
        self.servo_set_label = QtWidgets.QLabel(self.layoutWidget1)
        self.servo_set_label.setObjectName("servo_set_label")
        self.servo_layout.addWidget(self.servo_set_label, 4, 1, 1, 1)
        self.servo_d = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.servo_d.setMaximum(10000.0)
        self.servo_d.setObjectName("servo_d")
        self.servo_layout.addWidget(self.servo_d, 14, 1, 1, 1)
        self.servo_lockswitch = TextChangingButton(('Unlocked', 'Locked'), self.layoutWidget1)
        self.servo_lockswitch.setObjectName("servo_lockswitch")
        self.servo_layout.addWidget(self.servo_lockswitch, 1, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(SLS_gui)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 70, 131, 257))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.autolock_layout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.autolock_layout.setContentsMargins(0, 0, 0, 0)
        self.autolock_layout.setObjectName("autolock_layout")
        self.autolock_param_label = QtWidgets.QLabel(self.layoutWidget2)
        self.autolock_param_label.setObjectName("autolock_param_label")
        self.autolock_layout.addWidget(self.autolock_param_label, 9, 1, 1, 1)
        self.autolock_time = QtWidgets.QLabel(self.layoutWidget2)
        self.autolock_time.setAlignment(QtCore.Qt.AlignCenter)
        self.autolock_time.setFont(QtGui.QFont(shell_font, pointSize=18))
        self.autolock_time.setStyleSheet('color: blue')
        self.autolock_time.setObjectName("autolock_time")
        self.autolock_layout.addWidget(self.autolock_time, 3, 1, 2, 1)
        self.autolock_param = QtWidgets.QComboBox(self.layoutWidget2)
        self.autolock_param.setObjectName("autolock_param")
        self.autolock_param.addItem("")
        self.autolock_param.addItem("")
        self.autolock_param.addItem("")
        self.autolock_layout.addWidget(self.autolock_param, 10, 1, 1, 1)
        self.autolock_time_label = QtWidgets.QLabel(self.layoutWidget2)
        self.autolock_time_label.setObjectName("autolock_time_label")
        self.autolock_layout.addWidget(self.autolock_time_label, 2, 1, 1, 1)
        self.autolock_label = QtWidgets.QLabel(self.layoutWidget2)
        self.autolock_label.setObjectName("autolock_label")
        self.autolock_layout.addWidget(self.autolock_label, 0, 1, 1, 1)
        self.autolock_toggle_label = QtWidgets.QLabel(self.layoutWidget2)
        self.autolock_toggle_label.setObjectName("autolock_toggle_label")
        self.autolock_layout.addWidget(self.autolock_toggle_label, 7, 1, 1, 1)
        self.autolock_attempts = QtWidgets.QLabel(self.layoutWidget2)
        self.autolock_attempts.setAlignment(QtCore.Qt.AlignCenter)
        self.autolock_attempts.setObjectName("autolock_attempts")
        self.autolock_attempts.setFont(QtGui.QFont(shell_font, pointSize=18))
        self.autolock_attempts.setStyleSheet('color: blue')
        self.autolock_layout.addWidget(self.autolock_attempts, 6, 1, 1, 1)
        self.autolock_attempts_label = QtWidgets.QLabel(self.layoutWidget2)
        self.autolock_attempts_label.setObjectName("autolock_attempts_label")
        self.autolock_layout.addWidget(self.autolock_attempts_label, 5, 1, 1, 1)
        self.autolock_toggle = TextChangingButton(('On', 'Off'), self.layoutWidget2)
        self.autolock_toggle.setObjectName("autolock_toggle")
        self.autolock_layout.addWidget(self.autolock_toggle, 8, 1, 1, 1)
        self.autolock_lockswitch = TextChangingButton(('Unlocked', 'Locked'), self.layoutWidget2)
        self.autolock_lockswitch.setObjectName("autolock_lockswitch")
        self.autolock_layout.addWidget(self.autolock_lockswitch, 1, 1, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(SLS_gui)
        self.layoutWidget_2.setGeometry(QtCore.QRect(160, 70, 131, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.off_layout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.off_layout.setContentsMargins(0, 0, 0, 0)
        self.off_layout.setObjectName("off_layout")
        self.off_lockpoint_label = QtWidgets.QLabel(self.layoutWidget_2)
        self.off_lockpoint_label.setObjectName("off_lockpoint_label")
        self.off_layout.addWidget(self.off_lockpoint_label, 5, 1, 1, 1)
        self.off_label = QtWidgets.QLabel(self.layoutWidget_2)
        self.off_label.setObjectName("off_label")
        self.off_layout.addWidget(self.off_label, 1, 1, 1, 1)
        self.off_freq_label = QtWidgets.QLabel(self.layoutWidget_2)
        self.off_freq_label.setObjectName("off_freq_label")
        self.off_layout.addWidget(self.off_freq_label, 3, 1, 1, 1)
        self.off_freq = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.off_freq.setMinimum(10.0)
        self.off_freq.setMaximum(35.0)
        self.off_freq.setSingleStep(0.1)
        self.off_freq.setObjectName("off_freq")
        self.off_layout.addWidget(self.off_freq, 4, 1, 1, 1)
        self.off_lockswitch = TextChangingButton(('Unlocked', 'Locked'), self.layoutWidget_2)
        self.off_lockswitch.setObjectName("off_lockswitch")
        self.off_layout.addWidget(self.off_lockswitch, 2, 1, 1, 1)
        self.off_lockpoint = QtWidgets.QComboBox(self.layoutWidget_2)
        self.off_lockpoint.setObjectName("off_lockpoint")
        self.off_lockpoint.addItem("")
        self.off_lockpoint.addItem("")
        self.off_lockpoint.addItem("")
        self.off_lockpoint.addItem("")
        self.off_lockpoint.addItem("")
        self.off_layout.addWidget(self.off_lockpoint, 6, 1, 1, 1)

        self.retranslateUi(SLS_gui)
        QtCore.QMetaObject.connectSlotsByName(SLS_gui)

    def retranslateUi(self, SLS_gui):
        _translate = QtCore.QCoreApplication.translate
        self.sls_label.setText(_translate("SLS_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">SLS Laser Client</span></p></body></html>"))
        self.PDH_label.setText(_translate("SLS_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">PDH</span></p></body></html>"))
        self.PDH_freq_label.setText(_translate("SLS_gui", "Frequency (MHz)"))
        self.PDH_filter.setItemText(0, _translate("SLS_gui", "None"))
        self.PDH_filter.setItemText(1, _translate("SLS_gui", "1"))
        self.PDH_filter.setItemText(2, _translate("SLS_gui", "2"))
        self.PDH_filter.setItemText(3, _translate("SLS_gui", "3"))
        self.PDH_filter.setItemText(4, _translate("SLS_gui", "4"))
        self.PDH_filter.setItemText(5, _translate("SLS_gui", "5"))
        self.PDH_filter.setItemText(6, _translate("SLS_gui", "6"))
        self.PDH_filter.setItemText(7, _translate("SLS_gui", "7"))
        self.PDH_filter.setItemText(8, _translate("SLS_gui", "8"))
        self.PDH_filter.setItemText(9, _translate("SLS_gui", "9"))
        self.PDH_filter.setItemText(10, _translate("SLS_gui", "10"))
        self.PDH_filter.setItemText(11, _translate("SLS_gui", "11"))
        self.PDH_filter.setItemText(12, _translate("SLS_gui", "12"))
        self.PDH_filter.setItemText(13, _translate("SLS_gui", "13"))
        self.PDH_filter.setItemText(14, _translate("SLS_gui", "14"))
        self.PDH_filter.setItemText(15, _translate("SLS_gui", "15"))
        self.PDH_filter.setItemText(16, _translate("SLS_gui", "16"))
        self.PDH_filter_label.setText(_translate("SLS_gui", "Filter Index"))
        self.PDH_phasemodulation_label.setText(_translate("SLS_gui", "Phase modulation (rad)"))
        self.PDH_phaseoffset_label.setText(_translate("SLS_gui", "Reference phase (deg)"))
        self.servo_filter.setItemText(0, _translate("SLS_gui", "None"))
        self.servo_filter.setItemText(1, _translate("SLS_gui", "1"))
        self.servo_filter.setItemText(2, _translate("SLS_gui", "2"))
        self.servo_filter.setItemText(3, _translate("SLS_gui", "3"))
        self.servo_filter.setItemText(4, _translate("SLS_gui", "4"))
        self.servo_filter.setItemText(5, _translate("SLS_gui", "5"))
        self.servo_filter.setItemText(6, _translate("SLS_gui", "6"))
        self.servo_filter.setItemText(7, _translate("SLS_gui", "7"))
        self.servo_filter.setItemText(8, _translate("SLS_gui", "8"))
        self.servo_filter.setItemText(9, _translate("SLS_gui", "9"))
        self.servo_filter.setItemText(10, _translate("SLS_gui", "10"))
        self.servo_filter.setItemText(11, _translate("SLS_gui", "11"))
        self.servo_filter.setItemText(12, _translate("SLS_gui", "12"))
        self.servo_filter.setItemText(13, _translate("SLS_gui", "13"))
        self.servo_filter.setItemText(14, _translate("SLS_gui", "14"))
        self.servo_filter.setItemText(15, _translate("SLS_gui", "15"))
        self.servo_filter.setItemText(16, _translate("SLS_gui", "16"))
        self.servo_param.setItemText(0, _translate("SLS_gui", "Current"))
        self.servo_param.setItemText(1, _translate("SLS_gui", "PZT"))
        self.servo_param.setItemText(2, _translate("SLS_gui", "TX"))
        self.servo_p_label.setText(_translate("SLS_gui", "Proportional"))
        self.servo_i_label.setText(_translate("SLS_gui", "Integral"))
        self.servo_param_label.setText(_translate("SLS_gui", "Parameter"))
        self.servo_filter_label.setText(_translate("SLS_gui", "Filter Index"))
        self.servo_label.setText(_translate("SLS_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Servo PID</span></p></body></html>"))
        self.servo_d_label.setText(_translate("SLS_gui", "Differential"))
        self.servo_set_label.setText(_translate("SLS_gui", "Setpoint"))
        self.autolock_param_label.setText(_translate("SLS_gui", "Sweep Parameter"))
        self.autolock_time.setText(_translate("SLS_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#0055ff;\">Time</span></p></body></html>"))
        self.autolock_param.setItemText(0, _translate("SLS_gui", "Off"))
        self.autolock_param.setItemText(1, _translate("SLS_gui", "PZT"))
        self.autolock_param.setItemText(2, _translate("SLS_gui", "Current"))
        self.autolock_time_label.setText(_translate("SLS_gui", "Lock Time (d:h:m)"))
        self.autolock_label.setText(_translate("SLS_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Autolock</span></p></body></html>"))
        self.autolock_toggle_label.setText(_translate("SLS_gui", "Autolock"))
        self.autolock_attempts_label.setText(_translate("SLS_gui", "Lock Attempts"))
        self.off_lockpoint_label.setText(_translate("SLS_gui", "Lockpoint"))
        self.off_label.setText(_translate("SLS_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Offset Lock</span></p></body></html>"))
        self.off_freq_label.setText(_translate("SLS_gui", "Offset Frequency (MHz)"))
        self.off_lockpoint.setItemText(0, _translate("SLS_gui", "J(+2)"))
        self.off_lockpoint.setItemText(1, _translate("SLS_gui", "J(+1)"))
        self.off_lockpoint.setItemText(2, _translate("SLS_gui", "Resonance"))
        self.off_lockpoint.setItemText(3, _translate("SLS_gui", "J(-1)"))
        self.off_lockpoint.setItemText(4, _translate("SLS_gui", "J(-2)"))


if __name__ == "__main__":
    from EGGS_labrad.lib.clients import runGUI
    runGUI(SLS_gui)