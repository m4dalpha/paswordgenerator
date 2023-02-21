from kivy.app import App
from kivy.lang import Builder
import passwords as generate

KV = """
FloatLayout:
    Label:
        text: "Generated Password!"
        size_hint: [0.4, 0.2]
        pos_hint: {'top': 0.8, "right": 0.4}
        font_size: "30sp"
        bold: True

    TextInput:
        id: txt
        size_hint: [0.5, 0.2]
        pos_hint: {'top' :0.8, "center_x": .7}
        font_size: "60sp"
        bold: True
        multiline: False

    Label:
        text: "Input the Password length:"
        size_hint: [0.4, 0.2]
        pos_hint: {'top': 0.5, "right": 0.4}
        font_size: "20sp"
        bold: True

    TextInput:
        id: pw_length
        size_hint: [0.5, 0.2]
        pos_hint: {'top' :0.5, "center_x": .7}
        font_size: "60sp"
        bold: True
        multiline: False
        input_type: 'number'

    Button:
        text: "Generate a password!"
        size_hint: [0.5, 0.2]
        pos_hint: {'bottom':0.5, "center_x": 0.5}
        font_size: "20sp"
        bold: True
        background_normal: ""
        background_color: [1,0,0,1]
        color: [0,0,0,1]
        on_release:
            txt.text = app.pw_gener().password_generator(int(pw_length.text))
"""

class MyApp(App):
    title = "Password Generator v.1"
    icon = "logo32x32.png"

    def build(self):
        return Builder.load_string(KV)

    def pw_gener(self):
        return generate

if __name__ == "__main__":
    app = MyApp()
    app.run()
