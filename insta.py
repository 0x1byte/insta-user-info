from PyQt6 import QtCore, QtGui, QtWidgets
from insta_api import get_user_info
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 200, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 80, 100, 34))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Instagram User Info"))
        self.lineEdit.setPlaceholderText(
            _translate("MainWindow", "Enter Instagram Username")
        )
        self.lineEdit.setClearButtonEnabled(True)
        self.pushButton.setText(_translate("MainWindow", "Get User Info"))
        self.lineEdit.returnPressed.connect(self.get_user_info)
        self.pushButton.clicked.connect(self.get_user_info)

    def download_user_profile_pic(self, user_info):
        profile_pic_url = user_info["user"]["profile_pic_url"]
        response = requests.get(profile_pic_url)
        with open("profile_pic.jpg", "wb") as file:
            file.write(response.content)
            file.close()

    def get_user_info(self):
        username = self.lineEdit.text()
        if username:
            user_info = get_user_info(username)
            if user_info:
                self.download_user_profile_pic(user_info)
                self.show_user_info(user_info)
            else:
                self.statusbar.showMessage("User not found")

    def show_user_info(self, user_info):
        user_id = user_info["user"]["pk"]
        username = user_info["user"]["username"]
        full_name = user_info["user"]["full_name"]
        is_private = user_info["user"]["is_private"]
        is_verified = user_info["user"]["is_verified"]
        can_sms_reset = user_info["can_sms_reset"]
        can_email_reset = user_info["can_email_reset"]
        try:
            obfuscated_email = user_info["obfuscated_email"]
        except KeyError:
            obfuscated_email = "Not Available"
        try:
            obfuscated_phone = user_info["obfuscated_phone"]
        except KeyError:
            obfuscated_phone = "Not Available"
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.setWindowTitle(f"User Info: {username}")
        self.main_window.resize(400, 300)
        self.central_widget = QtWidgets.QWidget(parent=self.main_window)
        self.central_widget.setObjectName("central_widget")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)
        self.main_window.setCentralWidget(self.central_widget)
        self.profile_image = QtWidgets.QLabel()
        self.profile_image.setPixmap(QtGui.QPixmap("profile_pic.jpg"))
        self.profile_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.user_id_label = QtWidgets.QLabel(f"User ID: {user_id}")
        self.username_label = QtWidgets.QLabel(f"Username: {username}")
        self.full_name_label = QtWidgets.QLabel(f"Full Name: {full_name}")
        self.is_private_label = QtWidgets.QLabel(f"Is Private: {is_private}")
        self.is_verified_label = QtWidgets.QLabel(f"Is Verified: {is_verified}")
        self.can_sms_reset_label = QtWidgets.QLabel(f"Can SMS Reset: {can_sms_reset}")
        self.can_email_reset_label = QtWidgets.QLabel(
            f"Can Email Reset: {can_email_reset}"
        )
        self.obfuscated_email_label = QtWidgets.QLabel(
            f"Obfuscated Email: {obfuscated_email}"
        )
        self.obfuscated_phone_label = QtWidgets.QLabel(
            f"Obfuscated Phone: {obfuscated_phone}"
        )
        self.vertical_layout.addWidget(self.profile_image)
        self.vertical_layout.addWidget(self.user_id_label)
        self.vertical_layout.addWidget(self.username_label)
        self.vertical_layout.addWidget(self.full_name_label)
        self.vertical_layout.addWidget(self.is_private_label)
        self.vertical_layout.addWidget(self.is_verified_label)
        self.vertical_layout.addWidget(self.can_sms_reset_label)
        self.vertical_layout.addWidget(self.can_email_reset_label)
        self.vertical_layout.addWidget(self.obfuscated_email_label)
        self.vertical_layout.addWidget(self.obfuscated_phone_label)
        self.main_window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
