from PyQt6 import QtCore, QtGui, QtWidgets
import string
import random
import sqlite3


class Ui_BookInformation(object):
    def setupUi(self, BookInformation, MainMenu):
        MainMenu.close()
        BookInformation.setObjectName("BookInformation")
        BookInformation.resize(670, 425)
        BookInformation.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        BookInformation.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(BookInformation)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.border = QtWidgets.QFrame(BookInformation)
        self.border.setStyleSheet("#border{\n"
                                  "    color: \"#842a2d\";\n"
                                  "}")
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.border.setLineWidth(5)
        self.border.setObjectName("border")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.border)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_title = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rb_addbook = QtWidgets.QRadioButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.rb_addbook.setFont(font)
        self.rb_addbook.setObjectName("rb_addbook")
        self.rb_addbook.toggled.connect(self.rb_addbook_toggled)
        self.horizontalLayout.addWidget(self.rb_addbook)
        spacerItem1 = QtWidgets.QSpacerItem(
            13, 40, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.rb_editbook = QtWidgets.QRadioButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.rb_editbook.setFont(font)
        self.rb_editbook.setObjectName("rb_editbook")
        self.rb_editbook.toggled.connect(self.rb_editbook_toggled)
        self.horizontalLayout.addWidget(self.rb_editbook)
        spacerItem2 = QtWidgets.QSpacerItem(
            13, 40, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.rb_deletebook = QtWidgets.QRadioButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.rb_deletebook.setFont(font)
        self.rb_deletebook.setObjectName("rb_deletebook")
        self.rb_deletebook.toggled.connect(self.rb_deletebook_toggled)
        self.horizontalLayout.addWidget(self.rb_deletebook)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(self.border)
        self.line.setStyleSheet("border: 2px solid #842a2d;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input_search = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.input_search.setFont(font)
        self.input_search.setStyleSheet("QLineEdit {\n"
                                        "      color: #000000;\n"
                                        "      font: 12pt \"Verdana\";\n"
                                        "      border: None;\n"
                                        "      border-bottom-color: white;\n"
                                        "      border-radius: 10px;\n"
                                        "      padding: 0 8px;\n"
                                        "      background: #CBB1A0;\n"
                                        "      selection-background-color: darkgray;\n"
                                        "}")
        self.input_search.setObjectName("input_search")
        self.gridLayout_2.addWidget(self.input_search, 0, 1, 1, 1)
        self.search_label = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.search_label.setFont(font)
        self.search_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                       QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.search_label.setObjectName("search_label")
        self.gridLayout_2.addWidget(self.search_label, 0, 0, 1, 1)
        self.search_button = QtWidgets.QPushButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        self.search_button.setFont(font)
        self.search_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.search_button.setStyleSheet("QPushButton{\n"
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
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(self.search_button_clicked)
        self.gridLayout_2.addWidget(self.search_button, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.line_2 = QtWidgets.QFrame(self.border)
        self.line_2.setStyleSheet("border: 2px solid #842a2d;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line_4 = QtWidgets.QFrame(self.border)
        self.line_4.setStyleSheet("border: 2px solid #842a2d;")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 3, 0, 1, 2)
        self.label_ISBN = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_ISBN.setFont(font)
        self.label_ISBN.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                     QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_ISBN.setObjectName("label_ISBN")
        self.gridLayout.addWidget(self.label_ISBN, 2, 0, 1, 1)
        self.input_condition = QtWidgets.QComboBox(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.input_condition.setFont(font)
        self.input_condition.setStyleSheet("font: 12pt \"Verdana\"")
        self.input_condition.setInsertPolicy(
            QtWidgets.QComboBox.InsertPolicy.InsertAfterCurrent)
        self.input_condition.setObjectName("input_condition")
        self.input_condition.addItem("<choose condition>")
        self.input_condition.addItem("New")
        self.input_condition.addItem("Fine")
        self.input_condition.addItem("Good")
        self.input_condition.addItem("Fair")
        self.input_condition.addItem("Poor")
        self.gridLayout.addWidget(self.input_condition, 8, 1, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.border)
        self.line_9.setStyleSheet("border: 2px solid #842a2d;")
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 9, 0, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.border)
        self.line_5.setStyleSheet("border: 2px solid #842a2d;")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 1, 0, 1, 2)
        self.line_8 = QtWidgets.QFrame(self.border)
        self.line_8.setStyleSheet("border: 2px solid #842a2d;")
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 7, 0, 1, 2)
        self.label_author = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_author.setFont(font)
        self.label_author.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                       QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_author.setObjectName("label_author")
        self.gridLayout.addWidget(self.label_author, 6, 0, 1, 1)
        self.label_Title = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                      QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Title.setObjectName("label_Title")
        self.gridLayout.addWidget(self.label_Title, 4, 0, 1, 1)
        self.input_author = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.input_author.setFont(font)
        self.input_author.setStyleSheet("QLineEdit {\n"
                                        "      color: #000000;\n"
                                        "      font: 12pt \"Verdana\";\n"
                                        "      border: None;\n"
                                        "      border-bottom-color: white;\n"
                                        "      border-radius: 10px;\n"
                                        "      padding: 0 8px;\n"
                                        "      background: #CBB1A0;\n"
                                        "      selection-background-color: darkgray;\n"
                                        "}")
        self.input_author.setObjectName("input_author")
        self.gridLayout.addWidget(self.input_author, 6, 1, 1, 1)
        self.input_ISBN = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.input_ISBN.setFont(font)
        self.input_ISBN.setStyleSheet("QLineEdit {\n"
                                      "      color: #000000;\n"
                                      "      font: 12pt \"Verdana\";\n"
                                      "      border: None;\n"
                                      "      border-bottom-color: white;\n"
                                      "      border-radius: 10px;\n"
                                      "      padding: 0 8px;\n"
                                      "      background: #CBB1A0;\n"
                                      "      selection-background-color: darkgray;\n"
                                      "}")
        self.input_ISBN.setObjectName("input_ISBN")
        self.gridLayout.addWidget(self.input_ISBN, 2, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.border)
        self.line_6.setStyleSheet("border: 2px solid #842a2d;")
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 5, 0, 1, 2)
        self.label_bookid = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_bookid.setFont(font)
        self.label_bookid.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                       QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_bookid.setObjectName("label_bookid")
        self.gridLayout.addWidget(self.label_bookid, 0, 0, 1, 1)
        self.input_title = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.input_title.setFont(font)
        self.input_title.setStyleSheet("QLineEdit {\n"
                                       "      color: #000000;\n"
                                       "      font: 12pt \"Verdana\";\n"
                                       "      border: None;\n"
                                       "      border-bottom-color: white;\n"
                                       "      border-radius: 10px;\n"
                                       "      padding: 0 8px;\n"
                                       "      background: #CBB1A0;\n"
                                       "      selection-background-color: darkgray;\n"
                                       "}")
        self.input_title.setObjectName("input_title")
        self.gridLayout.addWidget(self.input_title, 4, 1, 1, 1)
        self.input_bookid = QtWidgets.QLineEdit(self.border)
        self.input_bookid.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        self.input_bookid.setFont(font)
        self.input_bookid.setStyleSheet("QLineEdit {\n"
                                        "      color: #000000;\n"
                                        "      border: None;\n"
                                        "      border-bottom-color: white;\n"
                                        "      border-radius: 10px;\n"
                                        "      padding: 0 8px;\n"
                                        "      background: #CBB1A0;\n"
                                        "      selection-background-color: darkgray;\n"
                                        "}")
        self.input_bookid.setInputMask("")
        self.input_bookid.setText("")
        self.input_bookid.setObjectName("input_bookid")
        self.input_bookid.clear()
        self.gridLayout.addWidget(self.input_bookid, 0, 1, 1, 1)
        self.label_condition = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_condition.setFont(font)
        self.label_condition.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                          QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_condition.setObjectName("label_condition")
        self.gridLayout.addWidget(self.label_condition, 8, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.confirm_button = QtWidgets.QPushButton(self.border)
        self.confirm_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.confirm_button.setStyleSheet("QPushButton{\n"
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
        self.confirm_button.setObjectName("confirm_button")
        self.confirm_button.clicked.connect(self.confirm_btn_clicked)
        self.horizontalLayout_3.addWidget(self.confirm_button)
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
            lambda: self.cancel_btn_clicked(BookInformation, MainMenu))
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.border)
        # * defaults to add
        self.rb_addbook.setChecked(True)

        self.retranslateUi(BookInformation)
        QtCore.QMetaObject.connectSlotsByName(BookInformation)

    def cancel_btn_clicked(self, BookInformation, MainMenu):
        BookInformation.close()
        MainMenu.show()

    def rb_addbook_toggled(self):
        self.search_button.setDisabled(True)
        self.input_bookid.setText(
            "BOOK-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
        self.input_search.clear()
        self.input_search.setReadOnly(True)
        self.input_ISBN.clear()
        self.input_title.clear()
        self.input_author.clear()
        self.input_condition.setCurrentIndex(0)

    def rb_editbook_toggled(self):
        self.clear_inpfields_search()

    def rb_deletebook_toggled(self):
        self.clear_inpfields_search()

    def confirm_btn_clicked(self):
        book_ID = self.input_bookid.text()
        ISBN = self.input_ISBN.text()
        Title = self.input_title.text()
        Author = self.input_author.text()
        Book_cond = self.input_condition.itemText(
            self.input_condition.currentIndex())
        book_stat = "Available"

        if (len(ISBN) == 0 or len(Title) == 0 or len(Author) == 0):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText("There are remaining empty input field/s!")
            msg.setWindowTitle("Incomplete information")
            msg.exec()
        elif (Book_cond == "<choose condition>"):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText("Choose a book condition!")
            msg.setWindowTitle("Incomplete information")
            msg.exec()
        else:
            self.manipulate_the_data(
                book_ID, ISBN, Title, Author, Book_cond, book_stat)

    def manipulate_the_data(self, book_ID, ISBN, Title, Author, Book_cond, book_stat):
        if (self.rb_addbook.isChecked() == True):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
            msg.setText("Are you sure to save current Book Information?")
            msg.setInformativeText(
                f"Issued ID:  {book_ID}\nISBN:  {ISBN}\nTitle:  {Title}\nAuthor:  {Author}\nBook Condition:  {Book_cond}")
            msg.setWindowTitle("Book Information Confirmation")
            msg.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            result = msg.exec()

            if (result == QtWidgets.QMessageBox.StandardButton.Yes):
                con = sqlite3.connect('./db/test.db')
                query = "INSERT INTO BOOK VALUES (?,?,?,?,?,?);"
                cur = con.cursor()
                interpolate_data = [book_ID, ISBN,
                                    Title, Author, Book_cond, book_stat]
                cur.execute(query, interpolate_data)
                con.commit()
                con.close()
                self.informative_message(
                    text="Data Added Successfully!",
                    subtext="Thank You for adding books to our Library!",
                    window_title="Added Successfully"
                )
                self.rb_addbook_toggled()

            elif (result == QtWidgets.QMessageBox.StandardButton.No):
                pass
        elif (self.rb_editbook.isChecked() == True):
            self.update_data_values(
                book_ID=book_ID, ISBN=ISBN, Title=Title, Author=Author, Book_cond=Book_cond)
        elif (self.rb_deletebook.isChecked() == True):
            self.delete_data_values(
                book_ID=book_ID, ISBN=ISBN, Title=Title, Author=Author, Book_cond=Book_cond)

    def search_button_clicked(self):
        searched_book_id = self.input_search.text()
        con = sqlite3.connect('./db/test.db')
        query = "SELECT Book_ID, Book_ISBN, Book_Title, Book_Author, Book_Condition FROM BOOK;"
        result = [form[1] for form in list(enumerate(con.execute(query)))]
        book_ids = [each_data[0] for each_data in result]
        if searched_book_id in book_ids:
            data_to_populate = [
                each_data for each_data in result if each_data[0] == searched_book_id][0]
            self.populate_data(book_ID=data_to_populate[0], ISBN=data_to_populate[1], Title=data_to_populate[2],
                               Author=data_to_populate[3], Book_cond=data_to_populate[4])
        else:
            self.informative_message(
                text="Entered ID was not found in the database!",
                subtext="Check for typographical errors or else, data doesn't exist in the database at all.",
                window_title="Book ID Not Found"
            )

    def update_data_values(self, book_ID, ISBN, Title, Author, Book_cond):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        msg.setText(f"Are you sure to save changes to {book_ID}?")
        msg.setInformativeText(
            f"ISBN:  {ISBN}\nTitle:  {Title}\nAuthor:  {Author}\nBook Condition:  {Book_cond}")
        msg.setWindowTitle("Edited Book Information Confirmation")
        msg.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        result = msg.exec()
        if (result == QtWidgets.QMessageBox.StandardButton.Yes):
            con = sqlite3.connect('./db/test.db')
            query = """
                UPDATE BOOK
                SET Book_ISBN = ?, Book_Title = ?, Book_Author = ?, Book_Condition = ?
                WHERE Book_ID = ?;
                    """
            cur = con.cursor()
            interpolate_data = [ISBN, Title, Author, Book_cond, book_ID]
            cur.execute(query, interpolate_data)
            con.commit()
            con.close()
            self.informative_message(
                text="Data Updated Successfully!",
                subtext='"Everyone makes mistakes. Everyone deserves a second chance.” - Mo’ne Davis',
                window_title="Update Successful"
            )
            self.clear_inpfields_search()
        elif (result == QtWidgets.QMessageBox.StandardButton.No):
            pass

    def delete_data_values(self, book_ID, ISBN, Title, Author, Book_cond):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        msg.setText(
            f"Are you sure to delete {book_ID}? It will be gone forever...")
        msg.setInformativeText(
            f"ISBN:\t{ISBN}\nTitle:\t{Title}\nAuthor:\t{Author}\nBook Condition:\t{Book_cond}")
        msg.setWindowTitle("DELETE Book Information Confirmation")
        msg.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        result = msg.exec()
        if (result == QtWidgets.QMessageBox.StandardButton.Yes):
            con = sqlite3.connect('./db/test.db')
            query = "DELETE FROM BOOK WHERE Book_ID = ?;"
            cur = con.cursor()
            interpolate_data = [book_ID]
            cur.execute(query, interpolate_data)
            con.commit()
            con.close()
            self.informative_message(
                text="Information has been deleted.",
                subtext=""""Be wise today so you don't cry tomorrow”  - E.A. Bucchianeri""",
                window_title="Deletion Completed"
            )
            self.clear_inpfields_search()
        elif (result == QtWidgets.QMessageBox.StandardButton.No):
            pass

    def clear_inpfields_search(self):
        self.search_button.setEnabled(True)
        self.input_search.setReadOnly(False)
        self.input_bookid.clear()
        self.input_ISBN.clear()
        self.input_title.clear()
        self.input_author.clear()
        self.input_condition.setCurrentIndex(0)

    def populate_data(self, book_ID, ISBN, Title, Author, Book_cond):
        self.input_bookid.setText(book_ID)
        self.input_ISBN.setText(ISBN)
        self.input_title.setText(Title)
        self.input_author.setText(Author)
        if (Book_cond == "New"):
            Book_cond = 1
        elif (Book_cond == "Fine"):
            Book_cond = 2
        elif (Book_cond == "Good"):
            Book_cond = 3
        elif (Book_cond == "Fair"):
            Book_cond = 4
        elif (Book_cond == "Poor"):
            Book_cond = 5
        self.input_condition.setCurrentIndex(Book_cond)

    def informative_message(self, text, subtext, window_title):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(text)
        msg.setInformativeText(subtext)
        msg.setWindowTitle(window_title)
        msg.exec()

    def retranslateUi(self, BookInformation):
        _translate = QtCore.QCoreApplication.translate
        BookInformation.setWindowTitle(_translate(
            "BookInformation", "Book Information"))
        self.label_title.setText(_translate(
            "BookInformation", "BOOK INFORMATION"))
        self.rb_addbook.setText(_translate("BookInformation", "Add"))
        self.rb_editbook.setText(_translate("BookInformation", "Edit"))
        self.rb_deletebook.setText(_translate("BookInformation", "Delete"))
        self.search_label.setText(_translate("BookInformation", "Search ID:"))
        self.search_button.setText(_translate(
            "BookInformation", "    Search   "))
        self.label_ISBN.setText(_translate("BookInformation", "ISBN:"))
        self.input_condition.setPlaceholderText(
            _translate("BookInformation", "<choose condition>"))
        self.label_author.setText(_translate("BookInformation", "Author:"))
        self.label_Title.setText(_translate("BookInformation", "Title:"))
        self.label_bookid.setText(_translate("BookInformation", "ID Issued:"))
        self.input_bookid.setPlaceholderText(
            _translate("BookInformation", "BOOK-XXXXX"))
        self.label_condition.setText(
            _translate("BookInformation", "Condition:"))
        self.confirm_button.setText(_translate("BookInformation", "Confirm"))
        self.cancel_button.setText(_translate("BookInformation", "Cancel"))
