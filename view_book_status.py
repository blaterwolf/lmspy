from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_BookStatus(object):
    def setupUi(self, BookStatus, current_class):
        BookStatus.setObjectName("BookStatus")
        BookStatus.resize(740, 670)
        BookStatus.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        BookStatus.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(BookStatus)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.border = QtWidgets.QFrame(BookStatus)
        self.border.setStyleSheet("#border{\n"
                                  "    color: #842a2d;\n"
                                  "}")
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setLineWidth(5)
        self.border.setMidLineWidth(5)
        self.border.setObjectName("border")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.border)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_title = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_3.addWidget(self.label_title)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_currently_viewing = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_currently_viewing.setFont(font)
        self.label_currently_viewing.setObjectName("label_currently_viewing")
        self.horizontalLayout_2.addWidget(self.label_currently_viewing)
        self.viewing_status = QtWidgets.QLineEdit(self.border)
        self.viewing_status.setEnabled(False)
        self.viewing_status.setStyleSheet("QLineEdit {\n"
                                          "      color: #000000;\n"
                                          "      font: 15pt \"Verdana\";\n"
                                          "      border: None;\n"
                                          "      border-bottom-color: white;\n"
                                          "      border-radius: 10px;\n"
                                          "      padding: 0 8px;\n"
                                          "      background: #CBB1A0;\n"
                                          "      selection-background-color: darkgray;\n"
                                          "}")
        self.viewing_status.setObjectName("viewing_status")
        self.horizontalLayout_2.addWidget(self.viewing_status)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(self.border)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(230)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.available_button = QtWidgets.QPushButton(self.border)
        self.available_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.available_button.setStyleSheet("QPushButton{\n"
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
        self.available_button.setObjectName("available_button")
        self.available_button.clicked.connect(self.load_available_books_data)
        self.horizontalLayout.addWidget(self.available_button)
        self.borrowed_button = QtWidgets.QPushButton(self.border)
        self.borrowed_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.borrowed_button.setStyleSheet("QPushButton{\n"
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
        self.borrowed_button.setObjectName("borrowed_button")
        self.borrowed_button.clicked.connect(self.load_borrowed_books_data)
        self.horizontalLayout.addWidget(self.borrowed_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
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
            lambda: self.return_action(BookStatus, current_class))
        self.verticalLayout.addWidget(self.back_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.border)
        self.retranslateUi(BookStatus)
        QtCore.QMetaObject.connectSlotsByName(BookStatus)

    def return_action(self, BookStatus, current_class):
        BookStatus.close()
        current_class.show()
        pass

    def load_available_books_data(self):
        self.viewing_status.setText("AVAILABLE BOOKS")
        con = sqlite3.connect('./db/test.db')
        query = "SELECT Book_Title, Book_Author, Book_Condition FROM BOOK WHERE Book_Status = \"Available\";"
        result = con.execute(query)
        self.tableWidget.setRowCount(0)
        for row, form in enumerate(result):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(
                    row, column, QtWidgets.QTableWidgetItem(str(item)))

    def load_borrowed_books_data(self):
        self.viewing_status.setText("BORROWED BOOKS")
        con = sqlite3.connect('./db/test.db')
        query = "SELECT Book_Title, Book_Author, Book_Condition FROM BOOK WHERE Book_Status = 'Borrowed';"
        result = con.execute(query)
        self.tableWidget.setRowCount(0)
        for row, form in enumerate(result):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(
                    row, column, QtWidgets.QTableWidgetItem(str(item)))

    def retranslateUi(self, BookStatus):
        _translate = QtCore.QCoreApplication.translate
        BookStatus.setWindowTitle(_translate("BookStatus", "Form"))
        self.label_title.setText(_translate("BookStatus", "VIEW BOOK STATUS"))
        self.label_currently_viewing.setText(
            _translate("BookStatus", "CURRENTLY VIEWING:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BookStatus", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BookStatus", "Author"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("BookStatus", "Condition"))
        self.available_button.setText(
            _translate("BookStatus", "AVAILABLE BOOKS"))
        self.borrowed_button.setText(
            _translate("BookStatus", "BORROWED BOOKS"))
        self.back_button.setText(_translate("BookStatus", "BACK"))
