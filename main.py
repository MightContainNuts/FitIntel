import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QMenuBar, QAction
)
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class HealthDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        # Title
        title = QLabel("Health Tracker Dashboard")
        title.setFont(QFont("Arial", 16))
        layout.addWidget(title)

        # Chart area (placeholder)

        layout.addWidget(self.canvas)
        self.plot_sample_data()

        self.setLayout(layout)

    def plot_sample_data(self):
        ax = self.canvas.figure.add_subplot(111)
        ax.set_title("Sample Heart Rate")
        ax.plot([60, 70, 75, 72, 68, 65, 62], marker="o")
        ax.set_ylabel("BPM")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VitalScope")
        self.setGeometry(100, 100, 800, 600)

        self.menu_bar = self.menuBar()
        self._create_menu()

        self.dashboard = HealthDashboard()
        self.setCentralWidget(self.dashboard)

    def _create_menu(self):
        sync_menu = self.menu_bar.addMenu("Sync Data")
        export_menu = self.menu_bar.addMenu("Export Data")

        sync_action = QAction("Synchronize Data", self)
        export_action = QAction("Export Data", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        sync_menu.addAction(sync_action)
        sync_menu.addAction(exit_action)
        export_menu.addAction(export_action)
        export_menu.addAction(exit_action)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())