CREATE TABLE LIBRARIAN (
    Librarian_Username    VARCHAR(15)    PRIMARY KEY NOT NULL,
    Librarian_Name    VARCHAR(50)    NOT NULL,
    Librarian_Password    VARCHAR(15)    NOT NULL
);

CREATE TABLE BOOK(
    Book_ID    VARCHAR(10)    PRIMARY KEY    NOT NULL,
    Book_ISBN    VARCHAR(13)    NOT NULL,
    Book_Title    VARCHAR(100)  NOT NULL,
    Book_Author    VARCHAR(30)    NOT NULL,
    Book_Condition    VARCHAR(4)    NOT NULL,
    Book_Status    VARCHAR(9)    NOT NULL
);

CREATE TABLE STUDENT (
    Student_ID    VARCHAR(12)    PRIMARY KEY    NOT NULL,
    Student_LastName    VARCHAR(30)    NOT NULL,
    Student_FirstName    VARCHAR(30)    NOT NULL,
    Student_Section    VARCHAR(15)    NOT NULL,
    Student_YearLevel    VARCHAR(8)    NOT NULL
);

CREATE TABLE PAYMENT (
    Payment_ID    VARCHAR(32)    PRIMARY KEY    NOT NULL,
    Payment_Amount    REAL    NOT NULL,
    Payment_Status    VARCHAR(7)    NOT NULL
);

