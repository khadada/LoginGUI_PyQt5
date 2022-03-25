# Importing necessary modules
import sys
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel, QPushButton)
from PyQt5.QtGui import QPixmap #=> To work with icons
from PyQt5.QtGui import QFont
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
        # display widgets in the screen:
        self.display_components()
        
    def display_components(self):
        """
        setup the components in our GUI
        """
        welcome_lbl = QLabel('Welcome to',self)
        welcome_lbl.setFont(QFont("Tahoma",16))
        welcome_lbl.move(44, 44)
        
        owner_projet_lbl = QLabel('Khaled GUI',self)
        owner_projet_lbl.setFont(QFont("Tahoma",16))
        owner_projet_lbl.move(200, 44)
        owner_projet_lbl.setStyleSheet('color:#779341')
        
        signin_lbl = QLabel('Sign in',self)
        signin_lbl.setFont(QFont("Tahoma",50))
        signin_lbl.move(44, 77)
        # signin_lbl.setStyleSheet('color:#779341')
        
        
        
    
        

# execution code for this gui
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myGui = LogInGUI()
    sys.exit(app.exec_())