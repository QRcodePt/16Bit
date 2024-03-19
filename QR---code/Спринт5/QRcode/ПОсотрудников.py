#from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.dialog import MDDialog
import sqlite3

x = ""
screen_width, screen_height = (400, 100)

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        login_label = MDLabel(text='Логин', halign="center")
        login_label_pos_x = screen_width / 9 - login_label.width / 2
        login_label_pos_y = screen_height / 2 + screen_height / 2
        login_label.pos = (login_label_pos_x, login_label_pos_y)

        login_input = MDTextField(hint_text="Введите логин", size_hint=(None, None), width=150, pos_hint={"center_x": 0.5, "center_y": 0.6})

        password_label = MDLabel(text='Пароль', halign="center")
        password_label_pos_x = screen_width / 4 - password_label.width / 1
        password_label_pos_y = screen_height / 10 + screen_height / 24
        password_label.pos = (password_label_pos_x, password_label_pos_y)

        password_input = MDTextField(hint_text="Введите пароль", password=True, size_hint=(None, None), width=150, pos_hint={"center_x": 0.5, "center_y": 0.45})

        layout.add_widget(login_label)
        layout.add_widget(login_input)
        layout.add_widget(password_label)
        layout.add_widget(password_input)

        button = MDRectangleFlatButton(text='Вход', pos_hint={"center_x": 0.5, "center_y": 0.35})
        button.bind(on_press=self.check_login)
        layout.add_widget(button)

        self.add_widget(layout)

    def check_login(self, instance):
        login_input = self.children[0].children[3]
        password_input = self.children[0].children[2]

        login = login_input.text
        password = password_input.text

        conn = sqlite3.connect('work_time_tracking.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Контактные_данные FROM Сотрудники WHERE Логин=? AND Пароль=?", (login, password))
        user = cursor.fetchone()

        if user:
            x = str(user[0])
            self.open_next_screen(instance)
        else:
            self.show_invalid_password_popup()

        cursor.close()
        conn.close()

    def show_invalid_password_popup(self):
        dialog = MDDialog(title="Ошибка", text="Неправильный логин/пароль, попробуйте снова.", size_hint=(0.8, 0.3))
        dialog.open()

    def open_next_screen(self, instance):
        self.manager.current = 'NextScreen'

class NextScreen(Screen):
    def __init__(self, **kwargs):
        super(NextScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        fio_label = MDLabel(text=x, halign="center")
        fio_label_pos_x = screen_width / 2 - len(x)*10 / 2
        fio_label_pos_y = screen_height / 2 + screen_height / 3
        fio_label.pos = (fio_label_pos_x, fio_label_pos_y)
        layout.add_widget(fio_label)

        button1 = MDRectangleFlatButton(text='Открыть смену', pos_hint={"center_x": 0.3, "center_y": 0.2})
        button1.bind(on_press=self.open_qr_screen)
        layout.add_widget(button1)

        button2 = MDRectangleFlatButton(text='Закрыть смену', pos_hint={"center_x": 0.7, "center_y": 0.2})
        button2.bind(on_press=self.open_qr_screen)
        layout.add_widget(button2)

        hours_label = MDLabel(text='Часов отработано 13', halign="center", pos_hint={"center_x": 0.5, "center_y": 0.3})
        layout.add_widget(hours_label)

        days_label = MDLabel(text='Дней отработано 13', halign="center", pos_hint={"center_x": 0.5, "center_y": 0.4})
        layout.add_widget(days_label)

        button3 = MDRectangleFlatButton(text='Выход', pos_hint={"center_x": 0.9, "center_y": 0.1})
        button3.bind(on_press=self.open_first_screen)
        layout.add_widget(button3)

        self.add_widget(layout)

    def open_qr_screen(self, instance):
        self.manager.current = 'QR_Screen'

    def open_first_screen(self, instance):
        self.manager.current = 'LoginScreen'

class QR_Screen(Screen):
    def __init__(self, **kwargs):
        super(QR_Screen, self).__init__(**kwargs)
        layout = FloatLayout()

        qr_label = MDLabel(text='Отсканируйте QR код', halign="center", pos_hint={"center_x": 0.5, "center_y": 0.7})

        button = MDRectangleFlatButton(text='Назад', pos_hint={"center_x": 0.9, "center_y": 0.1})
        button.bind(on_press=self.open_second_screen)

        layout.add_widget(button)
        layout.add_widget(qr_label)

        self.add_widget(layout)

    def open_second_screen(self, instance):
        self.manager.current = 'NextScreen'

class TestApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='LoginScreen'))
        sm.add_widget(NextScreen(name='NextScreen'))
        sm.add_widget(QR_Screen(name='QR_Screen'))

        return sm

if __name__ == '__main__':
    TestApp().run()