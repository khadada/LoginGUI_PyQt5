# Importing necessary modules
import sys
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel, QPushButton, QLineEdit,QMessageBox,QCheckBox)
from PyQt5.QtGui import QPixmap #=> To work with icons
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# -------- addUser class

class AddUserWindow(QWidget):
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
        self.setWindowTitle("Sign Up v 1.0")
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
        owner_projet_lbl.setStyleSheet(f'color:{AddUserWindow.PRIMARY_COLOR}')
        
        signin_lbl = QLabel('Sign Up',self)
        signin_lbl.setFont(QFont("Tahoma",50))
        signin_lbl.move(44, 77)
        
        
        
        have_account_lbl = QLabel("Have an Account ?",self)
        have_account_lbl.move(410, 50)
        have_account_lbl.setFont(QFont("Tahoma",9))
        
        signin_btn = QPushButton("Sign in",self)
        signin_btn.move(410, 70)
        signin_btn.setFont(QFont("Tahoma",9))
        signin_btn.setStyleSheet(f"background-color:transparent;color:{AddUserWindow.PRIMARY_COLOR}")
        signin_btn.clicked.connect(self.back_to_signin)
        
        # -------- Username or Email field
        email_lbl = QLabel('Enter your email address',self)
        email_lbl.setFont(QFont("Tahoma",10))
        email_lbl.move(44, 203)
        
        self.email_entry = QLineEdit(self)
        self.email_entry.resize(451,57)
        self.email_entry.move(44, 240)
        self.email_entry.setFont(QFont("Tahoma",12))
        self.email_entry.setStyleSheet(f"padding:10px 20px;border-radius:4px;background-color:#FFFFFF;border: 1px solid {AddUserWindow.BORDER_COLOR}")
        self.email_entry.setPlaceholderText("Enter email address")
        
        # username label
        username = QLabel("User name:",self)
        username.move(44,332)
        username.setFont(QFont("Tahoma", 10))
        #username QlineEdit
        self.username_entry = QLineEdit(self)
        self.username_entry.resize(216, 57)
        self.username_entry.move(44, 361)
        self.username_entry.setFont(QFont("Tahoma",12))
        self.username_entry.setPlaceholderText("Username")
        self.username_entry.setStyleSheet(f"padding:10px 20px;border-radius:4px;background-color:#FFFFFF;border: 1px solid {AddUserWindow.BORDER_COLOR}")
        
        
        # contact label
        contact = QLabel("Contact Number:",self)
        contact.move(279,332)
        contact.setFont(QFont("Tahoma", 10))
        #username QlineEdit
        self.contact_num = QLineEdit(self)
        self.contact_num.resize(216, 57)
        self.contact_num.move(279, 361)
        self.contact_num.setFont(QFont("Tahoma",12))
        self.contact_num.setPlaceholderText("+213780360303")
        self.contact_num.setStyleSheet(f"padding:10px 20px;border-radius:4px;background-color:#FFFFFF;border: 1px solid {AddUserWindow.BORDER_COLOR}")

        
        # -------- Password field
        password_lbl = QLabel('Enter your Password',self)
        password_lbl.setFont(QFont("Tahoma",10))
        password_lbl.move(44, 451)
        
        self.password = QLineEdit(self)
        self.password.resize(451,57)
        self.password.move(44, 488)
        self.password.setFont(QFont("Tahoma",12))
        self.password.setStyleSheet(f"padding:10px 20px;border-radius:4px;background-color:#FFFFFF;border: 1px solid {AddUserWindow.BORDER_COLOR}")
        self.password.setPlaceholderText("Enter Your Password")
        
        # Create account btn
        signin_btn = QPushButton("Sign Up",self)
        signin_btn.setFont(QFont("Tahoma",10))
        signin_btn.move(259, 608)
        signin_btn.resize(236, 54)
        signin_btn.setStyleSheet(f"background-color:{AddUserWindow.PRIMARY_COLOR};color:#fff;border-radius:4px")
        signin_btn.clicked.connect(self.creat_user_account)
    def back_to_signin(self):
        """
        Close the signup window to back to sigin window
        """
        self.close()
    def closeEvent(self, event):
        """
        Confirm that the user need to close the program.
        """
        sure_to_close = QMessageBox.question(self,"Sure to Close","Are you sure you need to close signup window",QMessageBox.Cancel,QMessageBox.Yes)
        if sure_to_close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
        
    def creat_user_account(self):
        """
        This method check if user.txt file is found add the user to it. Otherwise create one.
        """
        # Check for the users.txt file
        if (self.contact_num.text()!="" and self.username_entry.text()!="" and self.email_entry.text()!="" and self.password.text()!=""):
            users_with_name = {}
            users_with_email = {}
            line_txt = ''
            try:
                with open('data/users.txt','r+') as f:
                    for line in f:
                        field_info = line.split(" | ")
                        username = field_info[0]
                        email = field_info[1]
                        password = field_info[2].strip("\n")
                        users_with_name[username] = password
                        users_with_email[email] = password
                    # Check If the username email are exist 
                    if(self.username_entry.text() in users_with_name.keys()):
                        go_to_login = QMessageBox.information(self,"The User Exist",f"This {self.username_entry.text()} exist in database.\nTry to login",QMessageBox.Yes,QMessageBox.Cancel)
                        if go_to_login == QMessageBox.Yes:
                            print("Now you will back to login window")
                    elif (self.email_entry.text() in users_with_email.keys()):
                        go_to_login = QMessageBox.information(self,"The Email Exist",f"This {self.email_entry.text()} exist in database.\nTry to login",QMessageBox.Yes,QMessageBox.Cancel)
                        if go_to_login == QMessageBox.Yes:
                            print("Now you will back to login window")
                    else:
                        line_txt = f"{self.username_entry.text()} | {self.email_entry.text()} | {self.password.text()}\n"
                        f.write(line_txt)
            except FileNotFoundError:
                print("The file is not found. Creating file [users.txt]")
                f = open('data/users.txt',"w")
                field = f"username | email | password:\n{line_txt}"
                f.write(field)
        else:
            QMessageBox.warning(self,"Empty Field Error","All field are required!",QMessageBox.Ok)
            