CREATE TABLE BORROW (
    Borrow_ID    VARCHAR(12)    PRIMARY KEY    NOT NULL,
    Borrow_Date    DATE    NOT NULL,
    Borrow_Return_Date    DATE    NOT NULL,
    Borrow_Status    VARCHAR(8)    NOT NULL,
    Borrow_Overdue_Status INTEGER NOT NULL,
    Borrow_Issuer    VARCHAR(15),
    Student_ID    VARCHAR(12),
    Payment_ID    VARCHAR(32),
    Book_ID    VARCHAR(10),
    FOREIGN KEY(Borrow_Issuer) REFERENCES Librarian(Librarian_Username) ON UPDATE CASCADE,
    FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY(Payment_ID) REFERENCES Payment(Payment_ID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY(Book_ID) REFERENCES Book(Book_ID) ON UPDATE CASCADE ON DELETE SET NULL
);

-- * Important Queries
-- * NOTE: Question Marks are data to be Interpolated.

-- * SECTION 1: LOGIN/VALIDATION/SIGNUP/FORGOT_PASSWORD
-- >> 1. Check if username exists in LIBRARIAN
SELECT Librarian_Username FROM LIBRARIAN;
-- >> 2. Insert New Librarian to the Database. (add_librarian.py)
INSERT INTO LIBRARIAN VALUES (?,?,?);
-- >> 3. Check if username exists AND use username and fullname data to populate it to the input values.
SELECT Librarian_Username, Librarian_Name FROM LIBRARIAN;
-- >> 4. Update Librarian Information to the Database. (edit_librarian.py)
UPDATE LIBRARIAN
SET Librarian_Name = ?, Librarian_Password = ?
WHERE Librarian_Username = ?;
-- >> 5. Query the Username and Password to be used to login to the main menu.
SELECT Librarian_Username, Librarian_Password FROM LIBRARIAN;

-- * SECTION 2: MAIN_MENU (Evaluate Overdue)
-- >> 6. Query:
-- >> Borrow_ID (for updating borrow status),
-- >> Borrow_Date (for comparing the borrow_date and the date today),
-- >> Payment_ID (to later use for updating payment amount if found to be overdue)
-- >> to evaluate if the books currently borrowed are overdue or not.
SELECT Borrow_ID, Borrow_Date, Payment_ID
FROM BORROW
WHERE Borrow_Status = 'Borrowed';
-- >> 6.1. If overdue, update Payment_Amount in PAYMENT
UPDATE PAYMENT
SET Payment_Amount = ?
WHERE Payment_ID = ?;
-- >> 6.2 AND Borrow_Overdue_Status in BORROW:
UPDATE BORROW
SET Borrow_Overdue_Status = ?
WHERE Borrow_ID = ?;

-- * SECTION 3: BOOK_INFORMATION (Add/Edit/Delete)
-- >> 7. Check if Book_ID exists (for Edit/Delete search feature) (then use data gathered to populate data)
SELECT * FROM BOOK WHERE Book_ID = ?;
-- >> 8. Check if Book_ID exists in the database
SELECT Book_ID FROM BOOK;
-- >> 9. Insert New Book in the Database
INSERT INTO BOOK VALUES (?,?,?,?,?,?);
-- >> 10. Update data of a book in the database
UPDATE BOOK
SET Book_ISBN = ?, Book_Title = ?, Book_Author = ?, Book_Condition = ?
WHERE Book_ID = ?;
-- >> 11. Delete data from the database.
DELETE FROM BOOK WHERE Book_ID = ?;

-- * SECTION 4: STUDENT_INFORMATION (Add/Edit/Delete)
-- >> 12. Check if Student_ID exists (for Edit/Delete search feature) (then use data gathered to populate data)
SELECT * FROM STUDENT WHERE Student_ID = ?;
-- >> 13. Check if Student_IO exists in the database
SELECT Student_ID FROM STUDENT;
-- >> 14. Insert New Student in the Database
INSERT INTO STUDENT VALUES (?,?,?,?,?);
-- >> 15. Update Student data in the database.
UPDATE STUDENT
SET Student_LastName = ?, Student_FirstName = ?, Student_Section = ?, Student_YearLevel = ?
WHERE Student_ID  = ?;
-- >> 16. Delete Student Data in the database.
DELETE FROM STUDENT
WHERE Student_ID = ?;

-- * SECTION 5.1: BORROW REQUEST
-- >> 17. Query both Student_ID and Book_ID in the database whether the inputs exist in the database.
SELECT Student_ID FROM STUDENT;
SELECT Book_ID FROM BOOK;
-- >> 18. Verify if the Book_ID provided has a status of 'Available'
SELECT Book_Status FROM BOOK WHERE Book_ID = ?;
-- >> 19. Query the book title to be borrowed.
SELECT Book_Title FROM BOOK
WHERE Book_ID = ?;
-- >> 20. Query the name of the student who would borrow the book.
SELECT Student_FirstName, Student_LastName FROM STUDENT
WHERE Student_ID = ?;
-- >> 21. Generate and Insert a new Payment Row for the Book to be borrowed.
INSERT INTO PAYMENT VALUES (?,?,?);
-- >> 22. Update the Book_Status of the book to be borrowed to 'Borrowed'
UPDATE BOOK
SET Book_Status = ?
WHERE Book_ID = ?;
-- >> 23. Insert a new BORROW data to the database.
INSERT INTO BORROW VALUES (?,?,NULL,?,?,?,?,?,?);

-- * SECTION 5.2: VIEW STUDENTS AND BOOK (window inside the borrow_request.py)
-- >> 24. Load student data to the table widget.
SELECT Student_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Student_Section, Student_YearLevel
FROM STUDENT;
-- >> 25. Load book data to the table widget.
SELECT * FROM BOOK
WHERE Book_Status = 'Available';
-- * 26. SECTION 5.2.1: QUERIES ON BOOKS WITH VARYING REQUESTS (where Book_Status == "Available")
SELECT * FROM BOOK WHERE Book_ID = ? AND Book_Status = 'Available'; -- 26.1
SELECT * FROM BOOK WHERE Book_ISBN = ? AND Book_Status = 'Available'; -- 26.2
SELECT * FROM BOOK WHERE Book_Condition = ? AND Book_Status = 'Available'; -- 26.3
SELECT * FROM BOOK WHERE Book_Title LIKE '{like_query}' AND Book_Status = 'Available'; -- 26.4
SELECT * FROM BOOK WHERE Book_Author LIKE '{like_query}' AND Book_Status = 'Available'; -- 26.5
SELECT * FROM BOOK WHERE Book_Status = ? AND Book_Status = 'Available'; -- 26.6
-- * 27. SECTION 5.2.2: QUERIES ON STUDENTS WITH VARYING REQUESTS
-- 27.1
SELECT Student_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Student_Section, Student_YearLevel
FROM STUDENT
WHERE Student_ID = ?;
-- 27.2
SELECT Student_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Student_Section, Student_YearLevel
FROM STUDENT
WHERE Student_LastName = ? OR Student_FirstName = ?;
-- 27.3
SELECT Student_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Student_Section, Student_YearLevel
FROM STUDENT
WHERE Student_Section = ?;
-- 27.4
SELECT Student_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Student_Section, Student_YearLevel
FROM STUDENT
WHERE Student_YearLevel = ?;

-- * SECTION 6: RETURN REQUEST
-- >> 28. Query Borrow_ID in the database whether it exists in the database.
SELECT Borrow_ID FROM BORROW;
-- >> 29. Query Relevant data for the Return Process
SELECT Borrow_Date, Payment_ID, Book_ID FROM BORROW WHERE Borrow_ID = ?;
-- >> 30. Query the amount that the student have to pay for the return process.
SELECT Payment_Amount FROM PAYMENT
WHERE Payment_ID = ?;
-- >> 31. Query the book title to be returned.
SELECT Book_Title FROM BOOK
WHERE Book_ID = ?;
-- >> 32. Update the Payment Status from the PAYMENT table.
UPDATE PAYMENT
SET Payment_Status = ?
WHERE Payment_ID = ?;
-- >> 33. Update the Book Status of the book borrowed to 'Available'
UPDATE BOOK
SET Book_Status = ?
WHERE Book_ID = ?;
-- >> 34. Add the return date of the book and update its status to 'Returned'
UPDATE BORROW
SET Borrow_Return_Date = ?, Borrow_Status = ?
WHERE Borrow_ID = ?;

-- * SECTION 7: VIEW BOOK STATUS
-- >> 35. Query Available Books
SELECT Book_Title, Book_Author, Book_Condition FROM BOOK WHERE Book_Status = 'Available';
-- >> 36. Query Borrowed Books
SELECT Book_Title, Book_Author, Book_Condition FROM BOOK WHERE Book_Status = 'Borrowed';

-- * SECTION 8: CURRENTLY BORROWED BOOKS
SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Librarian_Name, Payment_ID
FROM BORROW
LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID
LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID
LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer
WHERE Borrow_Status = 'Borrowed';

-- * SECTION 9: CURRENTLY AVAILABLE BOOKS
SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Librarian_Name, Payment_Amount
FROM BORROW
LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID
LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID
LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer
LEFT JOIN PAYMENT ON PAYMENT.Payment_ID = BORROW.Payment_ID
WHERE Borrow_Overdue_Status = 1;

-- * SECTION 10: SEARCH HISTORY
-- ? NOTE: Some of the Queries here are the same as SECTION 5.2.1 and SECTION 5.2.2 so I will not be taking notes
-- ? of those queries anymore in this section.
-- >> 39. Load Borrow Data
SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Borrow_Return_Date, Borrow_Status, Borrow_Overdue_Status, Librarian_Name AS Borrow_Issuer, Payment_Amount
FROM BORROW
LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID
LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID
LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer
LEFT JOIN PAYMENT ON PAYMENT.Payment_ID = BORROW.Payment_ID;
-- >> 40. SECTION 10.1: QUERIES ON BORROW WITH VARYING REQUESTS
-- 40.1. Query Borrow_ID
SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Borrow_Return_Date, Borrow_Status, Borrow_Overdue_Status, Librarian_Name AS Borrow_Issuer, Payment_Amount
FROM BORROW
LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID
LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID
LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer
LEFT JOIN PAYMENT ON PAYMENT.Payment_ID = BORROW.Payment_ID
WHERE Borrow_ID LIKE '{like_query}';
-- 40.2. Query Borrow_Status (when Returned or Borrowed is typed)
SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Borrow_Return_Date, Borrow_Status, Borrow_Overdue_Status, Librarian_Name AS Borrow_Issuer, Payment_Amount
FROM BORROW
LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID
LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID
LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer
LEFT JOIN PAYMENT ON PAYMENT.Payment_ID = BORROW.Payment_ID
WHERE Borrow_Status LIKE '{like_query}';
-- 40.3. Query Borrow_Date
SELECT Borrow_ID, (Student_FirstName || ' ' || Student_LastName) AS Full_Name, Book_Title, Borrow_Date, Borrow_Return_Date, Borrow_Status, Borrow_Overdue_Status, Librarian_Name AS Borrow_Issuer, Payment_Amount
FROM BORROW
LEFT JOIN STUDENT ON STUDENT.Student_ID = BORROW.Student_ID
LEFT JOIN BOOK ON BOOK.Book_ID = BORROW.Book_ID
LEFT JOIN LIBRARIAN ON LIBRARIAN.Librarian_Username = BORROW.Borrow_Issuer
LEFT JOIN PAYMENT ON PAYMENT.Payment_ID = BORROW.Payment_ID
WHERE Borrow_Date LIKE '{like_query}';