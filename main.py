from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class PurlinMobileApp(App):
    def build(self):
        self.title = "Tra Dung Sai Xà Gồ AS/NZS"
        # Dữ liệu độ mạ
        self.zinc_data = {
            "Z70": 0.0098, "Z80": 0.0112, "Z100": 0.0140, "Z120": 0.0168,
            "Z180": 0.0252, "Z200": 0.0280, "Z275": 0.0385, "Z350": 0.0490, "Z450": 0.0630
        }

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Tiêu đề
        layout.add_widget(Label(text="TRA DUNG SAI XÀ GỒ", font_size='24sp', bold=True, color=(0, 0.5, 1, 1)))

        # Nhập BMT
        layout.add_widget(Label(text="Nhập độ dày thép nền BMT (mm):", halign='left', text_size=(Window.width - 40, None)))
        self.input_bmt = TextInput(text='1.6', multiline=False, input_filter='float', font_size='20sp', size_hint_y=None, height='50dp')
        layout.add_widget(self.input_bmt)

        # Chọn độ mạ
        layout.add_widget(Label(text="Chọn loại mạ kẽm (Z):"))
        self.spinner = Spinner(text='Z275', values=list(self.zinc_data.keys()), size_hint_y=None, height='50dp')
        layout.add_widget(self.spinner)

        # Nút tính toán
        btn = Button(text="TÍNH TOÁN", background_color=(0, 0.4, 0.8, 1), font_size='20sp', size_hint_y=None, height='60dp')
        btn.bind(on_press=self.calculate)
        layout.add_widget(btn)

        # Hiển thị kết quả
        self.result_label = Label(text="Kết quả sẽ hiển thị ở đây", font_size='16sp', halign='center', color=(1, 1, 1, 1))
        layout.add_widget(self.result_label)

        return layout

    def get_tolerance(self, bmt):
        if bmt <= 0.30: return 0.02
        elif 0.30 < bmt <= 0.50: return 0.03
        elif 0.50 < bmt <= 0.80: return 0.04
        elif 0.80 < bmt <= 1.20: return 0.05
        elif 1.20 < bmt <= 1.60: return 0.06
        elif 1.60 < bmt <= 2.00: return 0.07
        elif 2.00 < bmt <= 2.50: return 0.08
        elif 2.50 < bmt <= 3.00: return 0.09
        elif 3.00 < bmt <= 4.00: return 0.10
        return None

    def calculate(self, instance):
        try:
            bmt = float(self.input_bmt.text)
            zinc_type = self.spinner.text
            t_zinc = self.zinc_data[zinc_type]
            
            tol = self.get_tolerance(bmt)
            if tol:
                b_min = bmt - tol
                tct_min = b_min + t_zinc
                self.result_label.text = (
                    f"Dung sai: ±{tol} mm\n"
                    f"BMT tối thiểu: {b_min:.3f} mm\n"
                    f"TCT TỐI THIỂU (CẦN ĐO): {tct_min:.3f} mm"
                )
            else:
                self.result_label.text = "Ngoài phạm vi tiêu chuẩn!"
        except:
            self.result_label.text = "Vui lòng nhập số hợp lệ!"

if __name__ == '__main__':
    PurlinMobileApp().run()