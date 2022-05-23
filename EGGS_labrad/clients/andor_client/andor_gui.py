import pyqtgraph as pg
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QDoubleSpinBox, QSpinBox,\
    QPushButton, QCheckBox, QLineEdit, QSizePolicy

from twisted.internet.defer import inlineCallbacks
# todo: document
# todo: make dark mode


class AndorGUI(QWidget):
    """
    A GUI for Andor iXon cameras.
    """

    def __init__(self):
        super().__init__()
        self.makeLayout()
        self.connectLayout()

    def makeLayout(self):
        self.setWindowTitle("Andor")

        # layout
        layout = QGridLayout()
        self.plt = plt = pg.PlotItem()
        self.img_view = pg.ImageView(view=self.plt)
        plt.showAxis('top')
        plt.hideAxis('bottom')
        plt.setAspectLocked(True)
        self.img_view.getHistogramWidget().setHistogramRange(0, 1000)
        exposure_label = QLabel("Exposure")
        exposure_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.exposureSpinBox = QDoubleSpinBox()
        self.exposureSpinBox.setDecimals(3)
        self.exposureSpinBox.setSingleStep(0.001)
        self.exposureSpinBox.setRange(0.0, 10000.0)
        self.exposureSpinBox.setKeyboardTracking(False)
        self.exposureSpinBox.setSuffix(' s')

        # EMCCD Gain
        emccd_label = QLabel("EMCCD Gain")
        emccd_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.emccdSpinBox = QSpinBox()
        self.emccdSpinBox.setSingleStep(1)
        # todo fix
        # self.emrange = yield self.server.getemrange(None)
        mingain, maxgain = self.emrange
        self.emccdSpinBox.setRange(mingain, maxgain)
        self.emccdSpinBox.setKeyboardTracking(False)
        self.live_button = QPushButton("Live Video")
        self.live_button.setCheckable(True)
        self.set_image_region_button = QPushButton("Set Image Region")
        self.save_images = QCheckBox('Save Images')

        # controlling the display buttons
        self.view_all_button = QPushButton("View All")
        self.auto_levels_button = QPushButton("Auto Levels")

        # display mode buttons
        self.trigger_mode = QLineEdit()
        self.trigger_mode.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.trigger_mode.setReadOnly(True)
        self.acquisition_mode = QLineEdit()
        self.acquisition_mode.setReadOnly(True)
        self.acquisition_mode.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        label = QLabel("Trigger Mode")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(label, 1, 2)
        label = QLabel("Acquisition Mode")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # add lines for the cross
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        plt.addItem(self.vLine, ignoreBounds=True)
        plt.addItem(self.hLine, ignoreBounds=True)

        # lay out
        layout.addWidget(self.img_view, 0, 0, 1, 6)
        layout.addWidget(exposure_label, 1, 4, )
        layout.addWidget(self.exposureSpinBox, 1, 5)

        layout.addWidget(self.live_button,                  1, 0)
        layout.addWidget(self.set_image_region_button,      2, 0)
        layout.addWidget(self.save_images,                  3, 0)

        layout.addWidget(label, 2, 2)
        layout.addWidget(self.trigger_mode, 1, 3)
        layout.addWidget(self.acquisition_mode, 2, 3)
        layout.addWidget(emccd_label, 2, 4, )
        layout.addWidget(self.emccdSpinBox, 2, 5)
        layout.addWidget(self.view_all_button, 1, 1)
        layout.addWidget(self.auto_levels_button, 2, 1)

    def connectLayout(self):
        self.set_image_region_button.clicked.connect(self.on_set_image_region)
        self.plt.scene().sigMouseClicked.connect(self.mouse_clicked)
        self.auto_levels_button.clicked.connect(self.on_auto_levels_button)
        self.view_all_button.clicked.connect(self.on_auto_range_button)

    def mouse_clicked(self, event):
        """
        Draws the cross at the position of a double click.
        """
        pos = event.pos()
        if self.plt.sceneBoundingRect().contains(pos) and event.double():
            # only on double clicks within bounds
            mousePoint = self.plt.vb.mapToView(pos)
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())

    def on_auto_levels_button(self, checked):
        self.img_view.autoLevels()

    def on_auto_range_button(self, checked):
        self.img_view.autoRange()

    def get_image_header(self):
        header = ""
        shutter_time = self.exposureSpinBox.value()
        header += "shutter_time " + str(shutter_time) + "\n"
        em_gain = self.emccdSpinBox.value()
        header += "em_gain " + str(em_gain)
        return header


if __name__ == "__main__":
    from EGGS_labrad.clients import runGUI
    runGUI(AndorGUI)
