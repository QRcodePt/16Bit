from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.config import Config

import qrcode

Config.set ("graphics", "width", 400)
Config.set ("graphics", "height", 700)

class NotificationPopup(Popup):
    pass

class MyApp(App):
    def build(self):
        layout = FloatLayout()

        button1 = Button(text='Уведомление при сканировании', size_hint=(None, None), size=(200, 100), pos_hint={'center_x': 0.5, 'center_y': 0.85}) # Здесь вы можете установить ширину (200) и высоту (100) кнопки
        button1.bind(on_press=self.show_notification)
        self.qr_image = Image(source='')
        layout.add_widget(button1)
        layout.add_widget(self.qr_image)

        return layout
    def show_notification(self, instance):
        popup = NotificationPopup(title='QR код был отсканирован', size_hint=(None, None), size=(300, 100), pos_hint={'center_x': 0.5, 'center_y': 0.80})
        popup.open()
        
    def on_start(self):
        self.generate_qr_code(None)    
    
    def generate_qr_code(self, instance):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=2,
        )
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qrcode.png')

        self.qr_image.source = 'qrcode.png'
    

if __name__ == '__main__':
    MyApp().run()