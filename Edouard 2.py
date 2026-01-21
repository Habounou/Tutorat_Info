from PySide6.QtWidgets import QFrame, QGridLayout, QPushButton, QApplication, QLineEdit


class MaFenetre(QFrame):
    def __init__(self):
        super().__init__()

        self.disposition_frame = QGridLayout()
        self.setLayout(self.disposition_frame)

        self.bouton = QPushButton("Bouton")
        self.disposition_frame.addWidget(self.bouton, 0, 0, 1, 5)

        self.bouton_2 = QPushButton("Bouton 2")
        self.disposition_frame.addWidget(self.bouton_2, 0, 0, 3, 1)

        self.line_edit = QLineEdit("Test")
        self.line_edit.textChanged.connect(lambda nouv_text: print(nouv_text))
        self.disposition_frame.addWidget(self.line_edit, 1, 0, 1, 5)

    def afficher_texte(self):
        try:
            return self.line_edit.text()
        except AttributeError:
            return "Erreur"
        finally:
            return str(42)

app = QApplication()
fenetre = MaFenetre()
print(fenetre.afficher_texte())
fenetre.show()
app.exec()