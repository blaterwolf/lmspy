from PyQt6 import QtCore, QtGui, QtWidgets
from look_password import PasswordEdit
import sqlite3


class Ui_EditLibrarian(object):
    def setupUi(self, EditLibrarian, Login):
        EditLibrarian.setObjectName("EditLibrarian")
        EditLibrarian.resize(518, 516)
        EditLibrarian.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        EditLibrarian.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EditLibrarian)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.border = QtWidgets.QFrame(EditLibrarian)
        self.border.setStyleSheet("#border{\n"
                                  "    color: #842a2d;\n"
                                  "}")
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setLineWidth(5)
        self.border.setMidLineWidth(5)
        self.border.setObjectName("border")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.border)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_title = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_4.addWidget(self.label_title)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_8 = QtWidgets.QFrame(self.border)
        self.line_8.setStyleSheet("border: 2px solid #842a2d;")
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_3.addWidget(self.line_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name_2 = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name_2.setFont(font)
        self.label_name_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                       QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_name_2.setObjectName("label_name_2")
        self.horizontalLayout.addWidget(self.label_name_2)
        self.input_search_username = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.input_search_username.setFont(font)
        self.input_search_username.setStyleSheet("QLineEdit {\n"
                                                 "      color: #000000;\n"
                                                 "      font: 15pt \"Verdana\";\n"
                                                 "      border: None;\n"
                                                 "      border-bottom-color: white;\n"
                                                 "      border-radius: 10px;\n"
                                                 "      padding: 0 8px;\n"
                                                 "      background: #CBB1A0;\n"
                                                 "      selection-background-color: darkgray;\n"
                                                 "}")
        self.input_search_username.setMaxLength(15)
        self.input_search_username.setClearButtonEnabled(True)
        self.input_search_username.setObjectName("input_search_username")
        self.horizontalLayout.addWidget(self.input_search_username)
        self.search_username_button = QtWidgets.QPushButton(self.border)
        self.search_username_button.setEnabled(True)
        self.search_username_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.search_username_button.setStyleSheet("QPushButton{\n"
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
        self.search_username_button.setObjectName("search_username_button")
        self.search_username_button.clicked.connect(self.search_for_username)
        self.horizontalLayout.addWidget(self.search_username_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line_9 = QtWidgets.QFrame(self.border)
        self.line_9.setStyleSheet("border: 2px solid #842a2d;")
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_3.addWidget(self.line_9)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(
            17, 19, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                     QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 1, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.border)
        self.line_5.setStyleSheet("border: 2px solid #842a2d;")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 6, 0, 1, 2)
        self.input_password = PasswordEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.input_password.setFont(font)
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
        self.input_password.setText("")
        self.input_password.setMaxLength(15)
        self.input_password.setClearButtonEnabled(True)
        self.input_password.setObjectName("input_password")
        self.gridLayout.addWidget(self.input_password, 5, 1, 1, 1)
        self.input_password_confirm = PasswordEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.input_password_confirm.setFont(font)
        self.input_password_confirm.setStyleSheet("QLineEdit {\n"
                                                  "      color: #000000;\n"
                                                  "      font: 15pt \"Verdana\";\n"
                                                  "      border: None;\n"
                                                  "      border-bottom-color: white;\n"
                                                  "      border-radius: 10px;\n"
                                                  "      padding: 0 8px;\n"
                                                  "      background: #CBB1A0;\n"
                                                  "      selection-background-color: darkgray;\n"
                                                  "}")
        self.input_password_confirm.setText("")
        self.input_password_confirm.setMaxLength(15)
        self.input_password_confirm.setClearButtonEnabled(True)
        self.input_password_confirm.setObjectName("input_password_confirm")
        self.gridLayout.addWidget(self.input_password_confirm, 7, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.border)
        self.line_2.setStyleSheet("border: 2px solid #842a2d;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 2)
        self.label_username = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_username.setFont(font)
        self.label_username.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                         QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 3, 0, 1, 1)
        self.input_username = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.input_username.setFont(font)
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
        self.input_username.setMaxLength(15)
        self.input_username.setClearButtonEnabled(True)
        self.input_username.setObjectName("input_username")
        self.gridLayout.addWidget(self.input_username, 3, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.border)
        self.line_4.setStyleSheet("border: 2px solid #842a2d;")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 4, 0, 1, 2)
        self.label_pass = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_pass.setFont(font)
        self.label_pass.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                     QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_pass.setObjectName("label_pass")
        self.gridLayout.addWidget(self.label_pass, 5, 0, 1, 1)
        self.input_fullname = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.input_fullname.setFont(font)
        self.input_fullname.setStyleSheet("QLineEdit {\n"
                                          "      color: #000000;\n"
                                          "      font: 15pt \"Verdana\";\n"
                                          "      border: None;\n"
                                          "      border-bottom-color: white;\n"
                                          "      border-radius: 10px;\n"
                                          "      padding: 0 8px;\n"
                                          "      background: #CBB1A0;\n"
                                          "      selection-background-color: darkgray;\n"
                                          "}")
        self.input_fullname.setMaxLength(50)
        self.input_fullname.setClearButtonEnabled(True)
        self.input_fullname.setObjectName("input_fullname")
        self.gridLayout.addWidget(self.input_fullname, 1, 1, 1, 1)
        self.label_retype_pass = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_retype_pass.setFont(font)
        self.label_retype_pass.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_retype_pass.setObjectName("label_retype_pass")
        self.gridLayout.addWidget(self.label_retype_pass, 7, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.border)
        self.line_6.setStyleSheet("border: 2px solid #842a2d;")
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 8, 0, 1, 2)
        self.line_7 = QtWidgets.QFrame(self.border)
        self.line_7.setStyleSheet("border: 2px solid #842a2d;")
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 0, 0, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.edit_librarian = QtWidgets.QPushButton(self.border)
        self.edit_librarian.setEnabled(True)
        self.edit_librarian.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_librarian.setStyleSheet("QPushButton{\n"
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
        self.edit_librarian.setObjectName("edit_librarian")
        self.edit_librarian.clicked.connect(
            lambda: self.validate_names(EditLibrarian, Login))
        self.verticalLayout.addWidget(self.edit_librarian)
        self.cancel_button = QtWidgets.QPushButton(self.border)
        self.cancel_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.cancel_button.setStyleSheet("QPushButton{\n"
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
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(
            lambda: self.close_actions(EditLibrarian, Login))
        self.verticalLayout.addWidget(self.cancel_button)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.border)
        self.retranslateUi(EditLibrarian)
        QtCore.QMetaObject.connectSlotsByName(EditLibrarian)
        self.init_disabled_inputs()

    def close_actions(self, EditLibrarian, Login):
        EditLibrarian.close()
        Login.show()

    def search_for_username(self):
        username_to_search = self.input_search_username.text()
    # * query if that username exists in the database
        con = sqlite3.connect('./db/library.db')
        query = "SELECT Librarian_Username, Librarian_Name FROM LIBRARIAN;"
        result = [form[1] for form in list(enumerate(con.execute(query)))]
        usernames = [each_data[0] for each_data in result]
        if username_to_search in usernames:
            data_to_populate = [
                each_data for each_data in result if each_data[0] == username_to_search][0]
            self.enable_inputs()
            self.input_username.setDisabled(True)
            self.populate_data(
                username=data_to_populate[0], fullname=data_to_populate[1])
        else:
            self.informative_message(
                text="Username was not found in the database!",
                subtext="Check for typographical errors or data doesn't exist in the database at all.",
                window_title="Username Not Found"
            )

    def validate_names(self, EditLibrarian, Login):
        username_search = self.input_search_username.text()
        fullname = self.input_fullname.text()
        username = self.input_username.text()
        init_password = self.input_password.text()
        chck_password = self.input_password_confirm.text()

        if (len(fullname) == 0 or len(username) == 0 or len(init_password) == 0 or len(chck_password) == 0):
            self.label.setText("Input field/s are empty!")
        elif (init_password != chck_password):
            self.label.setText("Passwords do not match!")
        elif (len(init_password) < 8 or len(chck_password) < 8):
            self.label.setText("Passwords must be at least 8 characters!")
        else:
            self.label.setText("")
            self.update_data(fullname=fullname, username=username, password=init_password,
                             EditLibrarian=EditLibrarian, username_search=username_search, Login=Login)

    def update_data(self, fullname, username, password, EditLibrarian, username_search, Login):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(
            "You'll be updating the following information in the database: ")
        msg.setInformativeText(
            f"Name:\t\t{fullname}\nUsername:\t{username}\nPassword:\t{password}\n\nAre you sure?")
        msg.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        msg.setWindowTitle("Confirmation Check")
        result = msg.exec()
        if (result == QtWidgets.QMessageBox.StandardButton.Yes):
            # * Step 1: Connect to the database.
            con = sqlite3.connect('./db/library.db')
            cur = con.cursor()
            # * Step 2: Put the query inside the string.
            query = """
                UPDATE LIBRARIAN
                SET Librarian_Name = ?, Librarian_Password = ?
                WHERE Librarian_Username = ?;
            """
            # * Step 3: Put all the data to be interpolated inside a list.
            interpolate_data = [fullname, password, username]
            # * Step 4: Execute, Commit, Close
            cur.execute(query, interpolate_data)
            con.commit()
            con.close()
            self.informative_message(
                text="Data Updated Successfully!",
                subtext="You'll be redirected now to the Login Window...",
                window_title="Updated Successfully",
                icon_type="information"
            )
            self.close_actions(EditLibrarian, Login)
        elif (result == QtWidgets.QMessageBox.StandardButton.No):
            pass

    def informative_message(self, text, subtext, window_title, icon_type="critical"):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        if icon_type == "information":
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(text)
        msg.setInformativeText(subtext)
        msg.setWindowTitle(window_title)
        msg.exec()

    def init_disabled_inputs(self):
        # * setEnabled to False
        self.input_username.setEnabled(False)
        self.input_fullname.setEnabled(False)
        self.input_password.setEnabled(False)
        self.input_password_confirm.setEnabled(False)
        self.edit_librarian.setEnabled(False)

    def enable_inputs(self):
        # * setEnabled to True
        self.input_username.setEnabled(True)
        self.input_fullname.setEnabled(True)
        self.input_password.setEnabled(True)
        self.input_password_confirm.setEnabled(True)
        self.edit_librarian.setEnabled(True)

    def populate_data(self, username, fullname):
        self.input_username.setText(username)
        self.input_fullname.setText(fullname)

    def retranslateUi(self, EditLibrarian):
        _translate = QtCore.QCoreApplication.translate
        EditLibrarian.setWindowTitle(_translate(
            "EditLibrarian", "Sign Up Librarian"))
        self.label_title.setText(_translate(
            "EditLibrarian", "Change Librarian Information"))
        self.label_name_2.setText(_translate(
            "EditLibrarian", "Search Username:"))
        self.search_username_button.setText(
            _translate("EditLibrarian", "SEARCH"))
        self.label_name.setText(_translate("EditLibrarian", "Full Name:"))
        self.label_username.setText(_translate("EditLibrarian", "Username:"))
        self.label_pass.setText(_translate(
            "EditLibrarian", "Preferred Password:"))
        self.label_retype_pass.setText(
            _translate("EditLibrarian", "Retype Password:"))
        self.label.setText(_translate("EditLibrarian", ""))
        self.edit_librarian.setText(_translate(
            "EditLibrarian", "Edit Librarian"))
        self.cancel_button.setText(_translate("EditLibrarian", "Cancel"))
