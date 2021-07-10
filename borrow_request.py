# Form implementation generated from reading ui file 'borrow_request.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BorrowRequest(object):
    def setupUi(self, BorrowRequest, MainMenu):
        MainMenu.close()
        BorrowRequest.setObjectName("BorrowRequest")
        BorrowRequest.resize(526, 356)
        BorrowRequest.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        BorrowRequest.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(BorrowRequest)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.border = QtWidgets.QFrame(BorrowRequest)
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
        self.label_StudID = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_StudID.setFont(font)
        self.label_StudID.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                       QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_StudID.setObjectName("label_StudID")
        self.gridLayout.addWidget(self.label_StudID, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_StudId = QtWidgets.QLineEdit(self.border)
        self.input_StudId.setStyleSheet("QLineEdit {\n"
                                        "      color: #000000;\n"
                                        "      font: 15pt \"Verdana\";\n"
                                        "      border: None;\n"
                                        "      border-bottom-color: white;\n"
                                        "      border-radius: 10px;\n"
                                        "      padding: 0 8px;\n"
                                        "      background: #CBB1A0;\n"
                                        "      selection-background-color: darkgray;\n"
                                        "}")
        self.input_StudId.setObjectName("input_StudId")
        self.verticalLayout.addWidget(self.input_StudId)
        self.line_3 = QtWidgets.QFrame(self.border)
        self.line_3.setStyleSheet("border: 2px solid #842a2d;")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.input_BookId = QtWidgets.QLineEdit(self.border)
        self.input_BookId.setStyleSheet("QLineEdit {\n"
                                        "      color: #000000;\n"
                                        "      font: 15pt \"Verdana\";\n"
                                        "      border: None;\n"
                                        "      border-bottom-color: white;\n"
                                        "      border-radius: 10px;\n"
                                        "      padding: 0 8px;\n"
                                        "      background: #CBB1A0;\n"
                                        "      selection-background-color: darkgray;\n"
                                        "}")
        self.input_BookId.setObjectName("input_BookId")
        self.verticalLayout.addWidget(self.input_BookId)
        self.line_4 = QtWidgets.QFrame(self.border)
        self.line_4.setStyleSheet("border: 2px solid #842a2d;")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 2, 1)
        self.label_BookId = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_BookId.setFont(font)
        self.label_BookId.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                       QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_BookId.setObjectName("label_BookId")
        self.gridLayout.addWidget(self.label_BookId, 1, 0, 1, 1)
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
        self.borrow_button = QtWidgets.QPushButton(self.border)
        self.borrow_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
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
                                         "}")
        self.borrow_button.setObjectName("borrow_button")
        self.verticalLayout_3.addWidget(self.borrow_button)
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
            lambda: self.return_action(BorrowRequest, MainMenu))
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.border)

        self.retranslateUi(BorrowRequest)
        QtCore.QMetaObject.connectSlotsByName(BorrowRequest)

    def return_action(self, BorrowRequest, MainMenu):
        BorrowRequest.close()
        MainMenu.show()

    def retranslateUi(self, BorrowRequest):
        _translate = QtCore.QCoreApplication.translate
        BorrowRequest.setWindowTitle(
            _translate("BorrowRequest", "Borrow a Book"))
        self.borrow_book_label.setText(
            _translate("BorrowRequest", "BORROW A BOOK"))
        self.label_StudID.setText(_translate("BorrowRequest", "Student ID:"))
        self.label_BookId.setText(_translate("BorrowRequest", "Book ID:"))
        self.borrow_button.setText(_translate("BorrowRequest", "BORROW"))
        self.view_borrowed_books_button.setText(
            _translate("BorrowRequest", "  VIEW BORROWED BOOKS  "))
        self.cancel_button.setText(_translate("BorrowRequest", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BorrowRequest = QtWidgets.QWidget()
    ui = Ui_BorrowRequest()
    ui.setupUi(BorrowRequest)
    BorrowRequest.show()
    sys.exit(app.exec())