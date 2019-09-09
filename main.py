from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

class Space(ScreenManager):
    def __init__(self):
        super(Space, self).__init__()
        self.Inicio=Home(name="inicio", Space=self)
        self.add_widget(self.Inicio)
        self.DetalleLibro=p(name="detallelibro", Space=self)
        self.add_widget(self.DetalleLibro)

    def CambiarPantalla(self, texto):
        self.DetalleLibro.CambiarTexto(texto)
        self.current="detallelibro"
    def CambiarPantalla2(self):
        self.current="inicio"

class p(Screen):
    def __init__(self, name, Space):
        super(p,self).__init__()
        self.Space=Space
        self.name=name
    
    def CambiarTexto(self, texto):
        self.ids.button.text=texto

class Home(Screen):
    def Hola(self,dato, **kwargs):
        print(dato)

    def __init__(self, name, Space):
        super(Home,self).__init__()
        self.name=name
        self.Space=Space
        self.nombres=["Hola", "Mundo", "Estos", "son", "Ejemplos", "De como se veria", "Matar a pedro", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i in self.nombres:
            self.ids.grid.add_widget(MiniaturasHome(self.Space, i))
    
class MiniaturasHome(Button):
    def __init__(self, Space, texto):
        super(MiniaturasHome,self).__init__()
        self.Space=Space
        self.dato=texto
        self.text=texto
        #self.bind(on_press=self.Hola)
    def Hola(self):
        print("hola")

class CTWApp(App):
    def build(self):
        return Space()


if __name__=="__main__":
    CTWApp().run()
