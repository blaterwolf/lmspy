from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_StudentInformation(object):
    def setupUi(self, StudentInformation, MainMenu):
        StudentInformation.setObjectName("StudentInformation")
        StudentInformation.resize(670, 440)
        StudentInformation.setStyleSheet(
            ".QWidget{background-color: #CBB1A0;border-radius: 10px}")
        StudentInformation.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(StudentInformation)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.border = QtWidgets.QFrame(StudentInformation)
        self.border.setStyleSheet("#border{\n"
                                  "    color: #842a2d;\n"
                                  "}")
        self.border.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.border.setLineWidth(5)
        self.border.setMidLineWidth(5)
        self.border.setObjectName("border")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.border)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line_2 = QtWidgets.QFrame(self.border)
        self.line_2.setStyleSheet("border: 2px solid #842a2d;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            17, 27, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
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
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.rb_add_student = QtWidgets.QRadioButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.rb_add_student.setFont(font)
        self.rb_add_student.setObjectName("rb_add_student")
        self.horizontalLayout.addWidget(self.rb_add_student)
        spacerItem3 = QtWidgets.QSpacerItem(
            13, 40, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.rb_edit_student = QtWidgets.QRadioButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.rb_edit_student.setFont(font)
        self.rb_edit_student.setObjectName("rb_edit_student")
        self.horizontalLayout.addWidget(self.rb_edit_student)
        spacerItem4 = QtWidgets.QSpacerItem(
            13, 40, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.rb_delete_student = QtWidgets.QRadioButton(self.border)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.rb_delete_student.setFont(font)
        self.rb_delete_student.setObjectName("rb_delete_student")
        self.horizontalLayout.addWidget(self.rb_delete_student)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
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
        self.input_search.setClearButtonEnabled(True)
        self.input_search.setMaxLength(12)
        self.input_search.setObjectName("input_search")
        self.gridLayout_2.addWidget(self.input_search, 1, 1, 1, 1)
        self.label_search_student_id = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_search_student_id.setFont(font)
        self.label_search_student_id.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_search_student_id.setObjectName("label_search_student_id")
        self.gridLayout_2.addWidget(self.label_search_student_id, 1, 0, 1, 1)
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
        self.search_button.clicked.connect(self.search_student)
        self.gridLayout_2.addWidget(self.search_button, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 4, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            17, 27, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 6, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(
            17, 27, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(
            17, 27, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 13, 0, 1, 1)
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
        self.confirm_button.clicked.connect(lambda: self.validate_rb_state(
            add_button=self.rb_add_student,
            edit_button=self.rb_edit_student,
            delete_button=self.rb_delete_student,
            student_id=self.input_student_id.text(),
            firstname=self.input_firstname.text(),
            lastname=self.input_lastname.text(),
            section=self.input_section.text(),
            grade_level=self.input_cb_grade_level.currentText(),
        ))
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
            lambda: self.return_action(StudentInformation, MainMenu))
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 14, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_student_id = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_student_id.setFont(font)
        self.label_student_id.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_student_id.setObjectName("label_student_id")
        self.gridLayout.addWidget(self.label_student_id, 0, 0, 1, 1)
        self.input_student_id = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.input_student_id.setFont(font)
        self.input_student_id.setMaxLength(12)
        self.input_student_id.setStyleSheet("QLineEdit {\n"
                                            "      color: #000000;\n"
                                            "      font: 12pt \"Verdana\";\n"
                                            "      border: None;\n"
                                            "      border-bottom-color: white;\n"
                                            "      border-radius: 10px;\n"
                                            "      padding: 0 8px;\n"
                                            "      background: #CBB1A0;\n"
                                            "      selection-background-color: darkgray;\n"
                                            "}")
        self.input_student_id.setClearButtonEnabled(True)
        self.input_student_id.setObjectName("input_student_id")
        self.gridLayout.addWidget(self.input_student_id, 0, 1, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.border)
        self.line_5.setStyleSheet("border: 2px solid #842a2d;")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 1, 0, 1, 3)
        self.label_firstname = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_firstname.setFont(font)
        self.label_firstname.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                          QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_firstname.setObjectName("label_firstname")
        self.gridLayout.addWidget(self.label_firstname, 2, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.border)
        self.line_4.setStyleSheet("border: 2px solid #842a2d;")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 3, 0, 1, 3)
        self.label_lastname = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_lastname.setFont(font)
        self.label_lastname.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                         QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_lastname.setObjectName("label_lastname")
        self.gridLayout.addWidget(self.label_lastname, 4, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.border)
        self.line_6.setStyleSheet("border: 2px solid #842a2d;")
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 5, 0, 1, 3)
        self.label_section = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_section.setFont(font)
        self.label_section.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                        QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_section.setObjectName("label_section")
        self.gridLayout.addWidget(self.label_section, 6, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.border)
        self.line_8.setStyleSheet("border: 2px solid #842a2d;")
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 7, 0, 1, 3)
        self.label_gradeLevel = QtWidgets.QLabel(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_gradeLevel.setFont(font)
        self.label_gradeLevel.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_gradeLevel.setObjectName("label_gradeLevel")
        self.gridLayout.addWidget(self.label_gradeLevel, 8, 0, 1, 1)
        self.input_firstname = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.input_firstname.setFont(font)
        self.input_firstname.setMaxLength(30)
        self.input_firstname.setStyleSheet("QLineEdit {\n"
                                           "      color: #000000;\n"
                                           "      font: 12pt \"Verdana\";\n"
                                           "      border: None;\n"
                                           "      border-bottom-color: white;\n"
                                           "      border-radius: 10px;\n"
                                           "      padding: 0 8px;\n"
                                           "      background: #CBB1A0;\n"
                                           "      selection-background-color: darkgray;\n"
                                           "}")
        self.input_firstname.setClearButtonEnabled(True)
        self.input_firstname.setObjectName("input_firstname")
        self.gridLayout.addWidget(self.input_firstname, 2, 1, 1, 2)
        self.input_lastname = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.input_lastname.setFont(font)
        self.input_lastname.setMaxLength(30)
        self.input_lastname.setStyleSheet("QLineEdit {\n"
                                          "      color: #000000;\n"
                                          "      font: 12pt \"Verdana\";\n"
                                          "      border: None;\n"
                                          "      border-bottom-color: white;\n"
                                          "      border-radius: 10px;\n"
                                          "      padding: 0 8px;\n"
                                          "      background: #CBB1A0;\n"
                                          "      selection-background-color: darkgray;\n"
                                          "}")
        self.input_lastname.setClearButtonEnabled(True)
        self.input_lastname.setObjectName("input_lastname")
        self.gridLayout.addWidget(self.input_lastname, 4, 1, 1, 2)
        self.input_section = QtWidgets.QLineEdit(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.input_section.setFont(font)
        self.input_section.setMaxLength(15)
        self.input_section.setStyleSheet("QLineEdit {\n"
                                         "      color: #000000;\n"
                                         "      font: 12pt \"Verdana\";\n"
                                         "      border: None;\n"
                                         "      border-bottom-color: white;\n"
                                         "      border-radius: 10px;\n"
                                         "      padding: 0 8px;\n"
                                         "      background: #CBB1A0;\n"
                                         "      selection-background-color: darkgray;\n"
                                         "}")
        self.input_section.setClearButtonEnabled(True)
        self.input_section.setObjectName("input_section")
        self.gridLayout.addWidget(self.input_section, 6, 1, 1, 2)
        self.input_cb_grade_level = QtWidgets.QComboBox(self.border)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.input_cb_grade_level.setFont(font)
        self.input_cb_grade_level.setStyleSheet("font: 12pt \"Verdana\"")
        self.input_cb_grade_level.setInsertPolicy(
            QtWidgets.QComboBox.InsertPolicy.InsertAfterCurrent)
        self.input_cb_grade_level.setPlaceholderText("")
        self.input_cb_grade_level.setObjectName("input_cb_grade_level")
        self.input_cb_grade_level.addItem("")
        self.input_cb_grade_level.addItem("")
        self.input_cb_grade_level.addItem("")
        self.input_cb_grade_level.addItem("")
        self.input_cb_grade_level.addItem("")
        self.input_cb_grade_level.addItem("")
        self.gridLayout.addWidget(self.input_cb_grade_level, 8, 1, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout, 7, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.border)
        self.line_9.setStyleSheet("border: 2px solid #842a2d;")
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_3.addWidget(self.line_9, 11, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.border)
        self.line.setStyleSheet("border: 2px solid #842a2d;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 1)
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
        self.gridLayout_3.addWidget(self.status_label, 12, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.border)
        self.retranslateUi(StudentInformation)
        QtCore.QMetaObject.connectSlotsByName(StudentInformation)
        # * defaults to add + listen to toggle changes
        self.rb_add_student.setChecked(True)
        self.input_search.setEnabled(False)
        self.search_button.setEnabled(False)
        self.confirm_button.setText("Add Student")
        self.rb_add_student.toggled.connect(
            lambda: self.change_radio_button_state(self.rb_add_student))
        self.rb_edit_student.toggled.connect(
            lambda: self.change_radio_button_state(self.rb_edit_student))
        self.rb_delete_student.toggled.connect(
            lambda: self.change_radio_button_state(self.rb_delete_student))

    def return_action(self, StudentInformation, MainMenu):
        StudentInformation.close()
        MainMenu.show()

    def change_radio_button_state(self, button_to_change):
        if (button_to_change.text() == "Add"):
            self.input_search.setEnabled(False)
            self.search_button.setEnabled(False)
            self.enable_inputs()
            self.clear_data_on_inputs()
            self.confirm_button.setText("Add Student")
        else:
            self.input_search.setEnabled(True)
            self.search_button.setEnabled(True)
            self.disable_inputs()
            self.clear_data_on_inputs()
            if (button_to_change.text() == "Edit"):
                self.confirm_button.setText("Edit Student")
            else:
                self.confirm_button.setText("Delete Student")

    def clear_data_on_inputs(self):
        self.status_label.setText("")
        self.input_student_id.clear()
        self.input_firstname.clear()
        self.input_lastname.clear()
        self.input_section.clear()
        self.input_search.clear()
        self.input_cb_grade_level.setCurrentText("Grade 7")
        self.status_label.clear()

    def enable_inputs(self):
        self.input_student_id.setEnabled(True)
        self.input_firstname.setEnabled(True)
        self.input_lastname.setEnabled(True)
        self.input_section.setEnabled(True)
        self.input_cb_grade_level.setEnabled(True)

    def disable_inputs(self):
        self.input_student_id.setDisabled(True)
        self.input_firstname.setDisabled(True)
        self.input_lastname.setDisabled(True)
        self.input_section.setDisabled(True)
        self.input_cb_grade_level.setDisabled(True)

    def search_student(self):
        search_value = self.input_search.text()
        # * initialize sqlite
        con = sqlite3.connect('./db/test.db')
        cur = con.cursor()
        # * check if student_id exists
        check_id_query = "SELECT * FROM STUDENT WHERE Student_ID = ?;"
        interpolate_data = [search_value]
        result = cur.execute(check_id_query, interpolate_data)
        student_data = [form[1] for form in list(enumerate(result))]
        if student_data:
            self.status_label.setText("")
            student_data = student_data[0]
            self.populate_data(student_data)
            self.enable_inputs()
            self.input_student_id.setEnabled(False)
            if (self.rb_delete_student.isChecked()):
                self.disable_inputs()
                self.status_label.setText(
                    "NOTE: Clicking the Delete Student button deletes the data immediately.")
        else:
            self.clear_data_on_inputs()
            self.status_label.setText(
                "This student does not exist in the database!")
            self.disable_inputs()

    def populate_data(self, data):
        student_id = data[0]
        last_name = data[1]
        first_name = data[2]
        section = data[3]
        grade_level = data[4]
        self.input_student_id.setText(student_id)
        self.input_firstname.setText(first_name)
        self.input_lastname.setText(last_name)
        self.input_section.setText(section)
        self.input_cb_grade_level.setCurrentText(grade_level)

    def validate_rb_state(self, add_button, edit_button, delete_button, student_id, firstname, lastname, section, grade_level):
        if (add_button.isChecked()):
            self.validate_data_to_add(
                student_id, firstname, lastname, section, grade_level)
        if (edit_button.isChecked()):
            self.update_student_data(
                student_id, firstname, lastname, section, grade_level)
        if (delete_button.isChecked()):
            self.delete_student_data(student_id)

    def validate_data_to_add(self, student_id, firstname, lastname, section, grade_level):
        if (len(student_id) == 0 or len(firstname) == 0 or len(lastname) == 0 or len(section) == 0):
            self.status_label.setText("Invalid field/s are empty! ")
        else:
            # * check if this student ID already exists in the database.
            con = sqlite3.connect('./db/test.db')
            query = "SELECT Student_ID FROM STUDENT;"
            result = [form[1][0]
                      for form in list(enumerate(con.execute(query)))]
            if student_id in result:
                self.status_label.setText("This student already exists!")
            else:
                self.status_label.setText("")
                self.insert_student_data(student_id, firstname,
                                         lastname, section, grade_level)

    def insert_student_data(self, student_id, firstname, lastname, section, grade_level):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(
            "You'll be inserting the following information in the database: ")
        msg.setInformativeText(
            f"Student ID:\t\t{student_id}\nFirstname:\t\t{firstname}\nLastname:\t\t{lastname}\nSection:\t\t\t{section}\nGrade Level:\t\t{grade_level}\n\nYour Student ID will be permanent and cannot be changed.\nAre you sure?")
        msg.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        msg.setWindowTitle("Confirmation Check")
        result = msg.exec()
        if (result == QtWidgets.QMessageBox.StandardButton.Yes):
            con = sqlite3.connect('./db/test.db')
            query = "INSERT INTO STUDENT VALUES (?,?,?,?,?);"
            cur = con.cursor()
            interpolate_data = [student_id, lastname,
                                firstname, section, grade_level]
            cur.execute(query, interpolate_data)
            con.commit()
            con.close()
            self.informative_message(
                text="Data Added Successfully!",
                subtext="You can still add data after this message.",
                window_title="Added Successfully",
                icon_type="information"
            )
            self.clear_data_on_inputs()
        elif (result == QtWidgets.QMessageBox.StandardButton.No):
            pass

    def update_student_data(self, student_id, firstname, lastname, section, grade_level):
        if (len(firstname) == 0 or len(lastname) == 0 or len(section) == 0):
            self.status_label.setText(
                "There are remaining empty input field/s!")
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText(
                f"Are you sure to save changes to {student_id}?")
            msg.setInformativeText(
                f"Firstname:\t{firstname}\nLastname:\t{lastname}\nSection:\t\t{section}\nGrade Level:\t{grade_level}\n\nAre you sure?")
            msg.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            msg.setWindowTitle("Edited Student Information Confirmation")
            result = msg.exec()
            if (result == QtWidgets.QMessageBox.StandardButton.Yes):
                con = sqlite3.connect('./db/test.db')
                query_update = """
                UPDATE STUDENT 
                SET Student_LastName = ?, Student_FirstName = ?, Student_Section = ?, Student_YearLevel = ?
                WHERE Student_ID  = ?;
                """
                cur = con.cursor()
                interpolate_data = [lastname, firstname,
                                    section, grade_level, student_id]
                cur.execute(query_update, interpolate_data)
                con.commit()
                con.close()
                self.informative_message(
                    text="Data Updated Successfully!",
                    subtext='"Everyone makes mistakes. Everyone deserves a second chance.” - Mo’ne Davis',
                    window_title="Updated Successfully",
                    icon_type="information"
                )
                self.disable_inputs()
                self.clear_data_on_inputs()
            elif (result == QtWidgets.QMessageBox.StandardButton.No):
                pass

    def delete_student_data(self, student_id):
        # * Step 1: Initialize Database
        con = sqlite3.connect('./db/test.db')
        cur = con.cursor()
        # * Step 2: Query the data to be deleted
        query_delete = """
        DELETE FROM STUDENT
        WHERE Student_ID = ?;
        """
        interpolate_data = [student_id]
        # * Step 3: Execute, Commit, Close
        cur.execute(query_delete, interpolate_data)
        con.commit()
        con.close()
        self.informative_message(
            text="Data Deleted Successfully!",
            subtext="You can still delete data after this message.",
            window_title="Deleted Successfully",
            icon_type="information"
        )
        self.disable_inputs()
        self.clear_data_on_inputs()

    def informative_message(self, text, subtext, window_title, icon_type="critical"):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        if icon_type == "information":
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(text)
        msg.setInformativeText(subtext)
        msg.setWindowTitle(window_title)
        msg.exec()

    def retranslateUi(self, StudentInformation):
        _translate = QtCore.QCoreApplication.translate
        StudentInformation.setWindowTitle(_translate(
            "StudentInformation", "Student Information"))
        self.label_title.setText(_translate(
            "StudentInformation", "STUDENT INFORMATION"))
        self.rb_add_student.setText(_translate("StudentInformation", "Add"))
        self.rb_edit_student.setText(_translate("StudentInformation", "Edit"))
        self.rb_delete_student.setText(
            _translate("StudentInformation", "Delete"))
        self.label_search_student_id.setText(_translate(
            "StudentInformation", "Search Student ID:"))
        self.search_button.setText(_translate(
            "StudentInformation", "  Search  "))
        self.confirm_button.setText(
            _translate("StudentInformation", "Confirm"))
        self.cancel_button.setText(_translate("StudentInformation", "Cancel"))
        self.label_student_id.setText(_translate(
            "StudentInformation", "Student ID Number: "))
        self.label_firstname.setText(_translate(
            "StudentInformation", "First Name: "))
        self.label_lastname.setText(_translate(
            "StudentInformation", "Last Name:"))
        self.label_section.setText(_translate(
            "StudentInformation", "Section: "))
        self.label_gradeLevel.setText(_translate(
            "StudentInformation", "Grade Level: "))
        self.input_cb_grade_level.setItemText(
            0, _translate("StudentInformation", "Grade 7"))
        self.input_cb_grade_level.setItemText(
            1, _translate("StudentInformation", "Grade 8"))
        self.input_cb_grade_level.setItemText(
            2, _translate("StudentInformation", "Grade 9"))
        self.input_cb_grade_level.setItemText(
            3, _translate("StudentInformation", "Grade 10"))
        self.input_cb_grade_level.setItemText(
            4, _translate("StudentInformation", "Grade 11"))
        self.input_cb_grade_level.setItemText(
            5, _translate("StudentInformation", "Grade 12"))
