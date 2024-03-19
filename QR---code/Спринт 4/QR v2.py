from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.config import Config
from kivy.clock import Clock

import qrcode
import os

Config.set("graphics", "width", 400)
Config.set("graphics", "height", 700)

class NotificationPopup(Popup):
    pass

class MyApp(App):
    def build(self):
        layout = FloatLayout()

        self.qr_image = Image(source='')
        layout.add_widget(self.qr_image)

        # Generate the initial QR code
        self.generate_qr_code(None)

        # Schedule the QR code to update every 5 seconds
        Clock.schedule_interval(self.generate_qr_code, 5)

        return layout

    def generate_qr_code(self, dt):
        # Generate a new QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=2,
        )
        qr.add_data('Some data here ' + os.urandom(4).hex())  # Add some random data to the QR code to change it
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qrcode.png')

        # Update the image source to the new QR code
        self.qr_image.source = 'qrcode.png'
        self.qr_image.reload()

        # Show notification popup
        popup = NotificationPopup(title='QR-код обновлен', size_hint=(None, None), size=(300, 100), pos_hint={'center_x': 0.5, 'center_y': 0.80})
        popup.open()

        # Schedule the popup to dismiss after 1 second
        Clock.schedule_once(lambda dt: popup.dismiss(), 1)

if __name__ == '__main__':
    MyApp().run()