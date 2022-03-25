# Importing necessary modules
import sys
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel, QPushButton, QLineEdit)
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
        # -------- Username or Email field
        user_or_email_lbl = QLabel('Enter your username or email address',self)
        user_or_email_lbl.setFont(QFont("Tahoma",10))
        user_or_email_lbl.move(44, 308)
        
        self.user_or_email_entry = QLineEdit(self)
        self.user_or_email_entry.resize(451,57)
        self.user_or_email_entry.move(44, 345)
        self.user_or_email_entry.setFont(QFont("Tahoma",12))
        self.user_or_email_entry.setStyleSheet("padding:10px 20px;border-radius:4px;background-color:#FFFFFF;border: 1px solid #4285F4")
        self.user_or_email_entry.setPlaceholderText("Username or email address")
        
        # -------- Password field:
        password_lbl = QLabel('Enter your password',self)
        password_lbl.setFont(QFont("Tahoma",10))
        password_lbl.move(44, 438)
        
        self.password_entry = QLineEdit(self)
        self.password_entry.resize(451,57)
        self.password_entry.move(44, 475)
        self.password_entry.setFont(QFont("Tahoma",12))
        self.password_entry.setStyleSheet("padding:10px 20px;border-radius:4px;background-color:#FFFFFF;border: 1px solid #4285F4")
        self.password_entry.setPlaceholderText("Password")
        
        # ------ Forget password: btn
        forget_btn = QPushButton("forget PASSWORD",self)
        forget_btn.setFont(QFont("Tahoma",9))
        forget_btn.move(370, 544)
        forget_btn.setStyleSheet("background-color:transparent;color:#4285F4")
        
        # Sign in button
        signin_btn = QPushButton("Sign in",self)
        signin_btn.setFont(QFont("Tahoma",10))
        signin_btn.move(259, 608)
        signin_btn.resize(236, 54)
        signin_btn.setStyleSheet("background-color: #779341;color:#fff;border-radius:4px")
    
        

# execution code for this gui
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myGui = LogInGUI()
    sys.exit(app.exec_())