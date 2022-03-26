# Importing necessary modules
import sys
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel, QPushButton, QLineEdit,QMessageBox,QCheckBox)
from PyQt5.QtGui import QPixmap #=> To work with icons
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Registration import AddUserWindow
# our login gui
class LogInGUI(QWidget):
    PRIMARY_COLOR = "#E48700"
    SECONDARY_COLOR = "#4285F4"
    BORDER_COLOR = "#E48700"
    
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    def initialize_ui(self):
        """
        initialize neccesary widget in the screen.
        """
        self.setGeometry(0, 0, 539, 741)
        self.setFixedSize(539, 741)
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
        owner_projet_lbl.setStyleSheet(f'color:{LogInGUI.PRIMARY_COLOR}')
                
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
        self.user_or_email_entry.setStyleSheet(f"padding:10px 20px;border-radius:4px;background-color:#FFFFFF;border: 1px solid {LogInGUI.BORDER_COLOR}")
        self.user_or_email_entry.setPlaceholderText("Username or email address")
        
        # -------- Password field:
        password_lbl = QLabel('Enter your password',self)
        password_lbl.setFont(QFont("Tahoma",10))
        password_lbl.move(44, 438)
        
        self.password_entry = QLineEdit(self)
        self.password_entry.resize(451,57)
        self.password_entry.move(44, 475)
        self.password_entry.setFont(QFont("Tahoma",12))
        self.password_entry.setStyleSheet(f"padding:10px 20px;border-radius:4px;background-color:#FFFFFF;border: 1px solid {LogInGUI.BORDER_COLOR}")
        self.password_entry.setPlaceholderText("Password")
        
        # ------- CheckBox for showing the password:
        show_password_cb = QCheckBox("Show the password",self)
        show_password_cb.move(44, 544)
        show_password_cb.stateChanged.connect(self.show_password)
        show_password_cb.toggle()
        show_password_cb.setChecked(False)
        
        # ------ Forget password: btn
        forget_btn = QPushButton("forget PASSWORD",self)
        forget_btn.setFont(QFont("Tahoma",9))
        forget_btn.move(370, 544)
        forget_btn.setStyleSheet(f"background-color:transparent;color:{LogInGUI.SECONDARY_COLOR}")
        
        # Sign in button
        signin_btn = QPushButton("Sign in",self)
        signin_btn.setFont(QFont("Tahoma",10))
        signin_btn.move(259, 608)
        signin_btn.resize(236, 54)
        signin_btn.setStyleSheet(f"background-color:{LogInGUI.PRIMARY_COLOR};color:#fff;border-radius:4px")
        signin_btn.clicked.connect(self.login)
        # No account create one 
        no_account_lbl = QLabel("No Account ?",self)
        no_account_lbl.move(410, 50)
        no_account_lbl.setFont(QFont("Tahoma",9))
        # Create account btn
        signup_btn = QPushButton("Sign up",self)
        signup_btn.move(410, 70)
        signup_btn.setFont(QFont("Tahoma",9))
        signup_btn.setStyleSheet(f"background-color:transparent;color:{LogInGUI.PRIMARY_COLOR}")
        signup_btn.clicked.connect(self.create_account)
        # Change Close Event behavoir
    def closeEvent(self, event):
        sure_to_close = QMessageBox.question(self,"Sure to Close","Are you sure you need to close the program",QMessageBox.Cancel,QMessageBox.Yes)
        if sure_to_close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def show_password(self,state):
        if state == Qt.Checked:
            self.password_entry.setEchoMode(QLineEdit.Normal)
        else:
            self.password_entry.setEchoMode(QLineEdit.Password)
    
    def login(self):
        if(self.user_or_email_entry.text() !="" and self.password_entry.text() !="" ):
            usersbyusername = {}
            usersbyemail = {}
            try:
                with open("data/users.txt") as f:
                    for line in f:
                        data = line.split(" | ")
                        username = data[0]
                        password = data[1]
                        email = data[2].strip("\n")
                        usersbyusername[username] = password
                        usersbyemail[email] = password
                    
                if (self.user_or_email_entry.text() , self.password_entry.text()) in usersbyusername.items():
                    print("You login using username.")
                    QMessageBox.information(self,"Successful login by [Username]","You login with success. ",QMessageBox.Ok)
                elif (self.user_or_email_entry.text() , self.password_entry.text()) in usersbyemail.items():
                    print("You login using email.")
                    QMessageBox.information(self,"Successful login by [Email]","You login with success. ",QMessageBox.Ok)
                else:
                    print("Username or email or password is incorrect")
                    QMessageBox.warning(self,"Error login ","Check [Username/Email] or password. ",QMessageBox.Ok)
                    
            except FileNotFoundError:
                print("File Data not found. So we creating one.")
                open('data/users.txt',"w")                               
        else:
            QMessageBox.warning(self,"Empty Error","All field are required!",QMessageBox.Ok)
    def create_account(self):
        """
        This method popup new window to allow the to create new user.
        """
        self.add_user = AddUserWindow()              
        
            

# execution code for this gui
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myGui = LogInGUI()
    sys.exit(app.exec_())