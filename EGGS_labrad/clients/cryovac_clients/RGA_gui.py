from PyQt5.QtWidgets import QFrame
from PyQt5 import QtCore, QtGui, QtWidgets

from EGGS_labrad.clients.Widgets import Lockswitch


class RGA_gui(QFrame):

    def setupUi(self):
        RGA_gui = self
        RGA_gui.setObjectName("RGA_gui")
        RGA_gui.setFixedSize(650, 445)
        RGA_gui.setFrameStyle(0x0001 | 0x0030)
        self.RGA_label = QtWidgets.QLabel(RGA_gui)
        self.RGA_label.setGeometry(QtCore.QRect(220, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RGA_label.setFont(font)
        self.RGA_label.setObjectName("RGA_label")
        self.layoutWidget = QtWidgets.QWidget(RGA_gui)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 131, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.general_layout = QtWidgets.QGridLayout(self.layoutWidget)
        self.general_layout.setContentsMargins(0, 0, 0, 0)
        self.general_layout.setObjectName("general_layout")
        self.calibrate_electrometer = QtWidgets.QPushButton(self.layoutWidget)
        self.calibrate_electrometer.setObjectName("calibrate_electrometer")
        self.general_layout.addWidget(self.calibrate_electrometer, 4, 1, 1, 1)
        self.calibrate_detector = QtWidgets.QPushButton(self.layoutWidget)
        self.calibrate_detector.setObjectName("calibrate_detector")
        self.general_layout.addWidget(self.calibrate_detector, 3, 1, 1, 1)
        self.initialize = QtWidgets.QPushButton(self.layoutWidget)
        self.initialize.setObjectName("initialize")
        self.general_layout.addWidget(self.initialize, 2, 1, 1, 1)
        self.general_label = QtWidgets.QLabel(self.layoutWidget)
        self.general_label.setObjectName("general_label")
        self.general_layout.addWidget(self.general_label, 0, 1, 1, 1)
        self.general_lockswitch = Lockswitch(self.layoutWidget)
        self.general_lockswitch.setObjectName("general_lockswitch")
        self.general_layout.addWidget(self.general_lockswitch, 1, 1, 1, 1)
        self.degas = QtWidgets.QPushButton(self.layoutWidget)
        self.degas.setObjectName("degas")
        self.general_layout.addWidget(self.degas, 5, 1, 1, 1)
        self.general_tp = QtWidgets.QPushButton(self.layoutWidget)
        self.general_tp.setObjectName("general_tp")
        self.general_layout.addWidget(self.general_tp, 6, 1, 1, 1)
        self.layoutWidget_4 = QtWidgets.QWidget(RGA_gui)
        self.layoutWidget_4.setGeometry(QtCore.QRect(300, 60, 141, 371))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.scan_layout = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.scan_layout.setContentsMargins(0, 0, 0, 0)
        self.scan_layout.setObjectName("scan_layout")
        self.scan_mf_label = QtWidgets.QLabel(self.layoutWidget_4)
        self.scan_mf_label.setObjectName("scan_mf_label")
        self.scan_layout.addWidget(self.scan_mf_label, 10, 1, 1, 1)
        self.scan_mi_label = QtWidgets.QLabel(self.layoutWidget_4)
        self.scan_mi_label.setObjectName("scan_mi_label")
        self.scan_layout.addWidget(self.scan_mi_label, 6, 1, 1, 1)
        self.scan_num = QtWidgets.QDoubleSpinBox(self.layoutWidget_4)
        self.scan_num.setDecimals(0)
        self.scan_num.setMinimum(1.0)
        self.scan_num.setMaximum(255.0)
        self.scan_num.setObjectName("scan_num")
        self.scan_layout.addWidget(self.scan_num, 15, 1, 1, 1)
        self.scan_sa = QtWidgets.QDoubleSpinBox(self.layoutWidget_4)
        self.scan_sa.setDecimals(0)
        self.scan_sa.setMinimum(10.0)
        self.scan_sa.setMaximum(25.0)
        self.scan_sa.setSingleStep(1.0)
        self.scan_sa.setObjectName("scan_sa")
        self.scan_layout.addWidget(self.scan_sa, 13, 1, 1, 1)
        self.scan_type = QtWidgets.QComboBox(self.layoutWidget_4)
        self.scan_type.setObjectName("scan_type")
        self.scan_type.addItem("")
        self.scan_type.addItem("")
        self.scan_type.addItem("")
        self.scan_type.addItem("")
        self.scan_layout.addWidget(self.scan_type, 3, 1, 1, 1)
        self.scan_lockswitch = Lockswitch(self.layoutWidget_4)
        self.scan_lockswitch.setObjectName("scan_lockswitch")
        self.scan_layout.addWidget(self.scan_lockswitch, 1, 1, 1, 1)
        self.scan_sa_label = QtWidgets.QLabel(self.layoutWidget_4)
        self.scan_sa_label.setObjectName("scan_sa_label")
        self.scan_layout.addWidget(self.scan_sa_label, 12, 1, 1, 1)
        self.scan_num_label = QtWidgets.QLabel(self.layoutWidget_4)
        self.scan_num_label.setObjectName("scan_num_label")
        self.scan_layout.addWidget(self.scan_num_label, 14, 1, 1, 1)
        self.scan_type_label = QtWidgets.QLabel(self.layoutWidget_4)
        self.scan_type_label.setObjectName("scan_type_label")
        self.scan_layout.addWidget(self.scan_type_label, 2, 1, 1, 1)
        self.scan_mf = QtWidgets.QDoubleSpinBox(self.layoutWidget_4)
        self.scan_mf.setDecimals(0)
        self.scan_mf.setMaximum(200.0)
        self.scan_mf.setObjectName("scan_mf")
        self.scan_layout.addWidget(self.scan_mf, 11, 1, 1, 1)
        self.scan_label = QtWidgets.QLabel(self.layoutWidget_4)
        self.scan_label.setObjectName("scan_label")
        self.scan_layout.addWidget(self.scan_label, 0, 1, 1, 1)
        self.scan_start = QtWidgets.QPushButton(self.layoutWidget_4)
        self.scan_start.setObjectName("scan_start")
        self.scan_layout.addWidget(self.scan_start, 18, 1, 1, 1)
        self.mass_lock = QtWidgets.QDoubleSpinBox(self.layoutWidget_4)
        self.mass_lock.setDecimals(0)
        self.mass_lock.setMaximum(200.0)
        self.mass_lock.setObjectName("mass_lock")
        self.scan_layout.addWidget(self.mass_lock, 5, 1, 1, 1)
        self.mass_lock_label = QtWidgets.QLabel(self.layoutWidget_4)
        self.mass_lock_label.setObjectName("mass_lock_label")
        self.scan_layout.addWidget(self.mass_lock_label, 4, 1, 1, 1)
        self.scan_mi = QtWidgets.QDoubleSpinBox(self.layoutWidget_4)
        self.scan_mi.setDecimals(0)
        self.scan_mi.setMinimum(0.0)
        self.scan_mi.setMaximum(200.0)
        self.scan_mi.setObjectName("scan_mi")
        self.scan_layout.addWidget(self.scan_mi, 7, 1, 1, 1)
        self.layoutWidget_3 = QtWidgets.QWidget(RGA_gui)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 270, 131, 161))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.detector_layout = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.detector_layout.setContentsMargins(0, 0, 0, 0)
        self.detector_layout.setObjectName("detector_layout")
        self.detector_cv_label = QtWidgets.QLabel(self.layoutWidget_3)
        self.detector_cv_label.setObjectName("detector_cv_label")
        self.detector_layout.addWidget(self.detector_cv_label, 3, 1, 1, 1)
        self.detector_lockswitch = Lockswitch(self.layoutWidget_3)
        self.detector_lockswitch.setObjectName("detector_lockswitch")
        self.detector_layout.addWidget(self.detector_lockswitch, 2, 1, 1, 1)
        self.detector_hv = QtWidgets.QDoubleSpinBox(self.layoutWidget_3)
        self.detector_hv.setDecimals(0)
        self.detector_hv.setMinimum(10)
        self.detector_hv.setMaximum(2490)
        self.detector_hv.setSingleStep(1)
        self.detector_hv.setObjectName("detector_hv")
        self.detector_layout.addWidget(self.detector_hv, 4, 1, 1, 1)
        self.detector_nf_label = QtWidgets.QLabel(self.layoutWidget_3)
        self.detector_nf_label.setObjectName("detector_nf_label")
        self.detector_layout.addWidget(self.detector_nf_label, 5, 1, 1, 1)
        self.detector_nf = QtWidgets.QComboBox(self.layoutWidget_3)
        self.detector_nf.setObjectName("detector_nf")
        self.detector_nf.addItem("")
        self.detector_nf.addItem("")
        self.detector_nf.addItem("")
        self.detector_nf.addItem("")
        self.detector_nf.addItem("")
        self.detector_nf.addItem("")
        self.detector_nf.addItem("")
        self.detector_nf.addItem("")
        self.detector_layout.addWidget(self.detector_nf, 6, 1, 1, 1)
        self.detector_label = QtWidgets.QLabel(self.layoutWidget_3)
        self.detector_label.setObjectName("detector_label")
        self.detector_layout.addWidget(self.detector_label, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(RGA_gui)
        self.layoutWidget1.setGeometry(QtCore.QRect(160, 60, 131, 251))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.ionizer_layout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.ionizer_layout.setContentsMargins(0, 0, 0, 0)
        self.ionizer_layout.setObjectName("ionizer_layout")
        self.ionizer_vf_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ionizer_vf_label.setObjectName("ionizer_vf_label")
        self.ionizer_layout.addWidget(self.ionizer_vf_label, 5, 0, 1, 1)
        self.ionizer_lockswitch = Lockswitch(self.layoutWidget1)
        self.ionizer_lockswitch.setObjectName("ionizer_lockswitch")
        self.ionizer_layout.addWidget(self.ionizer_lockswitch, 2, 0, 1, 1)
        self.ionizer_ee = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.ionizer_ee.setDecimals(0)
        self.ionizer_ee.setMinimum(25.0)
        self.ionizer_ee.setMaximum(105.0)
        self.ionizer_ee.setSingleStep(1.0)
        self.ionizer_ee.setObjectName("ionizer_ee")
        self.ionizer_layout.addWidget(self.ionizer_ee, 8, 0, 1, 1)
        self.ionizer_ie_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ionizer_ie_label.setObjectName("ionizer_ie_label")
        self.ionizer_layout.addWidget(self.ionizer_ie_label, 9, 0, 1, 1)
        self.ionizer_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ionizer_label.setObjectName("ionizer_label")
        self.ionizer_layout.addWidget(self.ionizer_label, 1, 0, 1, 1)
        self.ionizer_ee_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ionizer_ee_label.setObjectName("ionizer_ee_label")
        self.ionizer_layout.addWidget(self.ionizer_ee_label, 7, 0, 1, 1)
        self.ionizer_ie = QtWidgets.QComboBox(self.layoutWidget1)
        self.ionizer_ie.setObjectName("ionizer_ie")
        self.ionizer_ie.addItem("")
        self.ionizer_ie.addItem("")
        self.ionizer_layout.addWidget(self.ionizer_ie, 10, 0, 2, 1)
        self.ionizer_fl_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ionizer_fl_label.setObjectName("ionizer_fl_label")
        self.ionizer_layout.addWidget(self.ionizer_fl_label, 3, 0, 1, 1)
        self.ionizer_fl = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.ionizer_fl.setDecimals(2)
        self.ionizer_fl.setMinimum(0.0)
        self.ionizer_fl.setMaximum(3.5)
        self.ionizer_fl.setSingleStep(0.1)
        self.ionizer_fl.setObjectName("ionizer_fl")
        self.ionizer_layout.addWidget(self.ionizer_fl, 4, 0, 1, 1)
        self.ionizer_vf = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.ionizer_vf.setDecimals(0)
        self.ionizer_vf.setMinimum(0)
        self.ionizer_vf.setMaximum(150)
        self.ionizer_vf.setSingleStep(1)
        self.ionizer_vf.setObjectName("ionizer_vf")
        self.ionizer_layout.addWidget(self.ionizer_vf, 6, 0, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(RGA_gui)
        self.layoutWidget2.setGeometry(QtCore.QRect(450, 60, 181, 371))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.buffer_layout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.buffer_layout.setContentsMargins(0, 0, 0, 0)
        self.buffer_layout.setObjectName("buffer_layout")
        self.buffer_label = QtWidgets.QLabel(self.layoutWidget2)
        self.buffer_label.setObjectName("buffer_label")
        self.buffer_layout.addWidget(self.buffer_label, 0, 0, 1, 1)
        self.buffer_readout = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        self.buffer_readout.setObjectName("buffer_readout")
        self.buffer_layout.addWidget(self.buffer_readout, 1, 0, 1, 1)
        self.buffer_clear = QtWidgets.QPushButton(self.layoutWidget2)
        self.buffer_clear.setObjectName("buffer_clear")
        self.buffer_layout.addWidget(self.buffer_clear, 2, 0, 1, 1)

        self.retranslateUi(RGA_gui)
        QtCore.QMetaObject.connectSlotsByName(RGA_gui)

    def retranslateUi(self, RGA_gui):
        _translate = QtCore.QCoreApplication.translate
        RGA_gui.setWindowTitle(_translate("RGA_gui", "SRS RGA Client"))
        self.RGA_label.setText(_translate("RGA_gui", "<html><head/><body><p>SRS RGA Client</p></body></html>"))
        self.calibrate_electrometer.setText(_translate("RGA_gui", "Calibrate Electrometer"))
        self.calibrate_detector.setText(_translate("RGA_gui", "Calibrate Detector"))
        self.initialize.setText(_translate("RGA_gui", "Initialize"))
        self.general_label.setText(_translate("RGA_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">General</span></p></body></html>"))
        self.degas.setText(_translate("RGA_gui", "Degas"))
        self.general_tp.setText(_translate("RGA_gui", "Total Pressure"))
        self.scan_mf_label.setText(_translate("RGA_gui", "Stop Mass (amu)"))
        self.scan_mi_label.setText(_translate("RGA_gui", "Start Mass (amu)"))
        self.scan_type.setItemText(0, _translate("RGA_gui", "Analog"))
        self.scan_type.setItemText(1, _translate("RGA_gui", "Histogram"))
        self.scan_type.setItemText(2, _translate("RGA_gui", "Single Mass"))
        self.scan_type.setItemText(3, _translate("RGA_gui", "Total Pressure"))
        self.scan_sa_label.setText(_translate("RGA_gui", "Steps per amu"))
        self.scan_num_label.setText(_translate("RGA_gui", "Number of scans"))
        self.scan_type_label.setText(_translate("RGA_gui", "Type"))
        self.scan_label.setText(_translate("RGA_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Scan</span></p></body></html>"))
        self.scan_start.setText(_translate("RGA_gui", "Start"))
        self.mass_lock_label.setText(_translate("RGA_gui", "Mass Lock"))
        self.detector_cv_label.setText(_translate("RGA_gui", "CDEM Voltage (V)"))
        self.detector_nf_label.setText(_translate("RGA_gui", "Noise Floor"))
        self.detector_nf.setItemText(0, _translate("RGA_gui", "0"))
        self.detector_nf.setItemText(1, _translate("RGA_gui", "1"))
        self.detector_nf.setItemText(2, _translate("RGA_gui", "2"))
        self.detector_nf.setItemText(3, _translate("RGA_gui", "3"))
        self.detector_nf.setItemText(4, _translate("RGA_gui", "4"))
        self.detector_nf.setItemText(5, _translate("RGA_gui", "5"))
        self.detector_nf.setItemText(6, _translate("RGA_gui", "6"))
        self.detector_nf.setItemText(7, _translate("RGA_gui", "7"))
        self.detector_label.setText(_translate("RGA_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Detector</span></p></body></html>"))
        self.ionizer_vf_label.setText(_translate("RGA_gui", "Focus Voltage (V)"))
        self.ionizer_ie_label.setText(_translate("RGA_gui", "Ion Energy (eV)"))
        self.ionizer_label.setText(_translate("RGA_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Ionizer</span></p></body></html>"))
        self.ionizer_ee_label.setText(_translate("RGA_gui", "Electron Energy (eV)"))
        self.ionizer_ie.setItemText(0, _translate("RGA_gui", "8"))
        self.ionizer_ie.setItemText(1, _translate("RGA_gui", "12"))
        self.ionizer_fl_label.setText(_translate("RGA_gui", "Filament Current (mA)"))
        self.buffer_label.setText(_translate("RGA_gui", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Buffer</span></p></body></html>"))
        self.buffer_clear.setText(_translate("RGA_gui", "Clear"))


if __name__ == "__main__":
    from EGGS_labrad.clients import runGUI
    runGUI(RGA_gui)