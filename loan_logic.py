from kivy.config import Config

#   setting the dimensions

Config.set("graphics","resizable",1)
Config.set("graphics","width","1200")
Config.set("graphics","height","900")


#   Main App

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

class MyManager(ScreenManager):
    def __init__(self, **kwargs):
        Builder.load_file("login.kv")
        Builder.load_file("requirement.kv")
        Builder.load_file("requirement2.kv")
        Builder.load_file("registering_member/account_info.kv")
        Builder.load_file("registering_member/contact_info.kv")
        Builder.load_file("registering_member/financial_info.kv")
        Builder.load_file("registering_member/personal_info.kv")

        super().__init__(**kwargs)
        self.add_widget(HomeScreen(name = 'home'))
        self.add_widget(LoanApplicationScreen(name='login'))
        self.add_widget(RequirementScreen(name='apply'))
        self.add_widget(RequirementScreen2(name='apply2'))
        self.add_widget(AccountInfo(name='accountinfo'))
        self.add_widget(PersonalInfo(name='personalinfo'))
        self.add_widget(FinancialInfo(name='financialinfo'))
        self.add_widget(ContactInfo(name='contactinfo'))
        



class AccountInfo(Screen):
    pass





class FinancialInfo(Screen):
    pass





class ContactInfo(Screen):
    pass



class PersonalInfo(Screen):
    pass



class RequirementScreen(Screen):
    pass


class RequirementScreen2(Screen):
    pass




class HomeScreen(Screen):
    def contact_us(self,widget):
        layout = BoxLayout(padding = 10,orientation = 'vertical')
        message = Label(text='Our Help Services\n1. Call us on: +256-7394-836939\n2.WhatsApp: .........',font_size = '35')
        ok_button = Button(text='OK',size_hint=(.4,.25),pos_hint = {'center_x': .5})

        layout.add_widget(message)
        layout.add_widget(ok_button)

        popup_menu = Popup(title = "Contact Info",content = layout,size_hint=(.8,.4))

        popup_menu.open()

        ok_button.bind(on_release = popup_menu.dismiss)


    def faq(self,widget):
        layout = BoxLayout(padding = 10,orientation = 'vertical')
        message = Label(text='Ooops!! Sorry this service is unavailable at the moment\n\nTry Again Later',font_size = '35')
        ok_button = Button(text='OK',size_hint=(.4,.25),pos_hint = {'center_x': .5})

        layout.add_widget(message)
        layout.add_widget(ok_button)

        popup_menu = Popup(title = "FAQs",content = layout,size_hint=(.8,.4))

        popup_menu.open()

        ok_button.bind(on_release = popup_menu.dismiss)


    def about_us(self,widget):
        layout = BoxLayout(padding = 10,orientation = 'vertical')
        message = Label(text='Ooops!! Sorry this service is unavailable at the moment\n\nTry Again Later',font_size = '35')
        ok_button = Button(text='OK',size_hint=(.4,.25),pos_hint = {'center_x': .5})

        layout.add_widget(message)
        layout.add_widget(ok_button)

        popup_menu = Popup(title = "About US",content = layout,size_hint=(.8,.4))

        popup_menu.open()

        ok_button.bind(on_release = popup_menu.dismiss)





class LoanApplicationScreen(Screen):

    def checkBalance(self,widget):
        layout = BoxLayout(padding = 10,orientation = 'vertical')
        message = Label(text='Your Account Balance is Ugx 250,000.34',font_size = '35')
        ok_button = Button(text='OK',size_hint=(.4,.25),pos_hint = {'center_x': .5})

        layout.add_widget(message)
        layout.add_widget(ok_button)

        popup_menu = Popup(title = "Balance Inquiry",content = layout,size_hint=(.8,.4))

        popup_menu.open()

        ok_button.bind(on_release = popup_menu.dismiss)







    def checkLoanStatus(self,widget):
        layout = BoxLayout(padding = 10,orientation = 'vertical')
        message = Label(font_size='25',text='Your Loan Request has been submitted,\nIt is under review.\nWe will let you know once review is done')
        ok_button = Button(text='OK',size_hint=(.4,.25),pos_hint = {'center_x':.5})

        layout.add_widget(message)
        layout.add_widget(ok_button)

        popup_menu = Popup(title = "Loan Status",content = layout,size_hint=(.6,.5))

        popup_menu.open()

        ok_button.bind(on_release = popup_menu.dismiss)





class LoanApp(App):
    def build(self):
        return MyManager()
    


if __name__ == "__main__":
    LoanApp().run()



