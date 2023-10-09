from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (25/255,255,255,255)


class Comp(BoxLayout):
    pass
   

class Comprador(App):
    def build(self):
        return Comp()

Comprador().run()