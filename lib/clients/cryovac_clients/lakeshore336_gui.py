from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFrame
from PyQt5.QtGui import QFont

from EGGS_labrad.lib.clients.Widgets import TextChangingButton as _TextChangingButton

class TextChangingButton(_TextChangingButton):
    def __init__(self, button_text=None, parent=None):
        super(TextChangingButton, self).__init__(button_text, parent)
        self.setMaximumHeight(30)


class lakeshore336_gui(QFrame):

    def setupUi(self):
        shell_font = 'MS Shell Dlg 2'
        lakeshore336_gui = self
        lakeshore336_gui.setObjectName("lakeshore336_gui")
        lakeshore336_gui.setFixedSize(517, 555)
        lakeshore336_gui.setFrameStyle(0x0001 | 0x0030)
        self.lakeshore_label = QtWidgets.QLabel(lakeshore336_gui)
        self.lakeshore_label.setGeometry(QtCore.QRect(30, 20, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lakeshore_label.setFont(font)
        self.lakeshore_label.setObjectName("lakeshore_label")
        self.heatAll_label = QtWidgets.QLabel(lakeshore336_gui)
        self.heatAll_label.setGeometry(QtCore.QRect(270, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.heatAll_label.setFont(font)
        self.heatAll_label.setObjectName("heatAll_label")
        self.tempAll_label = QtWidgets.QLabel(lakeshore336_gui)
        self.tempAll_label.setGeometry(QtCore.QRect(10, 70, 209, 24))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tempAll_label.setFont(font)
        self.tempAll_label.setObjectName("tempAll_label")
        self.heatAll_lockswitch = TextChangingButton(('Locked', 'Unlocked'), self)
        self.heatAll_lockswitch.setGeometry(QtCore.QRect(290, 110, 139, 23))
        self.heatAll_lockswitch.setObjectName("heatAll_lockswitch")
        self.tempAll_record = TextChangingButton(('Stop Recording', 'Start Recording'), self)
        self.tempAll_record.setGeometry(QtCore.QRect(30, 110, 159, 23))
        self.tempAll_record.setObjectName("tempAll_record")
        self.layoutWidget = QtWidgets.QWidget(lakeshore336_gui)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 150, 161, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.temp_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.temp_layout.setContentsMargins(0, 0, 0, 0)
        self.temp_layout.setObjectName("temp_layout")
        self.temp1_label = QtWidgets.QLabel(self.layoutWidget)
        self.temp1_label.setObjectName("temp1_label")
        self.temp_layout.addWidget(self.temp1_label)
        self.temp1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.temp1.setFont(font)
        self.temp1.setAlignment(QtCore.Qt.AlignCenter)
        self.temp1.setObjectName("temp1")
        self.temp_layout.addWidget(self.temp1)
        self.temp2_label = QtWidgets.QLabel(self.layoutWidget)
        self.temp2_label.setObjectName("temp2_label")
        self.temp_layout.addWidget(self.temp2_label)
        self.temp2 = QtWidgets.QLabel(self.layoutWidget)
        self.temp2.setAlignment(QtCore.Qt.AlignCenter)
        self.temp2.setObjectName("temp2")
        self.temp_layout.addWidget(self.temp2)
        self.temp3_label = QtWidgets.QLabel(self.layoutWidget)
        self.temp3_label.setObjectName("temp3_label")
        self.temp_layout.addWidget(self.temp3_label)
        self.temp3 = QtWidgets.QLabel(self.layoutWidget)
        self.temp3.setAlignment(QtCore.Qt.AlignCenter)
        self.temp3.setObjectName("temp3")
        self.temp_layout.addWidget(self.temp3)
        self.temp4_label = QtWidgets.QLabel(self.layoutWidget)
        self.temp4_label.setObjectName("temp4_label")
        self.temp_layout.addWidget(self.temp4_label)
        self.temp4 = QtWidgets.QLabel(self.layoutWidget)
        self.temp4.setAlignment(QtCore.Qt.AlignCenter)
        self.temp4.setObjectName("temp4")
        self.temp_layout.addWidget(self.temp4)
        self.layoutWidget1 = QtWidgets.QWidget(lakeshore336_gui)
        self.layoutWidget1.setGeometry(QtCore.QRect(220, 150, 280, 392))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.heatAll_layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.heatAll_layout.setContentsMargins(0, 0, 0, 0)
        self.heatAll_layout.setObjectName("heatAll_layout")
        self.heat1_layout = QtWidgets.QVBoxLayout()
        self.heat1_layout.setObjectName("heat1_layout")
        self.heat1_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.heat1_label.setFont(font)
        self.heat1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.heat1_label.setObjectName("heat1_label")
        self.heat1_layout.addWidget(self.heat1_label)
        self.heat1_out_curr_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat1_out_curr_label.setObjectName("heat1_out_curr_label")
        self.heat1_layout.addWidget(self.heat1_out_curr_label)
        self.heat1_out_curr = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.heat1_out_curr.setFont(font)
        self.heat1_out_curr.setAlignment(QtCore.Qt.AlignCenter)
        self.heat1_out_curr.setObjectName("heat1_out_curr")
        self.heat1_layout.addWidget(self.heat1_out_curr)
        self.heat1_mode_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat1_mode_label.setObjectName("heat1_mode_label")
        self.heat1_layout.addWidget(self.heat1_mode_label)
        self.heat1_mode = QtWidgets.QComboBox(self.layoutWidget1)
        self.heat1_mode.setObjectName("heat1_mode")
        self.heat1_mode.addItem("")
        self.heat1_mode.addItem("")
        self.heat1_mode.addItem("")
        self.heat1_mode.addItem("")
        self.heat1_layout.addWidget(self.heat1_mode)
        self.heat1_in_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat1_in_label.setObjectName("heat1_in_label")
        self.heat1_layout.addWidget(self.heat1_in_label)
        self.heat1_in = QtWidgets.QComboBox(self.layoutWidget1)
        self.heat1_in.setObjectName("heat1_in")
        self.heat1_in.addItem("")
        self.heat1_in.addItem("")
        self.heat1_in.addItem("")
        self.heat1_in.addItem("")
        self.heat1_layout.addWidget(self.heat1_in)
        self.heat1_res_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat1_res_label.setObjectName("heat1_res_label")
        self.heat1_layout.addWidget(self.heat1_res_label)
        self.heat1_res = QtWidgets.QComboBox(self.layoutWidget1)
        self.heat1_res.setObjectName("heat1_res")
        self.heat1_res.addItem("")
        self.heat1_res.addItem("")
        self.heat1_layout.addWidget(self.heat1_res)
        self.heat1_curr_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat1_curr_label.setObjectName("heat1_curr_label")
        self.heat1_layout.addWidget(self.heat1_curr_label)
        self.heat1_curr = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.heat1_curr.setObjectName("heat1_curr")
        self.heat1_layout.addWidget(self.heat1_curr)
        self.heat1_range_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat1_range_label.setObjectName("heat1_range_label")
        self.heat1_layout.addWidget(self.heat1_range_label)
        self.heat1_range = QtWidgets.QComboBox(self.layoutWidget1)
        self.heat1_range.setObjectName("heat1_range")
        self.heat1_range.addItem("")
        self.heat1_range.addItem("")
        self.heat1_range.addItem("")
        self.heat1_range.addItem("")
        self.heat1_layout.addWidget(self.heat1_range)
        self.heat1_p1_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat1_p1_label.setObjectName("heat1_p1_label")
        self.heat1_layout.addWidget(self.heat1_p1_label)
        self.heat1_p1 = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.heat1_p1.setMaximum(100.0)
        self.heat1_p1.setObjectName("heat1_p1")
        self.heat1_layout.addWidget(self.heat1_p1)
        self.heat1_set_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat1_set_label.setObjectName("heat1_set_label")
        self.heat1_layout.addWidget(self.heat1_set_label)
        self.heat1_set = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.heat1_set.setObjectName("heat1_set")
        self.heat1_layout.addWidget(self.heat1_set)
        self.heatAll_layout.addLayout(self.heat1_layout)
        self.heat2_layout = QtWidgets.QVBoxLayout()
        self.heat2_layout.setObjectName("heat2_layout")
        self.heat2_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.heat2_label.setFont(font)
        self.heat2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.heat2_label.setObjectName("heat2_label")
        self.heat2_layout.addWidget(self.heat2_label)
        self.heat2_out_curr = QtWidgets.QLabel(self.layoutWidget1)
        self.heat2_out_curr.setObjectName("heat2_out_curr")
        self.heat2_layout.addWidget(self.heat2_out_curr)
        self.heat2_out_curr_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.heat2_out_curr_label.setFont(font)
        self.heat2_out_curr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.heat2_out_curr_label.setObjectName("heat2_out_curr_label")
        self.heat2_layout.addWidget(self.heat2_out_curr_label)
        self.heat2_mode_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat2_mode_label.setObjectName("heat2_mode_label")
        self.heat2_layout.addWidget(self.heat2_mode_label)
        self.heat2_mode = QtWidgets.QComboBox(self.layoutWidget1)
        self.heat2_mode.setObjectName("heat2_mode")
        self.heat2_mode.addItem("")
        self.heat2_mode.addItem("")
        self.heat2_mode.addItem("")
        self.heat2_mode.addItem("")
        self.heat2_layout.addWidget(self.heat2_mode)
        self.heat2_in_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat2_in_label.setObjectName("heat2_in_label")
        self.heat2_layout.addWidget(self.heat2_in_label)
        self.heat2_in = QtWidgets.QComboBox(self.layoutWidget1)
        self.heat2_in.setObjectName("heat2_in")
        self.heat2_in.addItem("")
        self.heat2_in.addItem("")
        self.heat2_in.addItem("")
        self.heat2_in.addItem("")
        self.heat2_layout.addWidget(self.heat2_in)
        self.heat2_res_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat2_res_label.setObjectName("heat2_res_label")
        self.heat2_layout.addWidget(self.heat2_res_label)
        self.heat2_res = QtWidgets.QComboBox(self.layoutWidget1)
        self.heat2_res.setObjectName("heat2_res")
        self.heat2_res.addItem("")
        self.heat2_res.addItem("")
        self.heat2_layout.addWidget(self.heat2_res)
        self.heat2_curr_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat2_curr_label.setObjectName("heat2_curr_label")
        self.heat2_layout.addWidget(self.heat2_curr_label)
        self.heat2_curr = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.heat2_curr.setObjectName("heat2_curr")
        self.heat2_layout.addWidget(self.heat2_curr)
        self.heat2_range_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat2_range_label.setObjectName("heat2_range_label")
        self.heat2_layout.addWidget(self.heat2_range_label)
        self.heat2_range = QtWidgets.QComboBox(self.layoutWidget1)
        self.heat2_range.setObjectName("heat2_range")
        self.heat2_range.addItem("")
        self.heat2_range.addItem("")
        self.heat2_range.addItem("")
        self.heat2_range.addItem("")
        self.heat2_layout.addWidget(self.heat2_range)
        self.heat2_p1_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat2_p1_label.setObjectName("heat2_p1_label")
        self.heat2_layout.addWidget(self.heat2_p1_label)
        self.heat2_p1 = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.heat2_p1.setMaximum(100.0)
        self.heat2_p1.setObjectName("heat2_p1")
        self.heat2_layout.addWidget(self.heat2_p1)
        self.heat2_set_label = QtWidgets.QLabel(self.layoutWidget1)
        self.heat2_set_label.setObjectName("heat2_set_label")
        self.heat2_layout.addWidget(self.heat2_set_label)
        self.heat2_set = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.heat2_set.setObjectName("heat2_set")
        self.heat2_layout.addWidget(self.heat2_set)
        self.heatAll_layout.addLayout(self.heat2_layout)

        self.retranslateUi(lakeshore336_gui)
        QtCore.QMetaObject.connectSlotsByName(lakeshore336_gui)

    def retranslateUi(self, lakeshore336_gui):
        _translate = QtCore.QCoreApplication.translate
        lakeshore336_gui.setWindowTitle(_translate("lakeshore336_gui", "Lakeshore 336 Temperature Controller"))
        self.lakeshore_label.setText(_translate("lakeshore336_gui", "<html><head/><body><p><span style=\" font-size:20pt;\">Lakeshore 336 Temperature Controller</span></p></body></html>"))
        self.heatAll_label.setText(_translate("lakeshore336_gui", "Heater Configuration"))
        self.tempAll_label.setText(_translate("lakeshore336_gui", "Temperature Readout "))
        self.temp1_label.setText(_translate("lakeshore336_gui", "Diode 1 (K)"))
        self.temp1.setText(_translate("lakeshore336_gui", "<html><head/><body><p><span style=\" font-size:24pt; color:#0055ff;\">Temp 1</span></p></body></html>"))
        self.temp2_label.setText(_translate("lakeshore336_gui", "Diode 2 (K)"))
        self.temp2.setText(_translate("lakeshore336_gui", "<html><head/><body><p><span style=\" font-size:24pt; color:#0055ff;\">Temp 2</span></p></body></html>"))
        self.temp3_label.setText(_translate("lakeshore336_gui", "Diode 3 (K)"))
        self.temp3.setText(_translate("lakeshore336_gui", "<html><head/><body><p><span style=\" font-size:24pt; color:#0055ff;\">Temp 3</span></p></body></html>"))
        self.temp4_label.setText(_translate("lakeshore336_gui", "Diode 4 (K)"))
        self.temp4.setText(_translate("lakeshore336_gui", "<html><head/><body><p><span style=\" font-size:24pt; color:#0055ff;\">Temp 4</span></p></body></html>"))
        self.heat1_label.setText(_translate("lakeshore336_gui", "Heater 1"))
        self.heat1_out_curr_label.setText(_translate("lakeshore336_gui", "Output Current (A)"))
        self.heat1_out_curr.setText(_translate("lakeshore336_gui", "<html><head/><body><p><span style=\" font-size:18pt; color:#ff0000;\">Current 1</span></p></body></html>"))
        self.heat1_mode_label.setText(_translate("lakeshore336_gui", "Mode"))
        self.heat1_mode.setItemText(0, _translate("lakeshore336_gui", "Off"))
        self.heat1_mode.setItemText(1, _translate("lakeshore336_gui", "Autotune"))
        self.heat1_mode.setItemText(2, _translate("lakeshore336_gui", "PID"))
        self.heat1_mode.setItemText(3, _translate("lakeshore336_gui", "Manual"))
        self.heat1_in_label.setText(_translate("lakeshore336_gui", "Input"))
        self.heat1_in.setItemText(0, _translate("lakeshore336_gui", "1"))
        self.heat1_in.setItemText(1, _translate("lakeshore336_gui", "2"))
        self.heat1_in.setItemText(2, _translate("lakeshore336_gui", "3"))
        self.heat1_in.setItemText(3, _translate("lakeshore336_gui", "4"))
        self.heat1_res_label.setText(_translate("lakeshore336_gui", "Resistance (Ohms)"))
        self.heat1_res.setItemText(0, _translate("lakeshore336_gui", "25"))
        self.heat1_res.setItemText(1, _translate("lakeshore336_gui", "50"))
        self.heat1_curr_label.setText(_translate("lakeshore336_gui", "Max. Current (A)"))
        self.heat1_range_label.setText(_translate("lakeshore336_gui", "Range"))
        self.heat1_range.setItemText(0, _translate("lakeshore336_gui", "0"))
        self.heat1_range.setItemText(1, _translate("lakeshore336_gui", "1"))
        self.heat1_range.setItemText(2, _translate("lakeshore336_gui", "2"))
        self.heat1_range.setItemText(3, _translate("lakeshore336_gui", "3"))
        self.heat1_p1_label.setText(_translate("lakeshore336_gui", "Current (% max allowed)"))
        self.heat1_set_label.setText(_translate("lakeshore336_gui", "Setpoint (K)"))
        self.heat2_label.setText(_translate("lakeshore336_gui", "Heater 2"))
        self.heat2_out_curr.setText(_translate("lakeshore336_gui", "Output Current (A)"))
        self.heat2_out_curr_label.setText(_translate("lakeshore336_gui", "<html><head/><body><p><span style=\" font-size:18pt; color:#ff0000;\">Current 2</span></p></body></html>"))
        self.heat2_mode_label.setText(_translate("lakeshore336_gui", "Mode"))
        self.heat2_mode.setItemText(0, _translate("lakeshore336_gui", "Off"))
        self.heat2_mode.setItemText(1, _translate("lakeshore336_gui", "Autotune"))
        self.heat2_mode.setItemText(2, _translate("lakeshore336_gui", "PID"))
        self.heat2_mode.setItemText(3, _translate("lakeshore336_gui", "Manual"))
        self.heat2_in_label.setText(_translate("lakeshore336_gui", "Input"))
        self.heat2_in.setItemText(0, _translate("lakeshore336_gui", "1"))
        self.heat2_in.setItemText(1, _translate("lakeshore336_gui", "2"))
        self.heat2_in.setItemText(2, _translate("lakeshore336_gui", "3"))
        self.heat2_in.setItemText(3, _translate("lakeshore336_gui", "4"))
        self.heat2_res_label.setText(_translate("lakeshore336_gui", "Resistance (Ohms)"))
        self.heat2_res.setItemText(0, _translate("lakeshore336_gui", "25"))
        self.heat2_res.setItemText(1, _translate("lakeshore336_gui", "50"))
        self.heat2_curr_label.setText(_translate("lakeshore336_gui", "Max. Current (A)"))
        self.heat2_range_label.setText(_translate("lakeshore336_gui", "Range"))
        self.heat2_range.setItemText(0, _translate("lakeshore336_gui", "0"))
        self.heat2_range.setItemText(1, _translate("lakeshore336_gui", "1"))
        self.heat2_range.setItemText(2, _translate("lakeshore336_gui", "2"))
        self.heat2_range.setItemText(3, _translate("lakeshore336_gui", "3"))
        self.heat2_p1_label.setText(_translate("lakeshore336_gui", "Current (% max allowed)"))
        self.heat2_set_label.setText(_translate("lakeshore336_gui", "Setpoint (K)"))


if __name__ == "__main__":
    from EGGS_labrad.lib.clients import runGUI
    runGUI(lakeshore336_gui)