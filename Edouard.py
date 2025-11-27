from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QPixmap, QIntValidator
from PySide6.QtWidgets import QMainWindow, QApplication, QMenuBar, QPushButton, QFrame, QLineEdit, QGridLayout, \
    QRadioButton, QButtonGroup


class MaFenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 600)
        self.setWindowTitle("Jeu tutorat")
        self.setWindowIcon(QPixmap("./images/play-button.png"))

        menu_bar = QMenuBar()
        action_menu_principal = QAction("Menu principal", self)
        action_parametres = QAction("Paramètres", self)
        action_quit = QAction("Quitter", self)
        menu_bar.addAction(action_menu_principal)
        menu_bar.addAction(action_parametres)
        menu_bar.addAction(action_quit)
        action_menu_principal.triggered.connect(self.menu_principal_clicked)
        action_parametres.triggered.connect(self.parametres_clicked)
        action_quit.triggered.connect(self.close)
        self.setMenuBar(menu_bar)

        self.button_play = None
        self.frame_parameters = None

        self.menu_principal_clicked()

    def button_play_clicked(self):
        pass

    def parametres_clicked(self):
        self.frame_parameters = QFrame()
        self.frame_parameters.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        disposition_frame = QGridLayout()
        self.frame_parameters.setLayout(disposition_frame)

        button1 = QRadioButton("Bouton 1")
        button2 = QRadioButton("Bouton 2")
        button3 = QRadioButton("Bouton 3")
        button_group = QButtonGroup()
        button_group.addButton(button1)
        button_group.addButton(button2)
        button_group.addButton(button3)
        disposition_frame.addWidget(button1, 0, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        disposition_frame.addWidget(button2, 0, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        disposition_frame.addWidget(button3, 0, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

        line_edit_speed = QLineEdit()
        disposition_frame.addWidget(line_edit_speed, 1, 0, 1, 3)
        line_edit_speed.setPlaceholderText("Multiplicateur de vitesse de 0 à 99")
        validator = QIntValidator(0, 10)
        line_edit_speed.setValidator(validator)

        self.setCentralWidget(self.frame_parameters)

    def menu_principal_clicked(self):
        self.button_play = QPushButton()
        try:
            play_icon = QPixmap("./images/play-button.png")
        except FileNotFoundError:
            raise MonExecption
        self.button_play.setIcon(play_icon)
        self.button_play.setIconSize(play_icon.size())
        self.button_play.clicked.connect(self.button_play_clicked)
        self.setCentralWidget(self.button_play)

class MonExecption(Exception):
    def __init__(self):
        super().__init__()
        pass


app = QApplication()
mf = MaFenetre()
mf.show()
app.exec()

