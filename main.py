import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class connect(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 2

            
        self.add_widget(Label(text = "Enter your name:"))
        
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)
    
        
        
        self.add_widget(Label(text = "Enter your course:"))
        
        self.crs = TextInput(multiline = False)
        self.add_widget(self.crs)
        
        
        
        self.add_widget(Label(text = "enter your age:"))
        
        self.age = TextInput(multiline = False)
        self.add_widget(self.age)


        self.add_widget(Label(text = "Date of enquiry:"))
        
        self.doe = TextInput(multiline = False)
        self.add_widget(self.doe)

        self.add_widget(Label())
        self.submit = Button(text = "submit")
        self.submit.bind(on_press = self.saved)
        self.add_widget(self.submit)

    
    def saved(self,instance):
        name = self.name.text
        course = self.crs.text
        age = self.age.text
        doe = self.doe.text

        print(f"your name is {name} and your respected course is {course},your age is {age} and the doe is {doe}")

        
        f = open("D:\\visual studio code\\python programs\\collected.txt","a+") 
        f.write(f"\n{name}\t {course}\t {age}\t {doe}\n")
        
        f.close()

class mainapp(App):
    def build(self):
        return connect()

if __name__ == "__main__":
    mainapp().run()
