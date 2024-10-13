from PyQt5.QtWidgets import QApplication
import sys
from doodleclassifier import DoodleClassifer


app = QApplication(sys.argv)
window = DoodleClassifer()
window.show()
sys.exit(app.exec_())