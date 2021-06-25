### Render ui to py
```
pyuic6 -x login.ui -o login.py
```
### WindowFlags (Borderless)
```py
Login.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
```
### Close Button
```py
self.pushButton_3.clicked.connect(sys.exit)
```
### Colors
```
#CBB1A0 - Background
#842a2d - Main Color
```
### For Login Buttons
```
QLineEdit {\n      color: rgb(231, 231, 231);\n      font: 15pt "Verdana";\n      border: None;\n      border-bottom-color: white;\n      border-radius: 10px;\n      padding: 0 8px;\n      background: #CBB1A0;\n      selection-background-color: darkgray;\n}
```
### Sign In Buttons
```cs
color: #842a2d;\nfont: 17pt "Franklin Gothic Book";\nborder: 2px solid #842a2d;\npadding: 2px;\nborder-radius: 10px;\nopacity: 100;\n
```
### CLOSE COMMAND
```
self.pushButton.clicked.connect(sys.exit)
```
### code for readable base32
```python
def readable_base32(self, base32):
    str = ""
    counter = 0
    while counter != 32:
        if counter % 4 == 0:
            str += f" {base32[counter]}"
        else:
            str += base32[counter]
        counter += 1
    return " ".join(str.split(" ")[1:])
```
```py
self.lineEdit_2.setText(_translate(
            "Validation", f"{self.readable_base32(self.current_base32)}"))
```
### Buttons(?)
```
QLineEdit {\n      color: rgb(231, 231, 231);\n      font: 12pt "Verdana" bold;\n      border: None;\n      border-bottom-color: white;\n      border-radius: 10px;\n      padding: 0 8px;\n      background: #CBB1A0;\n      selection-background-color: darkgray;\n}
```
### Instructions
```
<Logo> Simple OTP Validation using Google Authenticator

1. Download the Google Authenticator App
2. Your Randomly Generated Base32 is presented below. Press the + button on Google Authenticator then click Enter Setup Key.
3. Type anything on the Account Name. Input all 32 digits in the "Your Key" field WITHOUT spaces. 
4. Set it to time-based as default. Click Add.
5. Enter the current OTP on your phone to the input field below.
```