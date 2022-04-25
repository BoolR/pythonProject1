from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class Calculator(App):
    def build(self):
        self.formula = ''
        box = BoxLayout(orientation="vertical", padding=15)
        grid = GridLayout(cols=4, spacing=4, size_hint=(1, 0.6))

        self.label = Label(text='0', font_size=35, halign='right', valign='center', size_hint=(1, 0.3),
                           text_size=(400 - 50, 500 * 0.3 - 50))
        box.add_widget(self.label)

        grid.add_widget(Button(text='%', on_press=self.operation, background_color=[1, .58, 0, 1]))
        grid.add_widget(Button(text='√', on_press=self.operation, background_color=[1, .58, 0, 1]))
        grid.add_widget(Button(text='C', on_press=self.clear, background_color=[1, .58, 0, 1]))
        grid.add_widget(Button(text='/', on_press=self.operation, background_color=[1, .58, 0, 1]))
        grid.add_widget(Button(text='7', on_press=self.num, background_color=[.65, .65, .65, 1]))
        grid.add_widget(Button(text='8', on_press=self.num, background_color=[.65, .65, .65, 1]))
        grid.add_widget(Button(text='9', on_press=self.num, background_color=[.65, .65, .65, 1]))
        grid.add_widget(Button(text='*', on_press=self.operation, background_color=[1, .58, 0, 1]))
        grid.add_widget(Button(text='4', on_press=self.num, background_color=[.65, .65, .65, 1]))
        grid.add_widget(Button(text='5', on_press=self.num, background_color=[.65, .65, .65, 1]))
        grid.add_widget(Button(text='6', on_press=self.num, background_color=[.65, .65, .65, 1]))
        grid.add_widget(Button(text='+', on_press=self.operation, background_color=[1, .58, 0, 1]))
        grid.add_widget(Button(text='1', on_press=self.num, background_color=[.65, .65, .65, 1]))
        grid.add_widget(Button(text='2', on_press=self.num, background_color=[.65, .65, .65, 1]))
        grid.add_widget(Button(text='3', on_press=self.num, background_color=[.65, .65, .65, 1]))
        grid.add_widget(Button(text='-', on_press=self.operation, background_color=[1, .58, 0, 1]))
        grid.add_widget(Button(text='000', on_press=self.num, background_color=[1, .58, 0, 1]))
        grid.add_widget(Button(text='0', on_press=self.num, background_color=[.65, .65, .65, 1]))
        grid.add_widget(Button(text='.', on_press=self.num, background_color=[1, .58, 0, 1]))
        grid.add_widget(Button(text='=', on_press=self.result, background_color=[1, .58, 0, 1]))

        box.add_widget(grid)
        return box

    def update(self):
        self.label.text = self.formula

    def num(self, instance):
        self.formula += str(instance.text)
        self.update()

    def operation(self, instance):
        self.formula += str(instance.text)
        self.update()

    def result(self, arg):
        self.label.text = str(eval(self.label.text))
        self.formula = ''

    def clear(self, arg):
        self.formula = ''
        self.update()


if __name__ == "__main__":
    Calculator().run()

