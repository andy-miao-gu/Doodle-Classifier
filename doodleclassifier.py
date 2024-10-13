from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow




class DoodleClassifer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Doodle Classifier")
        self.setGeometry(500, 300, 800, 600)

