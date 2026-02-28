from kivy.config import Config

#   setting the dimensions

Config.set("graphics","resizable",0)
Config.set("graphics","width","1200")
Config.set("graphics","height","900")


#   Main App

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang.builder import Builder

class MyManager(ScreenManager):
    def __init__(self, **kwargs):
        Builder.load_file("login.kv")
        Builder.load_file("requirement.kv")
        Builder.load_file("requirement2.kv")

        super().__init__(**kwargs)
        self.add_widget(HomeScreen(name = 'home'))
        self.add_widget(LoanApplicationScreen(name='login'))
        self.add_widget(RequirementScreen(name='apply'))
        self.add_widget(RequirementScreen2(name='apply2'))


class RequirementScreen(Screen):
    pass


class RequirementScreen2(Screen):
    pass




class HomeScreen(Screen):
    pass


class LoanApplicationScreen(Screen):
    pass



class LoanApp(App):
    def build(self):
        return MyManager()
    


if __name__ == "__main__":
    LoanApp().run()



