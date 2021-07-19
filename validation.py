from PyQt6 import QtCore, QtGui, QtWidgets
from add_librarian import Ui_AddLibrarian
from edit_librarian import Ui_EditLibrarian
import pyotp
import qrcode
import os


class Ui_Validation(object):
    def setupUi(self, Validation, Login, use_form):
        Login.close()
        self.current_base32 = pyotp.random_base32()
        self.generate_random_qr(self.current_base32)
        Validation.setObjectName("Validation")
        Validation.resize(459, 567)
        Validation.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        Validation.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Validation)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.border = QtWidgets.QFrame(Validation)
        self.border.setStyleSheet("#border{\n"
                                  "    color: #842a2d;\n"
                                  "}")
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setLineWidth(5)
        self.border.setMidLineWidth(5)
        self.border.setObjectName("border")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.border)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.border)
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_6 = QtWidgets.QLabel(self.border)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.input_otp = QtWidgets.QLineEdit(self.border)
        self.input_otp.setMinimumSize(QtCore.QSize(0, 30))
        self.input_otp.setStyleSheet("QLineEdit {\n"
                                     "      color: #000000;\n"
                                     "      font: 15pt \"Verdana\";\n"
                                     "      border: 1px;\n"
                                     "      padding: 0 8px;\n"
                                     "      background: #CBB1A0;\n"
                                     "}")
        self.input_otp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_otp.setObjectName("input_otp")
        self.verticalLayout.addWidget(self.input_otp)
        self.validate_button = QtWidgets.QPushButton(self.border)
        self.validate_button.setEnabled(True)
        self.validate_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.validate_button.setStyleSheet("QPushButton{\n"
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
        self.validate_button.setObjectName("validate_button")
        self.validate_button.clicked.connect(
            lambda: self.validate_otp(Validation, Login, form_to_run=use_form))
        self.verticalLayout.addWidget(self.validate_button)
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
            lambda: self.return_action(Validation, Login))
        self.verticalLayout.addWidget(self.cancel_button)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.border)
        self.retranslateUi(Validation)
        QtCore.QMetaObject.connectSlotsByName(Validation)

    def return_action(self, Validation, Login):
        os.remove("./icons/qr.png")
        Validation.close()
        Login.show()

    def generate_random_qr(self, base32):
        totp = pyotp.TOTP(base32)
        data = totp.provisioning_uri(
            name='lmspy', issuer_name='LSMPY Validation')
        qr = qrcode.QRCode(
            version=1,
            box_size=3,
            border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('./icons/qr.png')

    def validate_otp(self, Validation, Login, form_to_run):
        answer = self.input_otp.text()
        totp = pyotp.TOTP(self.current_base32)
        msg = QtWidgets.QMessageBox()
        if answer == totp.now():
            self.informative_message(
                text="That is the correct OTP!",
                subtext="You'll be redirected now to the next Window...",
                window_title="Validated Successfully!",
                icon_type="information"
            )
            if form_to_run == "add":
                self.run_add_librarian(Validation, Login)
            elif form_to_run == "edit":
                self.run_edit_librarian(Validation, Login)
            os.remove("./icons/qr.png")
        else:
            self.informative_message(
                text="The OTP is incorrect.",
                subtext="You have typed the incorrect OTP. If this problem kept happening, press cancel button and try again.",
                window_title="Incorrect Validation!",
            )

    def informative_message(self, text, subtext, window_title, icon_type="critical"):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        if icon_type == "information":
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(text)
        msg.setInformativeText(subtext)
        msg.setWindowTitle(window_title)
        msg.exec()

    def run_add_librarian(self, Validation, Login):
        self.AddLibrarian = QtWidgets.QWidget()
        self.ui_addlibrarian = Ui_AddLibrarian()
        self.ui_addlibrarian.setupUi(self.AddLibrarian, Login)
        self.AddLibrarian.show()
        Validation.close()

    def run_edit_librarian(self, Validation, Login):
        self.EditLibrarian = QtWidgets.QWidget()
        self.ui_editlibrarian = Ui_EditLibrarian()
        self.ui_editlibrarian.setupUi(self.EditLibrarian, Login)
        self.EditLibrarian.show()
        Validation.close()

    def retranslateUi(self, Validation):
        _translate = QtCore.QCoreApplication.translate
        Validation.setWindowTitle(_translate("Validation", "Validation OTP"))
        self.label_4.setText(_translate(
            "Validation", "<html><head/><body><p><img src=\"./icons/googleauth_100x100.png\"/></p></body></html>"))
        self.label_5.setText(_translate(
            "Validation", "GOOGLE AUTHENTICATOR VALIDATION"))
        self.label_3.setText(_translate("Validation", "1. Download the Google Authenticator App\n"
                                        "2. Press the + button on Google Authenticator then click \"Scan QRCode\"\n"
                                        "3. Follow the instructions for taking picture of the Randomly Generated QrCode.\n"
                                        "4. Enter the current OTP on your phone to the input field below."))
        self.label_2.setText(_translate("Validation", "QR Code:"))
        self.label_6.setText(_translate(
            "Validation", "<html><head/><body><p><img src=\"./icons/qr.png\"/></p></body></html>"))
        self.label.setText(_translate("Validation", "Enter Current OTP:"))
        self.validate_button.setText(_translate("Validation", "Validate"))
        self.cancel_button.setText(_translate("Validation", "Cancel"))
