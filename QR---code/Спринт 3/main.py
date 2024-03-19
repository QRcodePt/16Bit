from kivy import Config
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

# Получаем размеры монитора
screen_width, screen_height = Window.size

Window.clearcolor = (0.5, 0.5, 0.5, 1)

# Задаем размеры окна
Config.set('graphics', 'width', str(screen_width))
Config.set('graphics', 'height', str(screen_height))

# Применяем изменения
Config.write()

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        print(kwargs, '1')
        print(Window.size)
        layout = FloatLayout()

        # Создаем надпись для логина
        login_label = Label(text='Логин', size_hint=(None, None), size=(150, 50))

        # Устанавливаем позицию надписи для логина
        login_label_pos_x = screen_width / 2 - login_label.width / 2
        login_label_pos_y = screen_height / 2 + screen_height / 3
        login_label.pos = (login_label_pos_x, login_label_pos_y)

        # Создаем строку ввода для логина
        login_input = TextInput(size_hint=(None, None), size=(150, 50))

        # Устанавливаем позицию строки ввода для логина
        login_input_pos_x = screen_width / 2 - login_input.width / 2
        login_input_pos_y = screen_height / 2 + screen_height / 3 - 50
        login_input.pos = (login_input_pos_x, login_input_pos_y)

        # Создаем надпись для пароля
        password_label = Label(text='Пароль', size_hint=(None, None), size=(150, 50))

        # Устанавливаем позицию надписи для пароля
        password_label_pos_x = screen_width / 2 - password_label.width / 2
        password_label_pos_y = screen_height / 2 + screen_height / 6
        password_label.pos = (password_label_pos_x, password_label_pos_y)

        # Создаем строку ввода для пароля
        password_input = TextInput(password = True, size_hint=(None, None), size=(150, 50))

        # Устанавливаем позицию строки ввода для пароля
        password_input_pos_x = screen_width / 2 - password_input.width / 2
        password_input_pos_y = screen_height / 2 + screen_height / 6 - 50
        password_input.pos = (password_input_pos_x, password_input_pos_y)

        layout.add_widget(login_label)
        layout.add_widget(login_input)
        layout.add_widget(password_label)
        layout.add_widget(password_input)

        # Создаём кнопку и устанавливаем позицию
        button = Button(text='Вход', size_hint=(None, None), size=(150, 50))
        button_pos_x = screen_width / 2 - button.width / 2
        button_pos_y = screen_height / 2 - 50
        button.pos = (button_pos_x, button_pos_y)
        button.bind(on_press=self.open_next_screen)
        layout.add_widget(button)

        self.add_widget(layout)

    def open_next_screen(self, instance):
        print('openns')
        self.manager.current = 'NextScreen'

class NextScreen(Screen):
    def __init__(self, **kwargs):
        super(NextScreen, self).__init__(**kwargs)
        print(kwargs,'2')
        print(Window.size)
        layout = FloatLayout()

        # Добавляем строку с ФИО
        x = 'Осколков Максим Владимирович'
        fio_label = Label(text=x, size_hint=(None, None), size=(len(x)*10, 50))
        fio_label_pos_x = screen_width / 2 - len(x)*10 / 2
        fio_label_pos_y = screen_height / 2 + screen_height / 3
        fio_label.pos = (fio_label_pos_x, fio_label_pos_y)
        layout.add_widget(fio_label)

        # Добавляем первую кнопку
        button1 = Button(text='Открыть смену', size_hint=(None, None), size=(250, 80))
        button1_pos_x = screen_width / 2 - 260
        button1_pos_y = screen_height / 2 + screen_height / 4
        button1.pos = (button1_pos_x, button1_pos_y)
        button1.bind(on_press=self.open_qr_screen)
        layout.add_widget(button1)

        # Добавляем вторую кнопку
        button2 = Button(text='Закрыть смену', size_hint=(None, None), size=(250, 80))
        button2_pos_x = screen_width / 2 + 10
        button2_pos_y = screen_height / 2 + screen_height / 4
        button2.pos = (button2_pos_x, button2_pos_y)
        button2.bind(on_press=self.open_qr_screen)
        layout.add_widget(button2)

        # Добавляем строку с отработанными часами
        hours_label = Label(text='Часов отработано 13', size_hint=(None, None), size=(300, 50))
        hours_label_pos_x = screen_width / 2 - hours_label.width / 2
        hours_label_pos_y = screen_height / 2 + screen_height / 5
        hours_label.pos = (hours_label_pos_x, hours_label_pos_y)
        layout.add_widget(hours_label)

        # Добавляем строку с отработанными часами
        days_label = Label(text='Дней отработано 13', size_hint=(None, None), size=(300, 50))
        days_label_pos_x = screen_width / 2 - days_label.width / 2
        days_label_pos_y = screen_height / 2 + screen_height / 6
        days_label.pos = (days_label_pos_x, days_label_pos_y)
        layout.add_widget(days_label)

        # Создаём кнопку и устанавливаем позицию
        button3 = Button(text='Выход', size_hint=(None, None), size=(100, 100))
        button3_pos_x = screen_width - 100
        button3_pos_y = screen_height - 100
        button3.pos = (button3_pos_x, button3_pos_y)
        button3.bind(on_press=self.open_first_screen)
        layout.add_widget(button3)

        self.add_widget(layout)

    def open_qr_screen(self, instance):
        print('openqr')
        self.manager.current = 'QR_Screen'

    def open_first_screen(self, instance):
        print('openfs')
        self.manager.current = 'LoginScreen'

class QR_Screen(Screen):
    def __init__(self, **kwargs):
        super(QR_Screen, self).__init__(**kwargs)
        print(kwargs, '3')
        print(Window.size)
        layout = FloatLayout()

        # Создаем надпись для логина
        qr_label = Label(text='Отсканируйте QR код', size_hint=(None, None), size=(150, 50))
        qr_label_pos_x = screen_width / 2 - qr_label.width / 2
        qr_label_pos_y = screen_height / 3 + screen_height / 2
        qr_label.pos = (qr_label_pos_x, qr_label_pos_y)

        # Создаём кнопку и устанавливаем позицию
        button = Button(text='Назад', size_hint=(None, None), size=(100, 100))
        button_pos_x = screen_width - 100
        button_pos_y = screen_height -  100
        button.pos = (button_pos_x, button_pos_y)
        button.bind(on_press=self.open_second_screen)
        layout.add_widget(button)
        layout.add_widget(qr_label)

        self.add_widget(layout)

    def open_second_screen(self, instance):
        self.manager.current = 'NextScreen'

class TestApp(App):
    print(3)
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='LoginScreen'))
        sm.add_widget(NextScreen(name='NextScreen'))
        sm.add_widget(QR_Screen(name='QR_Screen'))

        return sm

if __name__ == '__main__':
    TestApp().run()
