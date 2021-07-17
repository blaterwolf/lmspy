# School Library Management System
A Simple School Library Management System for a school library that manages the condition of the books, borrowed books, students or the borrowers, penalty for overdue books. This design is inspired by simple library management systems in libraries which helps librarians to have a system for organizing a library.

[![Python: 3.9.6](https://img.shields.io/badge/python-3.9.6-blue?logo=python&logoColor=FFE873)](https://www.python.org/downloads) [![PyQt: 6.1.1](https://img.shields.io/badge/pyqt-6.1.1-darkgreen)](https://pypi.org/project/PyQt6)
___
### Domain Description
A school library must keep track of the status of all books in the library whether it is quality or quantity. It tracks all the available and borrowed books that a student can borrow with information related to the books and the borrower. It can also be able to add, edit, and delete student and book information. As a student borrows a book, the librarian is prompted to ask for the Student ID and the Book ID so that a student can borrow a book and the system takes note of the date that they borrowed it. If the student failed to return the book in each date (which is set to 7 days), they will be given a penalty for overdue books and will be given a fine that is calculated. The penalty is worth 100PHP when the student does not return it within the next 7 days and every succeeding day that the student does not return it, the penalty is increased by 5% of 100PHP. When the student returns the book, they will input the borrow ID issued to them and if there is a fine, it will show how much the fine will be so that they can pay for it. Each borrowed book is linked to a relevant information which is: who is the borrower (Student ID), the librarian who issued the borrow request (Librarian ID), the book title (Book ID), etc.
___
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
You must have at least Python 3.9.x or above to work. When we are building this, Visual Studio Code is recommended to run and try the program. PyCharm also works. You have to take note of the following packages to install:

| Package Name | Command                 | Description                                                                                                                     | Link                                                                                                                            |
|--------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| PyQt6        | pip install PyQt6       | This is a GUI Library that we will be using in this project.                                                                    | [![PyQt: 6.1.1](https://img.shields.io/badge/pyqt-6.1.1-darkgreen)](https://pypi.org/project/PyQt6)                             |
| pyqt6-tools  | pip install pyqt6-tools | This package includes the PyQt Designer which is a GUI that makes a GUI for the project.                                        | [![PyQt6 Tools: 6.1.0.3.2](https://img.shields.io/badge/pyqt6tools-6.1.0.3.2-darkgreen)](https://pypi.org/project/pyqt6-tools/) |
| Pillow       | pip install Pillow      | To generate an image for our QR Code, we will be using the Pillow package.                                                      | [![Pillow: 8.3.1](https://img.shields.io/badge/Pillow-8.3.1-blue)](https://pypi.org/project/Pillow/)                            |
| qrcode       | pip install qrcode      | This generates a QRCode for the Google Authentication which stores the generated provisioning URI.                              | [![qrcode: 7.1](https://img.shields.io/badge/qrcode-7.1-black)](https://pypi.org/project/qrcode/)                               |
| pyotp        | pip install pyotp       | This helps us to generate a base32 which will be used to generate a provisioning URI so that Google Authentication can scan it. | [![pyotp: 2.6.0](https://img.shields.io/badge/pyotp-2.6.0-black)](https://pypi.org/project/pyotp/)                              |
When everything is installed, run `login.py`. 
___
| Screenshots                 | File                |
|-----------------------------|---------------------|
| [![login][4]][4]            | `login.py`            |
| [![main_menu][5]][5]        | `main_menu.py`        |
| [![book_information][6]][6] | `book_information.py` |
| [![search_history][7]][7]   | `main_menu.py`        |

[1]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/erd_library.png
[2]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/relational_schema.png
[3]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/database_diagram.png
[4]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/login.png
[5]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/main_menu.png
[6]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/book_information.png
[7]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/search_history.png