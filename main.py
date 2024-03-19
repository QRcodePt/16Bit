from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.app import App
import qrcode
import sqlite3
from datetime import datetime

# Подключение к базе данных SQLite
conn = sqlite3.connect('DB_workhour.db')
cursor = conn.cursor()

# Создание таблицы, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS QRCode (
        code_id INTEGER PRIMARY KEY,
        qr_code TEXT NOT NULL,
        last_updated DATETIME NOT NULL
    )
''')
conn.commit()

# Функция для создания QR-кода
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

# KivyMD код
KV = '''
BoxLayout:
    orientation: 'vertical'

    Image:
        id: qr_code_image
        source: 'qrcode.png'

    Button:
        text: 'Update QR Code'
        on_press: app.update_qr_code()
'''

class QRCodeApp(App):
    def build(self):
        return Builder.load_string(KV)

    def update_qr_code(self):
        # Генерация нового QR-кода
        new_qr_data = "New QR Code Data"
        generate_qr_code(new_qr_data)

        # Сохранение нового QR-кода в базу данных
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO QRCode (qr_code, last_updated) VALUES (?, ?)
        ''', (new_qr_data, current_time))
        conn.commit()

        # Обновление изображения QR-кода в приложении
        self.root.ids.qr_code_image.source = 'qrcode.png'

# Обновление QR-кода каждые 10 секунд
def update_qr_code_callback(dt):
    qr_app.update_qr_code()

qr_app = QRCodeApp()
Clock.schedule_interval(update_qr_code_callback, 10)
qr_app.run()
