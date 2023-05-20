from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout, QWidget
import sys

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Login")

        # Erstelle Benutzername Label und Input Feld
        self.username_label = QLabel("Benutzername:", self)
        self.username_input = QLineEdit(self)

        # Erstelle Passwort Label und Input Feld
        self.password_label = QLabel("Kennwort:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        # Erstelle Button zum Login
        self.login_button = QPushButton("Anmelden", self)
        self.login_button.clicked.connect(self.check_login)

        # GridLayout Zuordnung
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.username_label, 0, 0)
        self.grid_layout.addWidget(self.username_input, 0, 1)
        self.grid_layout.addWidget(self.password_label, 1, 0)
        self.grid_layout.addWidget(self.password_input, 1, 1)
        self.grid_layout.addWidget(self.login_button, 2, 1)

        # Widget erstellen und GridLayout setzen
        self.widget = QWidget()
        self.widget.setLayout(self.grid_layout)

        # CentralWidget setzen
        self.setCentralWidget(self.widget)

    def check_login(self):
        # Liste von gültigen Benutzernamen und dazugehörige Passwörter
        valid_users = {
            "user1": "pass1",
            "user2": "pass2",
            "user3": "pass3"
        }

        # Eingegebenen Benutzernamen und Passwort abrufen
        username = self.username_input.text()
        password = self.password_input.text()

        # Prüfung ob Benutzername gültig ist
        if username in valid_users:
            # Prüfung ob Passwort gültig ist
            if password == valid_users[username]:
                # PopUp Fenster das anzeigt dass Anmeldung erfolgreich war
                QMessageBox.information(self, "Anmeldung erfolgreich", "Sie haben sich erfolgreich angemeldet.")
            else:
                # PopUp Fenster das anzeigt dass Anmeldung fehlgeschlagen ist bzw. das Passwort falsch ist
                QMessageBox.warning(self, "Anmeldung fehlgeschlagen", "Das eingegebene Kennwort ist falsch.")
        else:
            # PopUp Fenster das anzeigt dass Anmeldung fehlgeschlagen ist bzw. der Benutzername unbekannt ist
            QMessageBox.warning(self, "Anmeldung fehlgeschlagen", "Der eingegebene Benutzername ist unbekannt.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
