from PyQt6 import QtCore, QtGui, QtWidgets
from book_information import Ui_BookInformation
from student_information import Ui_StudentInformation
from view_book_status import Ui_BookStatus
from return_request import Ui_ReturnRequest
from borrow_request import Ui_BorrowRequest
from currently_borrowed_books import Ui_CurrentlyBorrowedBooks
from currently_overdue_books import Ui_CurrentlyOverdueBooks
from search_history import Ui_SearchHistory
from quote_machine import quote_data
import sqlite3
import random
import datetime


class Ui_MainMenu(object):
    def setupUi(self, MainMenu, Login, username_to_show):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(804, 426)
        font = QtGui.QFont()
        MainMenu.setFont(font)
        MainMenu.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        MainMenu.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(MainMenu)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.border = QtWidgets.QFrame(MainMenu)
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.border.setLineWidth(5)
        self.border.setMidLineWidth(5)
        self.border.setObjectName("border")
        self.border.setStyleSheet("#border{\n	color: #842a2d;\n}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.border)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_name = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.title_name.setFont(font)
        self.title_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                     QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.title_name.setObjectName("title_name")
        self.horizontalLayout_2.addWidget(self.title_name)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userloggedin_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userloggedin_label.setFont(font)
        self.userloggedin_label.setObjectName("userloggedin_label")
        self.horizontalLayout.addWidget(self.userloggedin_label)
        self.call_username_to_input = QtWidgets.QLineEdit(self.border)
        self.call_username_to_input.setEnabled(False)
        self.call_username_to_input.setStyleSheet("QLineEdit {\n"
                                                  "      color: #000000;\n"
                                                  "      font: 11pt \"Verdana\";\n"
                                                  "      border: None;\n"
                                                  "      border-bottom-color: white;\n"
                                                  "      border-radius: 10px;\n"
                                                  "      padding: 0 8px;\n"
                                                  "      background: #CBB1A0;\n"
                                                  "      selection-background-color: darkgray;\n"
                                                  "}")
        self.call_username_to_input.setObjectName("call_username_to_input")
        current_user = self.get_name(username_to_show)
        self.call_username_to_input.setText(current_user)
        self.horizontalLayout.addWidget(self.call_username_to_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.border)
        self.line_2.setStyleSheet("border: 2px solid #842a2d;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.book_image = QtWidgets.QLabel(self.border)
        self.book_image.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(
            self.book_image.sizePolicy().hasHeightForWidth())
        self.book_image.setSizePolicy(sizePolicy)
        self.book_image.setMinimumSize(QtCore.QSize(0, 0))
        self.book_image.setMaximumSize(QtCore.QSize(386, 270))
        self.book_image.setObjectName("book_image")
        self.verticalLayout_2.addWidget(self.book_image)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.random_quotes_generator = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.random_quotes_generator.setFont(font)
        self.random_quotes_generator.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.random_quotes_generator.setObjectName("random_quotes_generator")
        self.verticalLayout_2.addWidget(self.random_quotes_generator)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 7, 0, 1, 1)
        self.overdue_button = QtWidgets.QPushButton(self.border)
        self.overdue_button.setStyleSheet("QPushButton{\n"
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
        self.overdue_button.setObjectName("overdue_button")
        self.overdue_button.clicked.connect(
            lambda: self.run_currently_overdue_books(MainMenu))
        self.gridLayout.addWidget(self.overdue_button, 5, 0, 1, 2)
        self.book_button = QtWidgets.QPushButton(self.border)
        self.book_button.setStyleSheet("QPushButton{\n"
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
        self.book_button.setObjectName("book_button")
        self.book_button.clicked.connect(
            lambda: self.run_book_information(MainMenu))
        self.gridLayout.addWidget(self.book_button, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.search_history_button = QtWidgets.QPushButton(self.border)
        self.search_history_button.setStyleSheet("QPushButton{\n"
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
        self.search_history_button.setObjectName("search_history_button")
        self.search_history_button.clicked.connect(
            lambda: self.run_search_history(MainMenu))
        self.gridLayout.addWidget(self.search_history_button, 6, 0, 1, 2)
        self.borrow_button = QtWidgets.QPushButton(self.border)
        self.borrow_button.setStyleSheet("QPushButton{\n"
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
        self.borrow_button.setObjectName("borrow_button")
        self.borrow_button.clicked.connect(
            lambda: self.run_borrow_request(MainMenu, username_to_show))
        self.gridLayout.addWidget(self.borrow_button, 1, 0, 1, 1)
        self.return_button = QtWidgets.QPushButton(self.border)
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
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: #b34044;\n"
                                         "    border: 5px solid #b34044;\n"
                                         "}")
        self.return_button.setObjectName("return_button")
        self.return_button.clicked.connect(
            lambda: self.run_return_request(MainMenu, username_to_show))
        self.gridLayout.addWidget(self.return_button, 1, 1, 1, 1)
        self.book_status_button = QtWidgets.QPushButton(self.border)
        self.book_status_button.setStyleSheet("QPushButton{\n"
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
        self.book_status_button.setObjectName("book_status_button")
        self.book_status_button.clicked.connect(
            lambda: self.run_book_status(MainMenu))
        self.gridLayout.addWidget(self.book_status_button, 3, 0, 1, 2)
        self.borrowed_books_button = QtWidgets.QPushButton(self.border)
        self.borrowed_books_button.setStyleSheet("QPushButton{\n"
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
        self.borrowed_books_button.setObjectName("borrowed_books_button")
        self.borrowed_books_button.clicked.connect(
            lambda: self.run_currently_borrowed_books(MainMenu))
        self.gridLayout.addWidget(self.borrowed_books_button, 4, 0, 1, 2)
        self.student_button = QtWidgets.QPushButton(self.border)
        self.student_button.setStyleSheet("QPushButton{\n"
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
        self.student_button.setObjectName("student_button")
        self.student_button.clicked.connect(
            lambda: self.run_student_information(MainMenu))
        self.gridLayout.addWidget(self.student_button, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.logout_button = QtWidgets.QPushButton(self.border)
        self.logout_button.setStyleSheet("QPushButton{\n"
                                         "    color: #842a2d;\n"
                                         "    font: 17pt \"Franklin Gothic Book\";\n"
                                         "    border: 2px solid #842a2d;\n"
                                         "    padding: 2px 53px;\n"
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
        self.logout_button.setObjectName("logout_button")
        self.logout_button.clicked.connect(
            lambda: self.logout_user(Login, MainMenu))
        self.horizontalLayout_3.addWidget(self.logout_button)
        self.gridLayout.addLayout(self.horizontalLayout_3, 8, 0, 1, 2)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.border)
        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)
        # * Pointing Hand Cursor for Buttons (Late Update)
        self.book_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.student_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.borrow_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.return_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.book_status_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.borrowed_books_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.overdue_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.search_history_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        # * Initialization
        self.get_random_quote(quote_data)
        self.evaluate_overdue_books()

    def logout_user(self, Login, MainMenu):
        MainMenu.close()
        Login.show()

    def get_name(self, username):
        con = sqlite3.connect('./db/library.db')
        query = "SELECT Librarian_Name FROM LIBRARIAN WHERE Librarian_Username = (?);"
        params = [username]
        result = list(enumerate(con.execute(query, params)))[0][1][0]
        return result

    def get_random_quote(self, quote_data):
        random_quote_data = random.choice(quote_data)
        quote = random_quote_data["quote"]
        author = random_quote_data["author"]
        book = random_quote_data["book"]
        self.random_quotes_generator.setText(
            f"\"{quote}\"\n- {author} ({book})")

    def run_book_information(self, MainMenu):
        self.BookInformation = QtWidgets.QWidget()
        self.ui_book_information = Ui_BookInformation()
        self.ui_book_information.setupUi(self.BookInformation, MainMenu)
        self.BookInformation.show()

    def run_student_information(self, MainMenu):
        MainMenu.close()
        self.StudentInformation = QtWidgets.QWidget()
        self.ui_student_information = Ui_StudentInformation()
        self.ui_student_information.setupUi(self.StudentInformation, MainMenu)
        self.StudentInformation.show()

    def run_return_request(self, MainMenu, current_username):
        self.ReturnRequest = QtWidgets.QWidget()
        self.ui_return_request = Ui_ReturnRequest()
        self.ui_return_request.setupUi(
            self.ReturnRequest, MainMenu, Ui_CurrentlyBorrowedBooks, current_username)
        self.ReturnRequest.show()

    def run_borrow_request(self, MainMenu, current_username):
        self.BorrowRequest = QtWidgets.QWidget()
        self.ui_borrow_request = Ui_BorrowRequest()
        self.ui_borrow_request.setupUi(
            self.BorrowRequest, MainMenu, current_username)
        self.BorrowRequest.show()

    def run_currently_borrowed_books(self, MainMenu):
        self.CurrentlyBorrowedBooks = QtWidgets.QWidget()
        self.ui_currently_borrowed_books = Ui_CurrentlyBorrowedBooks()
        self.ui_currently_borrowed_books.setupUi(
            self.CurrentlyBorrowedBooks, MainMenu)
        self.CurrentlyBorrowedBooks.show()

    def run_currently_overdue_books(self, MainMenu):
        self.CurrentlyOverduedBooks = QtWidgets.QWidget()
        self.ui_currently_Overdue_books = Ui_CurrentlyOverdueBooks()
        self.ui_currently_Overdue_books.setupUi(
            self.CurrentlyOverduedBooks, MainMenu)
        self.CurrentlyOverduedBooks.show()

    def run_book_status(self, MainMenu):
        MainMenu.close()
        self.BookStatus = QtWidgets.QWidget()
        self.ui_book_status = Ui_BookStatus()
        self.ui_book_status.setupUi(
            self.BookStatus, current_class=MainMenu)
        self.BookStatus.show()

    def run_search_history(self, MainMenu):
        self.SearchHistory = QtWidgets.QWidget()
        self.ui_search_history = Ui_SearchHistory()
        self.ui_search_history.setupUi(
            self.SearchHistory, MainMenu)
        self.SearchHistory.show()

    def evaluate_overdue_books(self):
        # * Goal #1. Evaluate the Overdue Books on the Main Menu class
        # *    so that it can be queried on the overdue_window.
        # * Step 1: Query relevant data to the database.
        con = sqlite3.connect('./db/library.db')
        cur = con.cursor()
        query = """
        SELECT Borrow_ID, Borrow_Date, Payment_ID
        FROM BORROW
        WHERE Borrow_Status = 'Borrowed';
        """
        result = [form[1] for form in list(enumerate(con.execute(query)))]
        for each_data in result:
            borrow_id = each_data[0]
            borrow_date = datetime.datetime.strptime(
                each_data[1], '%Y-%m-%d %H:%M:%S.%f')
            borrow_return_date = datetime.datetime.now()
            payment_id = each_data[2]
            penalty_amount = self.compute_amount(
                borrow_date, borrow_return_date)
            days_passed = (borrow_return_date-borrow_date).days
            if days_passed >= 7:
                # * UPDATE PAYMENT data: Compute Amount
                payment_query = """
                UPDATE PAYMENT
                SET Payment_Amount = ?
                WHERE Payment_ID = ?;
                """
                interpolate_data = [penalty_amount, payment_id]
                cur.execute(payment_query, interpolate_data)
                # * UPDATE BORROW Overdue_Status
                borrow_query = """
                UPDATE BORROW
                SET Borrow_Overdue_Status = ?
                WHERE Borrow_ID = ?;
                """
                interpolate_data = [1, borrow_id]
                cur.execute(borrow_query, interpolate_data)
        con.commit()
        con.close()

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

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "LMSPY: Main Menu"))
        self.title_name.setText(_translate(
            "MainMenu", "SCHOOL LIBRARY MANAGEMENT SYSTEM"))
        self.userloggedin_label.setText(
            _translate("MainMenu", "USER LOGGED IN:"))
        self.book_image.setText(_translate(
            "MainMenu", "<html><head/><body><p><img src=\"./icons/library.jpg\"/></p></body></html>"))
        self.random_quotes_generator.setText(
            _translate("MainMenu", "\"Quote here\" - Author"))
        self.overdue_button.setText(_translate("MainMenu", "OVERDUE BOOKS"))
        self.book_button.setText(_translate("MainMenu", "BOOK"))
        self.search_history_button.setText(_translate("MainMenu", "HISTORY"))
        self.borrow_button.setText(_translate("MainMenu", "BORROW"))
        self.return_button.setText(_translate("MainMenu", "RETURN"))
        self.book_status_button.setText(
            _translate("MainMenu", "VIEW BOOK STATUS"))
        self.borrowed_books_button.setText(
            _translate("MainMenu", "BORROWED BOOKS"))
        self.student_button.setText(_translate("MainMenu", "STUDENT"))
        self.logout_button.setText(_translate("MainMenu", "LOGOUT"))
