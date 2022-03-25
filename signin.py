# Importing necessary modules
import sys
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel, QPushButton)
from PyQt5.QtGui import QPixmap #=> To work with icons

# our login gui
class LogInGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    def initialize_ui(self):
        """
        initialize neccesary widget in the screen.
        """
        self.setGeometry(0, 0, 539, 741)
        self.setWindowTitle("Login v 1.0")
        self.setStyleSheet("background-color:rgb(250, 250, 250)")
        

# execution code for this gui
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myGui = LogInGUI()
    sys.exit(app.exec_())