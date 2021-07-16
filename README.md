# School Library Management System
A Library Management System for a school library that manages the condition of the books, borrowed books, students or the borrowers, penalty for overdue books. This design is inspired by simple library management systems in libraries which helps librarians to have a system for organizing a library.

[![Python: 3.9.6](https://img.shields.io/badge/python-3.9.6-blue?logo=python&logoColor=FFE873)](https://www.python.org/downloads) [![PyQt: 6.1.1](https://img.shields.io/badge/pyqt-6.1.1-darkgreen)](https://pypi.org/project/PyQt6)
___
### Domain Description
A school library must keep track of the status of all books in the library whether it is quality or quantity. It tracks all the available and borrowed books that a student can borrow with information related to the books and the borrower. It can also be able to add, edit, and delete student and book information. As a student borrows a book, the librarian is prompted to ask for the Student ID and the Book ID so that a student can borrow a book and the system takes note of the date that they borrowed it. If the student failed to return the book in each date (which is set to 7 days), they will be given a penalty for overdue books and will be given a fine that is calculated. The penalty is worth 100PHP when the student does not return it within the next 7 days and every succeeding day that the student does not return it, the penalty is increased by 5% of 100PHP. When the student returns the book, they will input the borrow ID issued to them and if there is a fine, it will show how much the fine will be so that they can pay for it. Each borrowed book is linked to a relevant information which is: who is the borrower (Student ID), the librarian who issued the borrow request (Librarian ID), the book title (Book ID), etc.
___
### Sample Queries / Features
| Sample Queries                                                                                    | Features                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Give me all the books that are currently available in the library.                                | >>   view_book_status.py - This window queries the available books. This shows three columns: the book title, the author, and the current condition of the book.                         |
| Give me all the books that are currently borrowed.                                                | >>   view_book_status.py - This window queries the borrowed books. This shows three columns: the book title, the author, and the current   condition of the book.                        |
| Give me the current condition of all the books.                                                   | >>   view_book_status.py - This window queries the available and borrowed books with one of its columns is the condition of the book.                                                    |
| Give me all the students who currently borrowed a book.                                           | >>   currently_borrowed_books.py - This window displays the currently borrowed books.                                                                                                    |
| Give me all the students who currently borrowed a book and is past due date of the returned date. | >>   currently_overdue_books.py - This window displays the currently borrowed books that are past 7 days of the return date. This also displays the amount that the student has to pay.  |
| Give me the history of borrowed books all time or in a specific year.                             | >>   search_history.py - This window searches for relevant information in the database such as for the book, student, or on the borrow table.                                            |
___
### ERD
[![erd_library][1]][1]

___
### Relational Schema
[![relational_schema][2]][2]
___
### Database Diagram
[![database_diagram][3]][3]
___
### Installation and Setup
```py
# will update to v1.0.5
```
___
### Screenshots
```py
# will update to v1.0.5
```

[1]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/erd_library.png
[2]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/relational_schema.png
[3]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/database_diagram.png