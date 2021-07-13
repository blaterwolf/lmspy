from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SearchHistory(object):
    def setupUi(self, SearchHistory, MainMenu):
        SearchHistory.setObjectName("SearchHistory")
        SearchHistory.resize(1000, 669)
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
        self.student_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
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
        self.input_student_id = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.input_student_id.setFont(font)
        self.input_student_id.setStyleSheet("QLineEdit {\n"
                                            "      color: #000000;\n"
                                            "      font: 11pt \"Verdana\";\n"
                                            "      border: None;\n"
                                            "      border-bottom-color: white;\n"
                                            "      border-radius: 10px;\n"
                                            "      padding: 0 8px;\n"
                                            "      background: #CBB1A0;\n"
                                            "      selection-background-color: darkgray;\n"
                                            "}")
        self.input_student_id.setMaxLength(12)
        self.input_student_id.setObjectName("input_student_id")
        self.student_VerticalLayout.addWidget(self.input_student_id)
        self.line = QtWidgets.QFrame(self.border)
        self.line.setStyleSheet("border: 2px solid #842a2d;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.student_VerticalLayout.addWidget(self.line)
        self.student_search_button = QtWidgets.QPushButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.student_search_button.setFont(font)
        self.student_search_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.student_search_button.setStyleSheet("QPushButton{\n"
                                                 "    color: #842a2d;\n"
                                                 "    font: 12pt \"Franklin Gothic Book\" bold;\n"
                                                 "    border: 2px solid #842a2d;\n"
                                                 "    padding: 2px 53px;\n"
                                                 "    border-radius: 10px;\n"
                                                 "    opacity: 100;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover{\n"
                                                 "    background-color: #842a2d;\n"
                                                 "    color: #CBB1A0;\n"
                                                 "}")
        self.student_search_button.setObjectName("student_search_button")
        self.student_VerticalLayout.addWidget(self.student_search_button)
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
                                                "}")
        self.student_reset_button.setObjectName("student_reset_button")
        self.student_VerticalLayout.addWidget(self.student_reset_button)
        self.student_form.setLayout(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.student_VerticalLayout)
        self.student_tableWidget = QtWidgets.QTableWidget(self.border)
        self.student_tableWidget.setObjectName("student_tableWidget")
        self.student_tableWidget.setColumnCount(4)
        self.student_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.student_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.student_tableWidget.setHorizontalHeaderItem(3, item)
        self.student_tableWidget.horizontalHeader().setDefaultSectionSize(185)
        self.student_form.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.student_tableWidget)
        self.tables.addLayout(self.student_form, 0, 0, 1, 1)
        self.book_form = QtWidgets.QFormLayout()
        self.book_form.setObjectName("book_form")
        self.book_verticalLayout = QtWidgets.QVBoxLayout()
        self.book_verticalLayout.setContentsMargins(12, -1, 12, -1)
        self.book_verticalLayout.setObjectName("book_verticalLayout")
        self.book_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.book_label.setFont(font)
        self.book_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
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
        self.input_book_id = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.input_book_id.setFont(font)
        self.input_book_id.setStyleSheet("QLineEdit {\n"
                                         "      color: #000000;\n"
                                         "      font: 11pt \"Verdana\";\n"
                                         "      border: None;\n"
                                         "      border-bottom-color: white;\n"
                                         "      border-radius: 10px;\n"
                                         "      padding: 0 8px;\n"
                                         "      background: #CBB1A0;\n"
                                         "      selection-background-color: darkgray;\n"
                                         "}")
        self.input_book_id.setInputMask("")
        self.input_book_id.setMaxLength(10)
        self.input_book_id.setObjectName("input_book_id")
        self.book_verticalLayout.addWidget(self.input_book_id)
        self.line_2 = QtWidgets.QFrame(self.border)
        self.line_2.setStyleSheet("border: 2px solid #842a2d;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.book_verticalLayout.addWidget(self.line_2)
        self.book_search_button = QtWidgets.QPushButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.book_search_button.setFont(font)
        self.book_search_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.book_search_button.setStyleSheet("QPushButton{\n"
                                              "    color: #842a2d;\n"
                                              "    font: 12pt \"Franklin Gothic Book\" bold;\n"
                                              "    border: 2px solid #842a2d;\n"
                                              "    padding: 2px 53px;\n"
                                              "    border-radius: 10px;\n"
                                              "    opacity: 100;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "    background-color: #842a2d;\n"
                                              "    color: #CBB1A0;\n"
                                              "}")
        self.book_search_button.setObjectName("book_search_button")
        self.book_verticalLayout.addWidget(self.book_search_button)
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
                                             "}")
        self.book_reset_button.setObjectName("book_reset_button")
        self.book_verticalLayout.addWidget(self.book_reset_button)
        self.book_form.setLayout(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.book_verticalLayout)
        self.book_tableWidget = QtWidgets.QTableWidget(self.border)
        self.book_tableWidget.setObjectName("book_tableWidget")
        self.book_tableWidget.setColumnCount(6)
        self.book_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.book_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.book_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.book_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.book_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.book_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.book_tableWidget.setHorizontalHeaderItem(5, item)
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
        self.borrow_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
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
        self.input_borrow_id = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.input_borrow_id.setFont(font)
        self.input_borrow_id.setStyleSheet("QLineEdit {\n"
                                           "      color: #000000;\n"
                                           "      font: 11pt \"Verdana\";\n"
                                           "      border: None;\n"
                                           "      border-bottom-color: white;\n"
                                           "      border-radius: 10px;\n"
                                           "      padding: 0 8px;\n"
                                           "      background: #CBB1A0;\n"
                                           "      selection-background-color: darkgray;\n"
                                           "}")
        self.input_borrow_id.setInputMask("")
        self.input_borrow_id.setMaxLength(12)
        self.input_borrow_id.setObjectName("input_borrow_id")
        self.borrow_verticalLayout.addWidget(self.input_borrow_id)
        self.line_3 = QtWidgets.QFrame(self.border)
        self.line_3.setStyleSheet("border: 2px solid #842a2d;")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.borrow_verticalLayout.addWidget(self.line_3)
        self.borrow_search_button = QtWidgets.QPushButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.borrow_search_button.setFont(font)
        self.borrow_search_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.borrow_search_button.setStyleSheet("QPushButton{\n"
                                                "    color: #842a2d;\n"
                                                "    font: 12pt \"Franklin Gothic Book\" bold;\n"
                                                "    border: 2px solid #842a2d;\n"
                                                "    padding: 2px 53px;\n"
                                                "    border-radius: 10px;\n"
                                                "    opacity: 100;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "    background-color: #842a2d;\n"
                                                "    color: #CBB1A0;\n"
                                                "}")
        self.borrow_search_button.setObjectName("borrow_search_button")
        self.borrow_verticalLayout.addWidget(self.borrow_search_button)
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
                                               "}")
        self.borrow_reset_button.setObjectName("borrow_reset_button")
        self.borrow_verticalLayout.addWidget(self.borrow_reset_button)
        self.borrow_form.setLayout(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.borrow_verticalLayout)
        self.borrow_tableWidget = QtWidgets.QTableWidget(self.border)
        self.borrow_tableWidget.setObjectName("borrow_tableWidget")
        self.borrow_tableWidget.setColumnCount(8)
        self.borrow_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_tableWidget.setHorizontalHeaderItem(7, item)
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
                                       "}")
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(
            lambda: self.return_action(SearchHistory, MainMenu))
        self.below.addWidget(self.back_button)
        self.verticalLayout.addLayout(self.below)
        self.verticalLayout_2.addWidget(self.border)
        self.retranslateUi(SearchHistory)
        QtCore.QMetaObject.connectSlotsByName(SearchHistory)

    def return_action(self, SearchHistory, MainMenu):
        SearchHistory.close()
        MainMenu.show()

    def retranslateUi(self, SearchHistory):
        _translate = QtCore.QCoreApplication.translate
        SearchHistory.setWindowTitle(_translate("SearchHistory", "Form"))
        self.title_name.setText(_translate("SearchHistory", "SEARCH HISTORY"))
        self.student_label.setText(_translate("SearchHistory", "STUDENT"))
        self.student_id_label.setText(
            _translate("SearchHistory", "Student ID:"))
        self.student_search_button.setText(
            _translate("SearchHistory", "SEARCH"))
        self.student_reset_button.setText(
            _translate("SearchHistory", "RESET STUDENT TABLE"))
        item = self.student_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SearchHistory", "Student ID"))
        item = self.student_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SearchHistory", "Student Name"))
        item = self.student_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SearchHistory", "Section"))
        item = self.student_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SearchHistory", "Year Level"))
        self.book_label.setText(_translate("SearchHistory", "BOOK"))
        self.book_id_label.setText(_translate("SearchHistory", "Book ID:"))
        self.input_book_id.setText(_translate("SearchHistory", "BOOK-"))
        self.book_search_button.setText(_translate("SearchHistory", "SEARCH"))
        self.book_reset_button.setText(
            _translate("SearchHistory", "RESET BOOK TABLE"))
        item = self.book_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SearchHistory", "Book ID"))
        item = self.book_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SearchHistory", "ISBN"))
        item = self.book_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SearchHistory", "Title"))
        item = self.book_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SearchHistory", "Author"))
        item = self.book_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SearchHistory", "Condition"))
        item = self.book_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SearchHistory", "Status"))
        self.borrow_label.setText(_translate("SearchHistory", "BORROW"))
        self.borrow_id_label.setText(_translate("SearchHistory", "Borrow ID:"))
        self.input_borrow_id.setText(_translate("SearchHistory", "BORROW-"))
        self.borrow_search_button.setText(
            _translate("SearchHistory", "SEARCH"))
        self.borrow_reset_button.setText(
            _translate("SearchHistory", "RESET BORROW TABLE"))
        item = self.borrow_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SearchHistory", "Borrow ID"))
        item = self.borrow_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SearchHistory", "Borrow Date"))
        item = self.borrow_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SearchHistory", "Return Date"))
        item = self.borrow_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SearchHistory", "Status"))
        item = self.borrow_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SearchHistory", "Overdue"))
        item = self.borrow_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SearchHistory", "Issuer"))
        item = self.borrow_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("SearchHistory", "Payment Amount"))
        item = self.borrow_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("SearchHistory", "Payment"))
        self.status_label.setText(_translate("SearchHistory", "placeholder"))
        self.back_button.setText(_translate("SearchHistory", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchHistory = QtWidgets.QWidget()
    ui = Ui_SearchHistory()
    ui.setupUi(SearchHistory)
    SearchHistory.show()
    sys.exit(app.exec())
