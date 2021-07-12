CREATE TABLE LIBRARIAN IF NOT EXISTS(
    Librarian_Username      PRIMARY KEY    VARCHAR(15)    NOT NULL,
    Librarian_Name    VARCHAR(50)    NOT NULL,
    Librarian_Password    VARCHAR(15)    NOT NULL
);

CREATE TABLE BOOK IF NOT EXISTS(
    Book_ID    VARCHAR(10)    PRIMARY KEY    NOT NULL,
    Book_ISBN    VARCHAR(13)    NOT NULL,
    Book_Title    VARCHAR(100)  NOT NULL,
    Book_Author    VARCHAR(30)    NOT NULL,
    Book_Condition    VARCHAR(4)    NOT NULL,
    Book_Status    VARCHAR(9)    NOT NULL
);

CREATE TABLE STUDENT IF NOT EXISTS(
    Student_ID    VARCHAR(12)    PRIMARY KEY    NOT NULL,
    Student_LastName    VARCHAR(30)    NOT NULL,
    Student_FirstName    VARCHAR(30)    NOT NULL,
    Student_Section    VARCHAR(15)    NOT NULL,
    Student_YearLevel    INTEGER    NOT NULL
);

CREATE TABLE PAYMENT IF NOT EXISTS(
    Payment_ID    VARCHAR(32)    PRIMARY KEY    NOT NULL,
    Payment_Amount    INTEGER    NOT NULL,
    Payment_Status    VARCHAR(7)    NOT NULL,
    Payment_Date    DATE    NOT NULL
);

CREATE TABLE BORROW IF NOT EXISTS(
    Borrow_ID    VARCHAR(12)    PRIMARY KEY    NOT NULL,
    Borrow_Date    DATE    NOT NULL,
    Borrow_Return_Date    DATE    NOT NULL,
    Borrow_Status    VARCHAR(8)    NOT NULL,
    Librarian_Username    VARCHAR(15),
    Student_ID    VARCHAR(12),
    Payment_ID    VARCHAR(32),
    Book_ID    VARCHAR(10),
    FOREIGN KEY(Librarian_Username) REFERENCES Librarian(Librarian_Username) ON UPDATE CASCADE,
    FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY(Payment_ID) REFERENCES Payment(Payment_ID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY(Book_ID) REFERENCES Book(Book_ID) ON UPDATE CASCADE ON DELETE SET NULL
);