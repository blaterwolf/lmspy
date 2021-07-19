from PyQt6 import QtCore, QtGui, QtWidgets
from look_password import PasswordEdit
from validation import Ui_Validation
from main_menu import Ui_MainMenu
import sqlite3


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(480, 507)
        Login.setMaximumSize(QtCore.QSize(480, 528))
        Login.setMouseTracking(False)
        Login.setStyleSheet(
            ".QWidget{background-color:  #CBB1A0;border-radius: 10px}")
        Login.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Login)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.border = QtWidgets.QFrame(Login)
        self.border.setStyleSheet("#border{\n"
                                  "    color: #842a2d;\n"
                                  "}")
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setLineWidth(5)
        self.border.setMidLineWidth(5)
        self.border.setObjectName("border")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.border)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.border)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            398, 22, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.close_button = QtWidgets.QPushButton(self.widget)
        self.close_button.setEnabled(True)
        self.close_button.setMinimumSize(QtCore.QSize(35, 25))
        self.close_button.setMaximumSize(QtCore.QSize(35, 25))
        self.close_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.close_button.setStyleSheet("color: white;\n"
                                        "background-color: #82262C;\n"
                                        "font: 12pt \"Arial\" bold;\n"
                                        "border-radius: 5px;\n"
                                        "")
        self.close_button.setFlat(True)
        self.close_button.setObjectName("close_button")
        self.close_button.clicked.connect(sys.exit)
        self.gridLayout_3.addWidget(self.close_button, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.book_image = QtWidgets.QLabel(self.widget)
        self.book_image.setStyleSheet("")
        self.book_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.book_image.setObjectName("book_image")
        self.gridLayout.addWidget(self.book_image, 2, 0, 1, 1)
        self.title_name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.title_name.setFont(font)
        self.title_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_name.setObjectName("title_name")
        self.gridLayout.addWidget(self.title_name, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input_username = QtWidgets.QLineEdit(self.widget)
        self.input_username.setMaxLength(15)
        self.input_username.setMinimumSize(QtCore.QSize(0, 40))
        self.input_username.setStyleSheet("QLineEdit {\n"
                                          "      color: #000000;\n"
                                          "      font: 15pt \"Verdana\";\n"
                                          "      border: None;\n"
                                          "      border-bottom-color: white;\n"
                                          "      border-radius: 10px;\n"
                                          "      padding: 0 8px;\n"
                                          "      background: #CBB1A0;\n"
                                          "      selection-background-color: darkgray;\n"
                                          "}")
        self.input_username.setObjectName("input_username")
        self.input_username.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.input_username, 0, 1, 1, 1)
        self.login_button = QtWidgets.QPushButton(self.widget)
        self.login_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_button.setAutoFillBackground(False)
        self.login_button.setStyleSheet("QPushButton{\n"
                                        "    color: #842a2d;\n"
                                        "    font: 17pt \"Franklin Gothic Book\";\n"
                                        "    border: 2px solid #842a2d;\n"
                                        "    padding: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    opacity: 100;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: #842a2d;\n"
                                        "    color: #CBB1A0;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: #b34044;\n"
                                        "    border: 5px solid #b34044;\n"
                                        "}")
        self.login_button.setAutoDefault(False)
        self.login_button.setDefault(False)
        self.login_button.setFlat(False)
        self.login_button.setObjectName("login_button")
        self.gridLayout_2.addWidget(self.login_button, 6, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setStyleSheet("border: 2px solid #842a2d;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setStyleSheet("border: 2px solid #842a2d;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signup_button = QtWidgets.QPushButton(self.widget)
        self.signup_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.signup_button.sizePolicy().hasHeightForWidth())
        self.signup_button.setSizePolicy(sizePolicy)
        self.signup_button.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        self.signup_button.setFont(font)
        self.signup_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.signup_button.setAutoFillBackground(False)
        self.signup_button.setStyleSheet("QPushButton{\n"
                                         "    color: #842a2d;\n"
                                         "    font: 17pt \"Franklin Gothic Book\";\n"
                                         "    border: 2px solid #842a2d;\n"
                                         "    padding: 2px;\n"
                                         "    border-radius: 10px;\n"
                                         "    opacity: 100;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: #842a2d;\n"
                                         "    color: #CBB1A0;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: #b34044;\n"
                                         "    border: 5px solid #b34044;\n"
                                         "}")
        self.signup_button.setAutoDefault(False)
        self.signup_button.setDefault(False)
        self.signup_button.setFlat(False)
        self.signup_button.setObjectName("signup_button")
        self.horizontalLayout.addWidget(self.signup_button)
        self.forgot_password = QtWidgets.QPushButton(self.widget)
        self.forgot_password.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.forgot_password.sizePolicy().hasHeightForWidth())
        self.forgot_password.setSizePolicy(sizePolicy)
        self.forgot_password.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        self.forgot_password.setFont(font)
        self.forgot_password.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.forgot_password.setAutoFillBackground(False)
        self.forgot_password.setStyleSheet("QPushButton{\n"
                                           "    color: #842a2d;\n"
                                           "    font: 17pt \"Franklin Gothic Book\";\n"
                                           "    border: 2px solid #842a2d;\n"
                                           "    padding: 2px;\n"
                                           "    border-radius: 10px;\n"
                                           "    opacity: 100;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "    background-color: #842a2d;\n"
                                           "    color: #CBB1A0;\n"
                                           "}\n"
                                           "QPushButton:pressed{\n"
                                           "    background-color: #b34044;\n"
                                           "    border: 5px solid #b34044;\n"
                                           "}")
        self.forgot_password.setAutoDefault(False)
        self.forgot_password.setDefault(False)
        self.forgot_password.setFlat(False)
        self.forgot_password.setObjectName("forgot_password")
        self.horizontalLayout.addWidget(self.forgot_password)
        self.gridLayout_2.addLayout(self.horizontalLayout, 7, 0, 1, 2)
        self.status_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("padding: 10px 0px;\n"
                                        "color: red;")
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.gridLayout_2.addWidget(self.status_label, 4, 0, 1, 2)
        self.password_image = QtWidgets.QLabel(self.widget)
        self.password_image.setStyleSheet("")
        self.password_image.setObjectName("password_image")
        self.gridLayout_2.addWidget(self.password_image, 2, 0, 1, 1)
        self.input_password = PasswordEdit(self.widget)
        self.input_password.setMinimumSize(QtCore.QSize(0, 40))
        self.input_password.setMaxLength(15)
        self.input_password.setStyleSheet("QLineEdit {\n"
                                          "      color: #000000;\n"
                                          "      font: 15pt \"Verdana\";\n"
                                          "      border: None;\n"
                                          "      border-bottom-color: white;\n"
                                          "      border-radius: 10px;\n"
                                          "      padding: 0 8px;\n"
                                          "      background: #CBB1A0;\n"
                                          "      selection-background-color: darkgray;\n"
                                          "}")
        self.input_password.setObjectName("input_password")
        self.input_password.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.input_password, 2, 1, 1, 1)
        self.username_image = QtWidgets.QLabel(self.widget)
        self.username_image.setStyleSheet("")
        self.username_image.setObjectName("username_image")
        self.gridLayout_2.addWidget(self.username_image, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 2)
        self.horizontalLayout_3.addWidget(self.widget)
        self.verticalLayout_3.addWidget(self.border)
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        # * These are the functions:
        # * self.<name>_button is the variable for our buttons.
        self.login_button.clicked.connect(self.attempt_login)
        self.signup_button.clicked.connect(self.run_signup)
        self.forgot_password.clicked.connect(self.run_forgot_password)

    def run_signup(self):
        # * Creates an instance of the object Validation wherein this is the
        # * window to run our validation.py
        self.Validation = QtWidgets.QWidget()
        self.ui_validate = Ui_Validation()
        # * self.Validation - instance of QWidget to run our validation window.
        # * Login -> component of Login window.
        # * use_form -> variable to determine where to go later on add or edit librarian.
        self.ui_validate.setupUi(self.Validation, Login, use_form="add")
        self.reset_input()
        self.Validation.show()

    def run_forgot_password(self):
        # * Creates an instance of the object Validation wherein this is the
        # * window to run our validation.py
        self.Validation = QtWidgets.QWidget()
        self.ui_validate = Ui_Validation()
        # * self.Validation - instance of QWidget to run our validation window.
        # * Login -> component of Login window.
        # * use_form -> variable to determine where to go later on add or edit librarian.
        self.ui_validate.setupUi(self.Validation, Login, use_form="edit")
        self.reset_input()
        self.Validation.show()

    def attempt_login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        compare_data = (username, password)
        con = sqlite3.connect('./db/library.db')
        query = "SELECT Librarian_Username, Librarian_Password FROM LIBRARIAN;"
        result = [form[1] for form in list(enumerate(con.execute(query)))]
        if (len(username) == 0 or len(password) == 0):
            self.status_label.setText("Input field/s are empty!")
        elif compare_data in result:
            self.run_main_menu(Login, username)
        else:
            self.status_label.setText("Your username or password is invalid!")

    def informative_message(self, text, subtext, window_title):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(text)
        msg.setInformativeText(subtext)
        msg.setWindowTitle(window_title)
        msg.exec()

    def run_main_menu(self, Login, username):
        self.informative_message(
            text="You are logged in!",
            subtext="You will be redirected to the main menu...",
            window_title="Login Successful"
        )
        self.MainMenu = QtWidgets.QWidget()
        self.ui_menu = Ui_MainMenu()
        self.ui_menu.setupUi(self.MainMenu, Login, username)
        self.MainMenu.show()
        self.reset_input()
        Login.close()

    def reset_input(self):
        self.input_username.setText("")
        self.input_password.setText("")
        self.status_label.setText("")

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.close_button.setText(_translate("Login", "✖"))
        self.book_image.setText(_translate(
            "Login", "<html><head/><body><p><img src=\"./icons/library_100x100.png\"/></p></body></html>"))
        self.title_name.setText(_translate(
            "Login", "SCHOOL LIBRARY MANAGEMENT SYSTEM"))
        self.password_image.setText(_translate(
            "Login", "<html><head/><body><p><img src=\"./icons/lock_32x32.png\"/></p></body></html>"))
        self.username_image.setText(_translate(
            "Login", "<html><head/><body><p><img src=\"./icons/user_32x32.png\"/></p></body></html>"))
        self.login_button.setText(_translate("Login", "LOG IN"))
        self.signup_button.setText(_translate("Login", "SIGN UP"))
        self.forgot_password.setText(_translate("Login", "FORGOT PASSWORD"))


# * Why this code is only present in the login.py?
# * Because the login.py is the center of opening our Application.
# * So, login.py is responsible for opening the validation.py and
# * the main_menu.py which holds the other functions to open
# * other windows.
if __name__ == "__main__":
    import sys
    # * Creating an instance of QApplication to use the QWidgets app.
    app = QtWidgets.QApplication(sys.argv)
    # * Create a QWidget Class
    # * The QWidget Class helps us to create a QWidget Application
    Login = QtWidgets.QWidget()
    # * We need to store the Ui_Login() class into a variable named ui.
    ui = Ui_Login()
    # * Run the setupui() function where setupUi() is responsible for
    # * creating the components for our application.
    ui.setupUi(Login)
    # * Login.show() is the code in order to show the application to the user.
    Login.show()
    # * if the user has exited the application (clicked the button)
    # * the sys.exit(app.exec()) will destroy the program.
    sys.exit(app.exec())
