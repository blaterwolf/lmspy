CREATE TABLE LIBRARIAN(
    Librarian_ID    INTEGER    PRIMARY KEY    AUTOINCREMENT    NOT NULL,
    Librarian_Name    VARCHAR(50)    NOT NULL,
    Librarian_Username    VARCHAR(15)    NOT NULL,
    Librarian_Password    VARCHAR(15)    NOT NULL
);

CREATE TABLE BOOK(
    Book_ID    INTEGER    PRIMARY KEY    AUTOINCREMENT    NOT NULL,
    Book_ISBN    VARCHAR(13)    NOT NULL,
    Book_Title    VARCHAR(100)  NOT NULL,
    Book_Author    VARCHAR(30)    NOT NULL,
    Book_Condition    VARCHAR(4)    NOT NULL,
    Book_Status    VARCHAR(9)    NOT NULL
);

CREATE TABLE STUDENT(
    Student_ID    VARCHAR(12)    PRIMARY KEY    NOT NULL,
    Student_LastName    VARCHAR(30)    NOT NULL,
    Student_FirstName    VARCHAR(30)    NOT NULL,
    Student_Section    VARCHAR(15)    NOT NULL,
    Student_YearLevel    INTEGER    NOT NULL
);

CREATE TABLE PAYMENT(
    Payment_Number    INTEGER    PRIMARY KEY    AUTOINCREMENT    NOT NULL,
    Payment_Amount    INTEGER    NOT NULL,
    Payment_Status    VARCHAR(7)    NOT NULL,
    Payment_Date    DATE    NOT NULL
);

CREATE TABLE BORROW(
    Borrow_ID    INTEGER    PRIMARY KEY    AUTOINCREMENT    NOT NULL,
    Borrow_Date    DATE    NOT NULL,
    Borrow_Return_Date    DATE    NOT NULL,
    Borrow_Status    VARCHAR(8)    NOT NULL,
    Librarian_ID    INTEGER,
    Student_ID    INTEGER,
    Payment_Number    INTEGER,
    FOREIGN KEY(Librarian_ID) REFERENCES Librarian(Librarian_ID),
    FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID),
    FOREIGN KEY(Payment_Number) REFERENCES Payment(Payment_Number)
);