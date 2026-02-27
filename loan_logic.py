from kivy.config import Config

#   setting the dimensions

Config.set("graphics","resizable",0)
Config.set("graphics","width","1200")
Config.set("graphics","height","900")


#   Main App

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


class HomeScreen(Screen):
    pass


class LoanApplicationScreen(Screen):
    pass



class LoanApp(App):
    def build(self):
        sm = ScreenManager()
        #sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoanApplicationScreen(name="application"))
        return sm
    


if __name__ == "__main__":
    LoanApp().run()



