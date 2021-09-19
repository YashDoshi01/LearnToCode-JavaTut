import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class LearnJava(App):
    def build(self):
        return Label(text='Hello Word!')





if __name__=='__main__':
    LearnJava().run()


