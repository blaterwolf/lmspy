from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_SearchHistory(object):
    def setupUi(self, SearchHistory, MainMenu):
        SearchHistory.setObjectName("SearchHistory")
        SearchHistory.resize(1200, 700)
        SearchHistory.setStyleSheet(
            ".QWidget{background-color:  #CBB1A0;border-radius: 10px}")
        SearchHistory.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SearchHistory)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.border = QtWidgets.QFrame(SearchHistory)
        self.border.setStyleSheet("#border{\n"
                                  "    color: #842a2d;\n"
                                  "}")
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setLineWidth(5)
        self.border.setMidLineWidth(5)
        self.border.setObjectName("border")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.border)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_name = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title_name.setFont(font)
        self.title_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_name.setObjectName("title_name")
        self.verticalLayout.addWidget(self.title_name)
        self.tables = QtWidgets.QGridLayout()
        self.tables.setObjectName("tables")
        self.student_form = QtWidgets.QFormLayout()
        self.student_form.setObjectName("student_form")
        self.student_VerticalLayout = QtWidgets.QVBoxLayout()
        self.student_VerticalLayout.setContentsMargins(-1, 0, 0, -1)
        self.student_VerticalLayout.setObjectName("student_VerticalLayout")
        self.student_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.student_label.setFont(font)
        self.student_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.student_label.setObjectName("student_label")
        self.student_VerticalLayout.addWidget(self.student_label)
        self.student_id_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.student_id_label.setFont(font)
        self.student_id_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                           QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.student_id_label.setObjectName("student_id_label")
        self.student_VerticalLayout.addWidget(self.student_id_label)
        self.input_search_student = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.input_search_student.setFont(font)
        self.input_search_student.setStyleSheet("QLineEdit {\n"
                                                "      color: #000000;\n"
                                                "      font: 11pt \"Verdana\";\n"
                                                "      border: None;\n"
                                                "      border-bottom-color: white;\n"
                                                "      border-radius: 10px;\n"
                                                "      padding: 0 8px;\n"
                                                "      background: #CBB1A0;\n"
                                                "      selection-background-color: darkgray;\n"
                                                "}")
        self.input_search_student.setMaxLength(50)
        self.input_search_student.setClearButtonEnabled(True)
        self.input_search_student.setObjectName("input_search_student")
        self.student_VerticalLayout.addWidget(self.input_search_student)
        self.line = QtWidgets.QFrame(self.border)
        self.line.setStyleSheet("border: 2px solid #842a2d;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.student_VerticalLayout.addWidget(self.line)
        self.student_reset_button = QtWidgets.QPushButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.student_reset_button.setFont(font)
        self.student_reset_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.student_reset_button.setStyleSheet("QPushButton{\n"
                                                "    color: #842a2d;\n"
                                                "    font: 12pt \"Franklin Gothic Book\" bold;\n"
                                                "    border: 2px solid #842a2d;\n"
                                                "    padding: 2px 5px;\n"
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
                                                "background-color: #b34044;\n"
                                                "border: 5px solid #b34044;\n"
                                                "}")
        self.student_reset_button.setObjectName("student_reset_button")
        self.student_VerticalLayout.addWidget(self.student_reset_button)
        self.student_form.setLayout(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.student_VerticalLayout)
        self.student_tableWidget = QtWidgets.QTableWidget(self.border)
        self.student_tableWidget.setObjectName("student_tableWidget")
        self.student_column_count = 4
        self.student_tableWidget.setColumnCount(self.student_column_count)
        self.student_tableWidget.setRowCount(0)
        for index in range(self.student_column_count):
            item = QtWidgets.QTableWidgetItem()
            self.student_tableWidget.setHorizontalHeaderItem(index, item)
        self.student_tableWidget.horizontalHeader().setDefaultSectionSize(185)
        self.student_form.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.student_tableWidget)
        self.tables.addLayout(self.student_form, 0, 0, 1, 1)
        self.book_form = QtWidgets.QFormLayout()
        self.book_form.setObjectName("book_form")
        self.book_verticalLayout = QtWidgets.QVBoxLayout()
        self.book_verticalLayout.setContentsMargins(1, -1, 1, -1)
        self.book_verticalLayout.setObjectName("book_verticalLayout")
        self.book_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.book_label.setFont(font)
        self.book_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.book_label.setObjectName("book_label")
        self.book_verticalLayout.addWidget(self.book_label)
        self.book_id_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.book_id_label.setFont(font)
        self.book_id_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                        QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.book_id_label.setObjectName("book_id_label")
        self.book_verticalLayout.addWidget(self.book_id_label)
        self.input_search_book = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.input_search_book.setFont(font)
        self.input_search_book.setStyleSheet("QLineEdit {\n"
                                             "      color: #000000;\n"
                                             "      font: 11pt \"Verdana\";\n"
                                             "      border: None;\n"
                                             "      border-bottom-color: white;\n"
                                             "      border-radius: 10px;\n"
                                             "      padding: 0 8px;\n"
                                             "      background: #CBB1A0;\n"
                                             "      selection-background-color: darkgray;\n"
                                             "}")
        self.input_search_book.setInputMask("")
        self.input_search_book.setText("")
        self.input_search_book.setMaxLength(100)
        self.input_search_book.setClearButtonEnabled(True)
        self.input_search_book.setObjectName("input_search_book")
        self.book_verticalLayout.addWidget(self.input_search_book)
        self.line_2 = QtWidgets.QFrame(self.border)
        self.line_2.setStyleSheet("border: 2px solid #842a2d;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.book_verticalLayout.addWidget(self.line_2)
        self.book_reset_button = QtWidgets.QPushButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.book_reset_button.setFont(font)
        self.book_reset_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.book_reset_button.setStyleSheet("QPushButton{\n"
                                             "    color: #842a2d;\n"
                                             "    font: 12pt \"Franklin Gothic Book\" bold;\n"
                                             "    border: 2px solid #842a2d;\n"
                                             "    padding: 2px 5px;\n"
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
                                             "background-color: #b34044;\n"
                                             "border: 5px solid #b34044;\n"
                                             "}")
        self.book_reset_button.setObjectName("book_reset_button")
        self.book_verticalLayout.addWidget(self.book_reset_button)
        self.book_form.setLayout(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.book_verticalLayout)
        self.book_tableWidget = QtWidgets.QTableWidget(self.border)
        self.book_tableWidget.setObjectName("book_tableWidget")
        self.book_column_count = 6
        self.book_tableWidget.setColumnCount(self.book_column_count)
        self.book_tableWidget.setRowCount(0)
        for index in range(self.book_column_count):
            item = QtWidgets.QTableWidgetItem()
            self.book_tableWidget.setHorizontalHeaderItem(index, item)
        self.book_tableWidget.horizontalHeader().setDefaultSectionSize(185)
        self.book_form.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.book_tableWidget)
        self.tables.addLayout(self.book_form, 1, 0, 1, 1)
        self.borrow_form = QtWidgets.QFormLayout()
        self.borrow_form.setObjectName("borrow_form")
        self.borrow_verticalLayout = QtWidgets.QVBoxLayout()
        self.borrow_verticalLayout.setObjectName("borrow_verticalLayout")
        self.borrow_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.borrow_label.setFont(font)
        self.borrow_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.borrow_label.setObjectName("borrow_label")
        self.borrow_verticalLayout.addWidget(self.borrow_label)
        self.borrow_id_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.borrow_id_label.setFont(font)
        self.borrow_id_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                          QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.borrow_id_label.setObjectName("borrow_id_label")
        self.borrow_verticalLayout.addWidget(self.borrow_id_label)
        self.input_search_borrow = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.input_search_borrow.setFont(font)
        self.input_search_borrow.setStyleSheet("QLineEdit {\n"
                                               "      color: #000000;\n"
                                               "      font: 11pt \"Verdana\";\n"
                                               "      border: None;\n"
                                               "      border-bottom-color: white;\n"
                                               "      border-radius: 10px;\n"
                                               "      padding: 0 8px;\n"
                                               "      background: #CBB1A0;\n"
                                               "      selection-background-color: darkgray;\n"
                                               "}")
        self.input_search_borrow.setInputMask("")
        self.input_search_borrow.setMaxLength(20)
        self.input_search_borrow.setClearButtonEnabled(True)
        self.input_search_borrow.setObjectName("input_search_borrow")
        self.borrow_verticalLayout.addWidget(self.input_search_borrow)
        self.line_3 = QtWidgets.QFrame(self.border)
        self.line_3.setStyleSheet("border: 2px solid #842a2d;")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.borrow_verticalLayout.addWidget(self.line_3)
        self.borrow_reset_button = QtWidgets.QPushButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.borrow_reset_button.setFont(font)
        self.borrow_reset_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.borrow_reset_button.setStyleSheet("QPushButton{\n"
                                               "    color: #842a2d;\n"
                                               "    font: 12pt \"Franklin Gothic Book\" bold;\n"
                                               "    border: 2px solid #842a2d;\n"
                                               "    padding: 2px 5px;\n"
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
                                               "background-color: #b34044;\n"
                                               "border: 5px solid #b34044;\n"
                                               "}")
        self.borrow_reset_button.setObjectName("borrow_reset_button")
        self.borrow_verticalLayout.addWidget(self.borrow_reset_button)
        self.borrow_form.setLayout(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.borrow_verticalLayout)
        self.borrow_tableWidget = QtWidgets.QTableWidget(self.border)
        self.borrow_tableWidget.setObjectName("borrow_tableWidget")
        self.borrow_column_count = 9
        self.borrow_tableWidget.setColumnCount(self.borrow_column_count)
        self.borrow_tableWidget.setRowCount(0)
        for index in range(self.borrow_column_count):
            item = QtWidgets.QTableWidgetItem()
            self.borrow_tableWidget.setHorizontalHeaderItem(index, item)
        self.borrow_form.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.borrow_tableWidget)
        self.tables.addLayout(self.borrow_form, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.tables)
        self.below = QtWidgets.QHBoxLayout()
        self.below.setObjectName("below")
        self.status_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("padding: 10px 0px;\n"
                                        "color: red;")
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                       QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.status_label.setObjectName("status_label")
        self.below.addWidget(self.status_label)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.below.addItem(spacerItem)
        self.back_button = QtWidgets.QPushButton(self.border)
        self.back_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.back_button.setStyleSheet("QPushButton{\n"
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
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "background-color: #b34044;\n"
                                       "border: 5px solid #b34044;\n"
                                       "}")
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(
            lambda: self.return_action(SearchHistory, MainMenu))
        self.below.addWidget(self.back_button)
        self.verticalLayout.addLayout(self.below)
        self.verticalLayout_2.addWidget(self.border)
        self.retranslateUi(SearchHistory)
        QtCore.QMetaObject.connectSlotsByName(SearchHistory)
        # * initial query
        self.load_initial_data()
        # * functions
        self.student_reset_button.clicked.connect(
            lambda: self.reset_func("Student"))
        self.book_reset_button.clicked.connect(
            lambda: self.reset_func("Book"))
        self.borrow_reset_button.clicked.connect(
            lambda: self.reset_func("Borrow"))
        # * ever-changing-query
        self.input_search_student.textChanged.connect(
            lambda: self.query_func(action_to_do="Student"))
        self.input_search_book.textChanged.connect(
            lambda: self.query_func(action_to_do="Book"))
        self.input_search_borrow.textChanged.connect(
            lambda: self.query_func(action_to_do="Borrow"))

    def return_action(self, SearchHistory, MainMenu):
        SearchHistory.close()
        MainMenu.show()

    def load_student_data(self):
        con = sqlite3.connect('./db/test.db')
        student_query = """
        SELECT Student_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Student_Section, Student_YearLevel
        FROM STUDENT;
        """
        student_result = con.execute(student_query)
        self.student_tableWidget.setRowCount(0)
        for row, form in enumerate(student_result):
            self.student_tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.student_tableWidget.setItem(
                    row, column, QtWidgets.QTableWidgetItem(str(item)))

    def load_book_data(self):
        con = sqlite3.connect('./db/test.db')
        book_query = """
        SELECT * FROM BOOK;
        """
        book_result = con.execute(book_query)
        self.book_tableWidget.setRowCount(0)
        for row, form in enumerate(book_result):
            self.book_tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.book_tableWidget.setItem(
                    row, column, QtWidgets.QTableWidgetItem(str(item)))

    def load_borrow_data(self):
        con = sqlite3.connect('./db/test.db')
        borrow_query = """
        SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Borrow_Return_Date, Borrow_Status, Borrow_Overdue_Status, Librarian_Name AS Borrow_Issuer, Payment_Amount
        FROM BORROW
        LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID
        LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID
        LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer 
        LEFT JOIN PAYMENT ON PAYMENT.Payment_ID = BORROW.Payment_ID
        """
        borrow_result = con.execute(borrow_query)
        self.borrow_tableWidget.setRowCount(0)
        for row, form in enumerate(borrow_result):
            self.borrow_tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.borrow_tableWidget.setItem(
                    row, column, QtWidgets.QTableWidgetItem(str(item)))

    def load_initial_data(self):
        self.load_student_data()
        self.load_book_data()
        self.load_borrow_data()

    def reset_func(self, action_to_do):
        if (action_to_do == "Student"):
            self.load_student_data()
            self.input_search_student.clear()
        if (action_to_do == "Book"):
            self.load_book_data()
            self.input_search_book.clear()
        if (action_to_do == "Borrow"):
            self.load_borrow_data()
            self.input_search_borrow.clear()
        self.status_label.clear()

    def query_func(self, action_to_do):
        if (action_to_do == "Student"):
            search_value = self.input_search_student.text()
            if (search_value == ""):
                self.load_student_data()
                self.status_label.setText("")
            else:
                pass
                self.bruteforce_search_students(search_value)
        if (action_to_do == "Book"):
            search_value = self.input_search_book.text()
            if (search_value == ""):
                self.load_book_data()
                self.status_label.setText("")
            else:
                pass
                self.bruteforce_search_books(search_value)
        if (action_to_do == "Borrow"):
            search_value = self.input_search_borrow.text()
            if (search_value == ""):
                self.load_borrow_data()
                self.status_label.setText("")
            else:
                self.bruteforce_search_borrow(search_value)

    def student_data_to_query(self, i, like_query):
        data_query = [
            {
                "query": f"SELECT Student_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Student_Section, Student_YearLevel FROM STUDENT WHERE Student_ID LIKE '{like_query}';"
            },
            {
                "query": f"SELECT Student_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Student_Section, Student_YearLevel FROM STUDENT WHERE Student_LastName LIKE '{like_query}' OR Student_FirstName LIKE '{like_query}';"
            },
            {
                "query": f"SELECT Student_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Student_Section, Student_YearLevel FROM STUDENT WHERE Student_Section LIKE '{like_query}';"
            },
            {
                "query": f"SELECT Student_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Student_Section, Student_YearLevel FROM STUDENT WHERE Student_YearLevel LIKE '{like_query}';"
            },
        ]
        return data_query[i]["query"]

    def book_data_to_query(self, i, like_query):
        data_query = [
            {
                "query": "SELECT * FROM BOOK WHERE Book_ID = ?;"
            },
            {
                "query": "SELECT * FROM BOOK WHERE Book_ISBN = ?;"
            },
            {
                "query": "SELECT * FROM BOOK WHERE Book_Condition = ?;"
            },
            {
                "query": f"SELECT * FROM BOOK WHERE Book_Title LIKE '{like_query}';"
            },
            {
                "query": f"SELECT * FROM BOOK WHERE Book_Author LIKE '{like_query}';"
            },
            {
                "query": "SELECT * FROM BOOK WHERE Book_Status = ?;"
            }
        ]
        return data_query[i]["query"]

    def borrow_data_to_query(self, i, like_query):
        data_query = [
            {
                "query": f"SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Borrow_Return_Date, Borrow_Status, Borrow_Overdue_Status, Librarian_Name AS Borrow_Issuer, Payment_Amount FROM BORROW LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer LEFT JOIN PAYMENT ON PAYMENT.Payment_ID = BORROW.Payment_ID WHERE Borrow_ID LIKE '{like_query}';"
            },
            {
                "query": f"SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Borrow_Return_Date, Borrow_Status, Borrow_Overdue_Status, Librarian_Name AS Borrow_Issuer, Payment_Amount FROM BORROW LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer LEFT JOIN PAYMENT ON PAYMENT.Payment_ID = BORROW.Payment_ID WHERE Borrow_Status LIKE '{like_query}';"
            },
            {
                "query": f"SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Borrow_Return_Date, Borrow_Status, Borrow_Overdue_Status, Librarian_Name AS Borrow_Issuer, Payment_Amount FROM BORROW LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer LEFT JOIN PAYMENT ON PAYMENT.Payment_ID = BORROW.Payment_ID WHERE Borrow_Date LIKE '{like_query}';"
            }
        ]
        return data_query[i]["query"]

    def bruteforce_search_students(self, search_value):
        con = sqlite3.connect('./db/test.db')
        cur = con.cursor()
        iteration = 0
        lever = True
        while iteration <= 3:
            # * iteration id
            # * 0: student_id
            # * 1: name
            # * 2: section
            # * 3: year level
            query = self.student_data_to_query(
                iteration, like_query=f'%{search_value}%')
            result = cur.execute(query)
            data = cur.fetchall()
            if data:
                self.status_label.setText("")
                self.student_tableWidget.setRowCount(0)
                for row in range(len(data)):
                    self.student_tableWidget.insertRow(row)
                    for column, item in enumerate(data[row]):
                        self.student_tableWidget.setItem(
                            row, column, QtWidgets.QTableWidgetItem(str(item)))
                break
            else:
                self.student_tableWidget.setRowCount(0)
                self.status_label.setText(
                    "Your search result does not exist!")
            iteration += 1

    def bruteforce_search_books(self, search_value):
        con = sqlite3.connect('./db/test.db')
        cur = con.cursor()
        iteration = 0
        while iteration <= 5:
            # * iteration id
            # * 0: book_id
            # * 1: isbn
            # * 2: condition
            # * 3: title
            # * 4: author
            # * 5: status
            query = self.book_data_to_query(
                iteration, like_query=f'%{search_value}%')
            if iteration == 3 or iteration == 4:
                result = cur.execute(query)
            else:
                interpolate_data = [search_value]
                result = cur.execute(query, interpolate_data)
            data = cur.fetchall()
            if data:
                self.status_label.setText("")
                self.book_tableWidget.setRowCount(0)
                for row in range(len(data)):
                    self.book_tableWidget.insertRow(row)
                    for column, item in enumerate(data[row]):
                        self.book_tableWidget.setItem(
                            row, column, QtWidgets.QTableWidgetItem(str(item)))
                break
            else:
                self.book_tableWidget.setRowCount(0)
                self.status_label.setText(
                    "Your search result does not exist!")
            iteration += 1

    def bruteforce_search_borrow(self, search_value):
        con = sqlite3.connect('./db/test.db')
        cur = con.cursor()
        iteration = 0
        while iteration <= 2:
            # * iteration id
            # * 0: borrow_id
            # * 1: borrow_status
            # * 2: borrow_date
            query = self.borrow_data_to_query(
                iteration, like_query=f'%{search_value}%')
            result = cur.execute(query)
            data = cur.fetchall()
            if data:
                self.status_label.setText("")
                self.borrow_tableWidget.setRowCount(0)
                for row in range(len(data)):
                    self.borrow_tableWidget.insertRow(row)
                    for column, item in enumerate(data[row]):
                        self.borrow_tableWidget.setItem(
                            row, column, QtWidgets.QTableWidgetItem(str(item)))
                break
            else:
                self.borrow_tableWidget.setRowCount(0)
                self.status_label.setText(
                    "Your search result does not exist!")
            iteration += 1

    def retranslateUi(self, SearchHistory):
        _translate = QtCore.QCoreApplication.translate
        SearchHistory.setWindowTitle(
            _translate("SearchHistory", "Search History"))
        self.title_name.setText(_translate("SearchHistory", "SEARCH HISTORY"))
        self.student_label.setText(_translate("SearchHistory", "STUDENT"))
        self.student_id_label.setText(_translate(
            "SearchHistory", "Search Student data:"))
        self.student_reset_button.setText(
            _translate("SearchHistory", "RESET STUDENT TABLE"))
        self.column_student_text = ["Student ID",
                                    "Student Name", "Section", "Year Level"]
        for index in range(self.student_column_count):
            item = self.student_tableWidget.horizontalHeaderItem(index)
            item.setText(_translate("SearchHistory",
                         self.column_student_text[index]))
        self.book_label.setText(_translate("SearchHistory", "BOOK"))
        self.book_id_label.setText(_translate(
            "SearchHistory", "Search Book data:"))
        self.book_reset_button.setText(_translate(
            "SearchHistory", "   RESET BOOK TABLE   "))

        self.column_book_text = ["Book ID", "ISBN",
                                 "Title", "Author", "Condition", "Status"]
        for index in range(self.book_column_count):
            item = self.book_tableWidget.horizontalHeaderItem(index)
            item.setText(_translate("SearchHistory",
                         self.column_book_text[index]))
        self.borrow_label.setText(_translate("SearchHistory", "BORROW"))
        self.borrow_id_label.setText(_translate(
            "SearchHistory", "Search Borrow data:\n(ID, Borrow Date, Status)"))
        self.borrow_reset_button.setText(
            _translate("SearchHistory", "RESET BORROW TABLE"))
        self.column_borrow_text = ["Borrow ID", "Student Name",
                                   "Book Title", "Borrow Date", "Return Date", "Status", "Overdue Status", "Issuer", "Payment Amount"]
        for index in range(self.borrow_column_count):
            item = self.borrow_tableWidget.horizontalHeaderItem(index)
            item.setText(_translate("SearchHistory",
                         self.column_borrow_text[index]))
        self.back_button.setText(_translate("SearchHistory", "BACK"))
