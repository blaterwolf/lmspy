from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_ViewStudentAndBooks(object):
    def setupUi(self, ViewStudentAndBooks, BorrowRequest):
        ViewStudentAndBooks.setObjectName("ViewStudentAndBooks")
        ViewStudentAndBooks.resize(835, 640)
        ViewStudentAndBooks.setStyleSheet(
            ".QWidget{background-color:  #CBB1A0;border-radius: 10px}")
        ViewStudentAndBooks.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(ViewStudentAndBooks)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.border = QtWidgets.QFrame(ViewStudentAndBooks)
        self.border.setStyleSheet("#border{\n"
                                  "    color: #842a2d;\n"
                                  "}")
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setLineWidth(5)
        self.border.setMidLineWidth(5)
        self.border.setObjectName("border")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.border)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_title = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_5.addWidget(self.label_title)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.student_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.student_label.setFont(font)
        self.student_label.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        self.student_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                        QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.student_label.setObjectName("student_label")
        self.verticalLayout_3.addWidget(self.student_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_student_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_student_label.setFont(font)
        self.search_student_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.search_student_label.setObjectName("search_student_label")
        self.verticalLayout.addWidget(self.search_student_label)
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
        self.verticalLayout.addWidget(self.input_search_student)
        self.line = QtWidgets.QFrame(self.border)
        self.line.setStyleSheet("border: 2px solid #842a2d;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.student_tableWidget = QtWidgets.QTableWidget(self.border)
        self.student_tableWidget.setObjectName("student_tableWidget")
        self.student_column_count = 4
        self.student_tableWidget.setColumnCount(self.student_column_count)
        self.student_tableWidget.setRowCount(0)
        for index in range(self.student_column_count):
            item = QtWidgets.QTableWidgetItem()
            self.student_tableWidget.setHorizontalHeaderItem(index, item)
        self.student_tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.verticalLayout_3.addWidget(self.student_tableWidget)
        self.status_label_student = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.status_label_student.setFont(font)
        self.status_label_student.setStyleSheet("padding: 10px 0px;\n"
                                                "color: red;")
        self.status_label_student.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_label_student.setObjectName("status_label_student")
        self.verticalLayout_3.addWidget(self.status_label_student)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.book_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.book_label.setFont(font)
        self.book_label.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        self.book_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                     QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.book_label.setObjectName("book_label")
        self.horizontalLayout.addWidget(self.book_label)
        self.available_books_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        self.available_books_label.setFont(font)
        self.available_books_label.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        self.available_books_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.available_books_label.setObjectName("available_books_label")
        self.horizontalLayout.addWidget(self.available_books_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.search_book_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_book_label.setFont(font)
        self.search_book_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                            QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.search_book_label.setObjectName("search_book_label")
        self.verticalLayout_2.addWidget(self.search_book_label)
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
        self.input_search_book.setMaxLength(50)
        self.input_search_book.setClearButtonEnabled(True)
        self.input_search_book.setObjectName("input_search_book")
        self.verticalLayout_2.addWidget(self.input_search_book)
        self.line_2 = QtWidgets.QFrame(self.border)
        self.line_2.setStyleSheet("border: 2px solid #842a2d;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.book_tableWidget = QtWidgets.QTableWidget(self.border)
        self.book_tableWidget.setObjectName("book_tableWidget")
        self.book_column_count = 6
        self.book_tableWidget.setColumnCount(self.book_column_count)
        self.book_tableWidget.setRowCount(0)
        for index in range(self.book_column_count):
            item = QtWidgets.QTableWidgetItem()
            self.book_tableWidget.setHorizontalHeaderItem(index, item)
        self.book_tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.verticalLayout_4.addWidget(self.book_tableWidget)
        self.status_label_book = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.status_label_book.setFont(font)
        self.status_label_book.setStyleSheet("padding: 10px 0px;\n"
                                             "color: red;")
        self.status_label_book.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_label_book.setObjectName("status_label_book")
        self.verticalLayout_4.addWidget(self.status_label_book)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.back_button = QtWidgets.QPushButton(self.border)
        self.back_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.back_button.setStyleSheet("QPushButton{\n"
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
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(
            lambda: self.return_action(ViewStudentAndBooks, BorrowRequest))
        self.verticalLayout_5.addWidget(self.back_button)
        self.horizontalLayout_3.addWidget(self.border)
        self.retranslateUi(ViewStudentAndBooks)
        QtCore.QMetaObject.connectSlotsByName(ViewStudentAndBooks)
        # * ever-changing-query
        self.input_search_student.textChanged.connect(self.query_student)
        self.input_search_book.textChanged.connect(self.query_book)
        self.load_students()
        self.load_book()

    def return_action(self, ViewStudentAndBooks, BorrowRequest):
        ViewStudentAndBooks.close()
        BorrowRequest.show()

    def load_students(self):
        con = sqlite3.connect('./db/library.db')
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

    def load_book(self):
        con = sqlite3.connect('./db/library.db')
        book_query = """
        SELECT * FROM BOOK
        WHERE Book_Status = 'Available';
        """
        book_result = con.execute(book_query)
        self.book_tableWidget.setRowCount(0)
        for row, form in enumerate(book_result):
            self.book_tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.book_tableWidget.setItem(
                    row, column, QtWidgets.QTableWidgetItem(str(item)))

    def query_student(self):
        search_value = self.input_search_student.text()
        if (search_value == ""):
            self.load_students()
            self.status_label_student.setText("")
        else:
            self.bruteforce_search_students(search_value)

    def query_book(self):
        search_value = self.input_search_book.text()
        if (search_value == ""):
            self.load_book()
            self.status_label_book.setText("")
        else:
            self.bruteforce_search_book(search_value)

    def book_data_to_query(self, i, like_query):
        data_query = [
            {
                "query": "SELECT * FROM BOOK WHERE Book_ID = ? AND Book_Status = 'Available';"
            },
            {
                "query": "SELECT * FROM BOOK WHERE Book_ISBN = ? AND Book_Status = 'Available';"
            },
            {
                "query": "SELECT * FROM BOOK WHERE Book_Condition = ? AND Book_Status = 'Available';"
            },
            {
                "query": f"SELECT * FROM BOOK WHERE Book_Title LIKE '{like_query}' AND Book_Status = 'Available';"
            },
            {
                "query": f"SELECT * FROM BOOK WHERE Book_Author LIKE '{like_query}' AND Book_Status = 'Available';"
            },
            {
                "query": "SELECT * FROM BOOK WHERE Book_Status = ? AND Book_Status = 'Available';"
            }
        ]
        return data_query[i]["query"]

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

    def bruteforce_search_students(self, search_value):
        con = sqlite3.connect('./db/library.db')
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
            interpolate_data = [search_value]
            if iteration == 1:
                interpolate_data = [search_value, search_value]
            result = cur.execute(query)
            data = cur.fetchall()
            if data:
                self.status_label_student.setText("")
                self.student_tableWidget.setRowCount(0)
                for row in range(len(data)):
                    self.student_tableWidget.insertRow(row)
                    for column, item in enumerate(data[row]):
                        self.student_tableWidget.setItem(
                            row, column, QtWidgets.QTableWidgetItem(str(item)))
                break
            else:
                self.student_tableWidget.setRowCount(0)
                self.status_label_student.setText(
                    "Your search result does not exist!")
            iteration += 1

    def bruteforce_search_book(self, search_value):
        con = sqlite3.connect('./db/library.db')
        cur = con.cursor()
        iteration = 0
        while iteration <= 5:
            # * iteration id
            # * 0: book_id
            # * 1: isbn
            # * 2: title
            # * 3: author
            # * 4: condition
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
                self.status_label_book.setText("")
                self.book_tableWidget.setRowCount(0)
                for row in range(len(data)):
                    self.book_tableWidget.insertRow(row)
                    for column, item in enumerate(data[row]):
                        self.book_tableWidget.setItem(
                            row, column, QtWidgets.QTableWidgetItem(str(item)))
                break
            else:
                self.book_tableWidget.setRowCount(0)
                self.status_label_book.setText(
                    "Your search result does not exist!")
            iteration += 1

    def retranslateUi(self, ViewStudentAndBooks):
        _translate = QtCore.QCoreApplication.translate
        ViewStudentAndBooks.setWindowTitle(_translate(
            "ViewStudentAndBooks", "View Student And Books"))
        self.label_title.setText(_translate(
            "ViewStudentAndBooks", "VIEW STUDENT AND BOOKS"))
        self.student_label.setText(_translate(
            "ViewStudentAndBooks", "STUDENT"))
        self.search_student_label.setText(_translate(
            "ViewStudentAndBooks", "Search Student:"))
        self.column_student_text = ["Student ID",
                                    "Student Name", "Section", "Year Level"]
        for index in range(self.student_column_count):
            item = self.student_tableWidget.horizontalHeaderItem(index)
            item.setText(_translate("SearchHistory",
                         self.column_student_text[index]))
        self.status_label_student.setText(_translate(
            "ViewStudentAndBooks", ""))
        self.book_label.setText(_translate("ViewStudentAndBooks", "BOOK"))
        self.available_books_label.setText(_translate(
            "ViewStudentAndBooks", "(available books)"))
        self.search_book_label.setText(_translate(
            "ViewStudentAndBooks", "Search Book:"))
        self.column_book_text = ["Book ID", "ISBN",
                                 "Title", "Author", "Condition", "Status"]
        for index in range(self.book_column_count):
            item = self.book_tableWidget.horizontalHeaderItem(index)
            item.setText(_translate("SearchHistory",
                         self.column_book_text[index]))
        self.status_label_book.setText(_translate(
            "ViewStudentAndBooks", ""))
        self.back_button.setText(_translate("ViewStudentAndBooks", "BACK"))
