from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.display = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        self.add_widget(self.display)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "=", "+"],
            ["C", "sqrt", "sin", "cos"]
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.add_widget(h_layout)

    def on_button_press(self, instance):
        text = instance.text
        if text == "C":
            self.display.text = ""
        elif text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = "Error"
        elif text == "sqrt":
            try:
                self.display.text = str(math.sqrt(float(self.display.text)))
            except Exception:
                self.display.text = "Error"
        elif text == "sin":
            try:
                self.display.text = str(math.sin(math.radians(float(self.display.text))))
            except Exception:
                self.display.text = "Error"
        elif text == "cos":
            try:
                self.display.text = str(math.cos(math.radians(float(self.display.text))))
            except Exception:
                self.display.text = "Error"
        else:
            self.display.text += text

class ScientificCalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    ScientificCalculatorApp().run()