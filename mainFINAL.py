#https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html#PySide6.QtWidgets.PySide6.QtWidgets.QLineEdit.setInputMask
#https://www.w3schools.com/python/python_strings_slicing.asp
#https://www.w3schools.com/python/ref_string_rsplit.asp

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout, QWidget
import sys


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        self.username_label = QLabel("Benutzername:", self)
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("max. 6 Zeichen")
        #self.username_input.setMaxLength(6)
        self.username_input.setInputMask("NNNNNN;_")

        self.password_label = QLabel("Kennwort:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("6 Zeichen")
        #self.password_input.setMaxLength(6)
        self.password_input.setInputMask("XXXXXX")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Anmelden", self)
        self.login_button.clicked.connect(self.test)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.username_label, 0, 0)
        self.grid_layout.addWidget(self.username_input, 0, 1)
        self.grid_layout.addWidget(self.password_label, 1, 0)
        self.grid_layout.addWidget(self.password_input, 1, 1)
        self.grid_layout.addWidget(self.login_button, 2, 1)

        self.widget = QWidget()
        self.widget.setLayout(self.grid_layout)

        self.setCentralWidget(self.widget)

        self.list_username = ["user1", "user2", "user3"]
        self.list_password = ["123456", "123456", "123456"]

    def test(self):
        exists = False
        index = None

        for n in self.list_username:
            if self.username_input.text() == n:
                exists = True
                index = self.list_username.index(n)

            if exists == True:
                if self.password_input.text() == self.list_password[index]:
                    QMessageBox.information(self, "Anmeldung war erfolgreich.", "Anmeldung war erfolgreich.")
                    break

            else:
                QMessageBox.warning(self, "Anmeldung ist fehlgeschlagen.", "Anmeldung ist fehlgeschlagen.")
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
