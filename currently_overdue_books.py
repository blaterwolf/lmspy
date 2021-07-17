from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_CurrentlyOverdueBooks(object):
    def setupUi(self, CurrentlyOverdueBooks, MainMenu):
        MainMenu.close()
        CurrentlyOverdueBooks.setObjectName("CurrentlyOverdueBooks")
        CurrentlyOverdueBooks.resize(740, 670)
        CurrentlyOverdueBooks.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        CurrentlyOverdueBooks.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout = QtWidgets.QVBoxLayout(CurrentlyOverdueBooks)
        self.verticalLayout.setObjectName("verticalLayout")
        self.border = QtWidgets.QFrame(CurrentlyOverdueBooks)
        self.border.setStyleSheet("#border{\n"
                                  "    color: #842a2d;\n"
                                  "}")
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setLineWidth(5)
        self.border.setMidLineWidth(5)
        self.border.setObjectName("border")
        self.gridLayout = QtWidgets.QGridLayout(self.border)
        self.gridLayout.setObjectName("gridLayout")
        self.overdue_title_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.overdue_title_label.setFont(font)
        self.overdue_title_label.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        self.overdue_title_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.overdue_title_label.setObjectName("overdue_title_label")
        self.gridLayout.addWidget(self.overdue_title_label, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.border)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
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
            lambda: self.return_action(CurrentlyOverdueBooks, MainMenu))
        self.gridLayout.addWidget(self.back_button, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.border)

        self.retranslateUi(CurrentlyOverdueBooks)
        QtCore.QMetaObject.connectSlotsByName(CurrentlyOverdueBooks)
        self.load_currently_overdue_books()

    def return_action(self, CurrentlyOverdueBooks, MainMenu):
        CurrentlyOverdueBooks.close()
        MainMenu.show()

    def load_currently_overdue_books(self):
        con = sqlite3.connect('./db/library.db')
        query = """
        SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Librarian_Name, Payment_Amount 
        FROM BORROW
        LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID
        LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID
        LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer
        LEFT JOIN PAYMENT ON PAYMENT.Payment_ID = BORROW.Payment_ID
        WHERE Borrow_Overdue_Status = 1;
        """
        result = con.execute(query)
        self.tableWidget.setRowCount(0)
        for row, form in enumerate(result):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(
                    row, column, QtWidgets.QTableWidgetItem(str(item)))

    def retranslateUi(self, CurrentlyOverdueBooks):
        _translate = QtCore.QCoreApplication.translate
        CurrentlyOverdueBooks.setWindowTitle(
            _translate("CurrentlyOverdueBooks", "Borrow History"))
        self.overdue_title_label.setText(_translate(
            "CurrentlyOverdueBooks", "CURRENTLY OVERDUE BOOKS"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("CurrentlyOverdueBooks", "Borrow ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("CurrentlyOverdueBooks", "Student Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("CurrentlyOverdueBooks", "Book Title"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("CurrentlyOverdueBooks", "Borrow Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("CurrentlyOverdueBooks", "Librarian Issuer"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("CurrentlyOverdueBooks", "Payment Amount"))
        self.back_button.setText(_translate("CurrentlyOverdueBooks", "BACK"))
