from PyQt6 import QtCore, QtGui, QtWidgets
import datetime
import sqlite3


class Ui_ReturnRequest(object):
    def setupUi(self, ReturnRequest, MainMenu, Ui_CurrentlyBorrowedBooks, current_username):
        MainMenu.close()
        ReturnRequest.setObjectName("ReturnRequest")
        ReturnRequest.resize(529, 331)
        ReturnRequest.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        ReturnRequest.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(ReturnRequest)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.border = QtWidgets.QFrame(ReturnRequest)
        self.border.setStyleSheet("#border{\n"
                                  "    color: #842a2d;\n"
                                  "}")
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setLineWidth(5)
        self.border.setMidLineWidth(5)
        self.border.setObjectName("border")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.border)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.borrow_book_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.borrow_book_label.setFont(font)
        self.borrow_book_label.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        self.borrow_book_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.borrow_book_label.setObjectName("borrow_book_label")
        self.verticalLayout_4.addWidget(self.borrow_book_label)
        spacerItem = QtWidgets.QSpacerItem(
            10, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_1 = QtWidgets.QFrame(self.border)
        self.line_1.setStyleSheet("border: 2px solid #842a2d;")
        self.line_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_1.setObjectName("line_1")
        self.verticalLayout_2.addWidget(self.line_1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_borrow_id = QtWidgets.QLineEdit(self.border)
        self.input_borrow_id.setStyleSheet("QLineEdit {\n"
                                           "      color: #000000;\n"
                                           "      font: 15pt \"Verdana\";\n"
                                           "      border: None;\n"
                                           "      border-bottom-color: white;\n"
                                           "      border-radius: 10px;\n"
                                           "      padding: 0 8px;\n"
                                           "      background: #CBB1A0;\n"
                                           "      selection-background-color: darkgray;\n"
                                           "}")
        self.input_borrow_id.setObjectName("input_borrow_id")
        self.input_borrow_id.setText("BORROW-")
        self.verticalLayout.addWidget(self.input_borrow_id)
        self.line_3 = QtWidgets.QFrame(self.border)
        self.line_3.setStyleSheet("border: 2px solid #842a2d;")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 2, 1)
        self.borrow_id_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.borrow_id_label.setFont(font)
        self.borrow_id_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                          QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.borrow_id_label.setObjectName("borrow_id_label")
        self.gridLayout.addWidget(self.borrow_id_label, 0, 0, 2, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(self.border)
        self.line_2.setStyleSheet("border: 2px solid #842a2d;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.status_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.verticalLayout_3.addWidget(self.status_label)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.return_button = QtWidgets.QPushButton(self.border)
        self.return_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.return_button.setStyleSheet("QPushButton{\n"
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
                                         "}")
        self.return_button.setObjectName("return_button")
        self.return_button.clicked.connect(
            lambda: self.validate_return_books(ReturnRequest, current_username))
        self.verticalLayout_3.addWidget(self.return_button)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.view_borrowed_books_button = QtWidgets.QPushButton(self.border)
        self.view_borrowed_books_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.view_borrowed_books_button.setStyleSheet("QPushButton{\n"
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
                                                      "}")
        self.view_borrowed_books_button.setObjectName(
            "view_borrowed_books_button")
        self.view_borrowed_books_button.clicked.connect(
            lambda: self.run_borrowed_books(Ui_CurrentlyBorrowedBooks, ReturnRequest))
        self.horizontalLayout_3.addWidget(self.view_borrowed_books_button)
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
                                         "}")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(
            lambda: self.return_action(ReturnRequest, MainMenu))
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.border)

        self.retranslateUi(ReturnRequest)
        QtCore.QMetaObject.connectSlotsByName(ReturnRequest)

    def return_action(self, ReturnRequest, MainMenu):
        ReturnRequest.close()
        MainMenu.show()

    def run_borrowed_books(self, Ui_CurrentlyBorrowedBooks, ReturnRequest):
        ReturnRequest.close()
        self.CurrentlyBorrowedBooks = QtWidgets.QWidget()
        self.ui_currently_borrowed_books = Ui_CurrentlyBorrowedBooks()
        self.ui_currently_borrowed_books.setupUi(
            self.CurrentlyBorrowedBooks, current_class=ReturnRequest)
        self.CurrentlyBorrowedBooks.show()

    def validate_return_books(self, ReturnRequest, current_username):
        borrow_id = self.input_borrow_id.text()
        # * initialize sqlite
        con = sqlite3.connect('./db/test.db')
        cur = con.cursor()
        # * check if borrow_id exists
        check_id_query = "SELECT Borrow_ID FROM BORROW;"
        result_borrow = [form[1][0] for form in list(
            enumerate(con.execute(check_id_query)))]
        if borrow_id in result_borrow:
            # * query the payment_id and book_id
            self.status_label.setText("")
            borrow_query = "SELECT Borrow_Date, Payment_ID, Book_ID FROM BORROW WHERE Borrow_ID = ?;"
            interpolate_data = [borrow_id]
            result = cur.execute(borrow_query, interpolate_data)
            borrow_data = [form[1] for form in list(enumerate(result))][0]
            self.execute_returning_books(
                borrow_date=borrow_data[0],
                payment_id=borrow_data[1],
                book_id=borrow_data[2],
                borrow_id=borrow_id,
                current_username=current_username
            )
            self.input_borrow_id.setText("BORROW-")
        else:
            self.status_label.setText("Borrow ID is invalid!")

    def execute_returning_books(self, borrow_date, payment_id, book_id, borrow_id, current_username):
        # * Step 1: Initialize Database
        borrow_date = datetime.datetime.strptime(
            borrow_date, '%Y-%m-%d %H:%M:%S.%f')
        borrow_return_date = datetime.datetime.now()
        borrow_status = "Returned"
        penalty_amount = self.compute_amount(borrow_date, borrow_return_date)
        book_status = 'Available'
        payment_status = 'Paid'
        payment_issuer = current_username

        # * Step 1.5: Initialize Database
        con = sqlite3.connect('./db/test.db')
        cur = con.cursor()

        # * Step 2: UPDATE PAYMENT data: Compute Amount, Status, and Issuer
        payment_query = """UPDATE PAYMENT
                        SET Payment_Amount = ?, Payment_Status = ?, Payment_Issuer = ?
                        WHERE Payment_ID = ?;
        """
        interpolate_data = [penalty_amount,
                            payment_status, payment_issuer, payment_id]
        cur.execute(payment_query, interpolate_data)
        # * Step 3: UPDATE BOOK Book_Status to Available
        book_query = """UPDATE BOOK
                        SET Book_Status = ?
                        WHERE Book_ID = ?;
        """
        interpolate_data = [book_status, book_id]
        cur.execute(book_query, interpolate_data)
        # * Step 4: UPDATE BORROW Borrow_Return_Date to datetime.now()
        borrow_query = """UPDATE BORROW
                        SET Borrow_Return_Date = ?, Borrow_Status = ?
                        WHERE Borrow_ID = ?;
        """
        interpolate_data = [borrow_return_date, borrow_status, borrow_id]
        cur.execute(borrow_query, interpolate_data)
        con.commit()
        con.close()
        # ! query the updated borrow id here
        self.informative_message(
            text="You Returned Successfully!",
            subtext=f"You successfully returned {borrow_id}",
            window_title="Returned Successfully",
            icon_type="information"
        )

    def compute_amount(self, borrow_date, borrow_return_date):
        penalty = 0.0
        days_passed = (borrow_return_date-borrow_date).days
        while days_passed >= 7:
            if days_passed == 7:
                penalty += 100.00
                days_passed = 0
            else:
                penalty += (0.05 * 100.00)
                days_passed -= 1
        return penalty

    def informative_message(self, text, subtext, window_title, icon_type="critical"):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        if icon_type == "information":
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(text)
        msg.setInformativeText(subtext)
        msg.setWindowTitle(window_title)
        msg.exec()

    def retranslateUi(self, ReturnRequest):
        _translate = QtCore.QCoreApplication.translate
        ReturnRequest.setWindowTitle(_translate("ReturnRequest", "Form"))
        self.borrow_book_label.setText(
            _translate("ReturnRequest", "RETURN A BOOK"))
        self.borrow_id_label.setText(_translate("ReturnRequest", "Borrow ID:"))
        self.return_button.setText(_translate("ReturnRequest", "RETURN"))
        self.view_borrowed_books_button.setText(
            _translate("ReturnRequest", "  VIEW BORROWED BOOKS  "))
        self.cancel_button.setText(_translate("ReturnRequest", "CANCEL"))
