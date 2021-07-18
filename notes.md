### Render ui to py
```
pyuic6 -x login.ui -o login.py
```
### WindowFlags (Borderless)
```
<Object>.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
```
### EXIT COMMAND
In PyQt6, the `sys.exit` command terminates the whole program.
```
self.<Object>.clicked.connect(sys.exit)
```
### CLOSE COMMAND
In PyQt6, the `<Object>.close` command closes the window only, leaving any potential open windows.
```
self.pushButton.clicked.connect(<Object>.close)
```
### Colors
```
#CBB1A0 - Background
#842a2d - Main Color
```
### Instructions
Instructions for the OTP Validation using Google Authenticator.
```
<Logo> Simple OTP Validation using Google Authenticator
1. Download the Google Authenticator App
2. Your Randomly Generated Base32 is presented below. Press the + button on Google Authenticator then click Enter Setup Key.
3. Type anything on the Account Name. Input all 32 digits in the "Your Key" field WITHOUT spaces. 
4. Set it to time-based as default. Click Add.
5. Enter the current OTP on your phone to the input field below.
```
### Loading Data
To load data from the TableWidget in PyQt6... (reference only, query might change depending on the problem).
```py
def load_data(self):
    con = sqlite3.connect('./db/test.db')
    query = "SELECT Book_Title, Book_Author, Book_Condition FROM BOOK WHERE Book_Status = \"Available\";"
    result = con.execute(query)
    self.tableWidget.setRowCount(0)
    for row, form in enumerate(result):
        self.tableWidget.insertRow(row)
        for column, item in enumerate(form):
            print(str(item))
            self.tableWidget.setItem(
                row, column, QtWidgets.QTableWidgetItem(str(item)))
```
### Parameters for Condition and Status
```md
Book_Condition
New
Fine
Good
Fair
Poor

Book_Status
Available
Borrowed

Borrow_Status
Borrowed
Returned

Overdue_Status
0 - False
1 - True

Payment_Status
Pending
Paid
```
### Generate 5 Random Numbers and Letters
```py
import random
import string

random = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
```
### Testing for Main Menu Checking for Overdue Books
```py
# * pip install tabulate (simple and cool table print)
from tabulate import tabulate
collect_data = [] # * outside for loop
collect_data.append(
                [borrow_id, payment_id, penalty_amount, days_passed])
print(tabulate(collect_data, headers=[
              'Borrow_ID', 'Payment_ID', 'Payment_Evaluation', 'Days Passed']))
```