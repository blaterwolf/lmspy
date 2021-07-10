# School Library Management System
A Simple School Library Management System for a school library that manages the condition of the books, borrowed books, students or the borrowers, penalty for unreturned books. This design is inspired by real-world library management systems in libraries which helps librarians to have a system for organizing a library.

[![Python: 3.9.6](https://img.shields.io/badge/python-3.9.6-blue?logo=python&logoColor=FFE873)](https://www.python.org/downloads) [![PyQt: 6.1.1](https://img.shields.io/badge/pyqt-6.1.1-darkgreen)](https://pypi.org/project/PyQt6)
___
### Domain Description
A school library has to keep track of the status of all books in the library whether it is quality or quantity. It tracks all the available and unavailable books that a student can borrow with information related to the books and the borrower. It can also be able to add and edit student and book information. As a student borrows a book, it will generate the book information and the date that they borrowed it and the potential return date. If the student failed to return the book in a given date (let’s say 7 days), they will be given a penalty for overdue books and will be given a fine that is calculated. When the student returns the book, they will input the return date and the current condition of the book and if there is a fine, it will show how much the fine will be so that they can pay for it. Each borrowed book is linked to the relevant information which is: Who is the borrower, what date did the borrower borrowed it and what is the due date.
___
### Sample Queries
* Give me all the books that are currently available in the library.
* Give me all the books that are currently borrowed.
* Give me all the students who currently borrowed a book.
* Give me all the students who currently borrowed a book and is past due date of the returned date. 
* Give me the history of borrowed books all time or in a specific year.
* Give me the current condition of all the books.
___
### ERD
[![erd_library][1]][1]
```py
# append image here...
```
___
### Relational Schema
```py
# append image here...
```
___
### Installation and Setup
```py
# Instructions and Setup here...
```
___
### Screenshots
```py
# append images here...
```

[1]: https://raw.githubusercontent.com/blaterwolf/lmspy/main/img/erd_library.png