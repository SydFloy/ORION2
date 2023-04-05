from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.actionbar import ActionBar
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.widget import Widget
import webbrowser
#import os




Window.clearcolor=(141/255.0,90/255.0,165/255.0,255)
#Window.size=(400,600)
class WindowManager(ScreenManager):
    pass
class Logscreen(Screen):
     def on_touch_move(self, touch):
        if touch.dx > 50:
            # swipe right, change to previous screen
            self.manager.transition.direction = 'right'
            self.manager.current = 'main'
   
class Harromanscreen(Screen):
    pass
class Mainscreen(Screen):
    pass
class Secondscreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
            # swipe right, change to previous screen
            self.manager.transition.direction = 'right'
            self.manager.current = 'main'
        
        
class Geascreen(Screen):
  def on_touch_move(self, touch):
        if touch.dx > 50:
            
            self.manager.transition.direction = 'right'
            self.manager.current = 'main'
        
class Glattscreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
                
            self.manager.transition.direction = 'right'
            self.manager.current = 'main'
        
class Harroscreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
                
            self.manager.transition.direction = 'right'
            self.manager.current = 'main'
        
class Lastscreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
                
            self.manager.transition.direction = 'right'
            self.manager.current = 'main'
        
class Hongascreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
                
            self.manager.transition.direction = 'right'
            self.manager.current = 'main'
        
class Pgeascreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
                
            self.manager.transition.direction = 'right'
            self.manager.current = 'Gea'
        
class Egeascreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
                
            self.manager.transition.direction = 'right'
            self.manager.current = 'Gea'
            

kv=Builder.load_file('main.kv')
class MymainApp(App):
    def build(self):
        self.title='boutkhil'
        return kv  
    def lunch_link(self,index):
        if index == 0:
             link='https://drive.google.com/file/d/1qPrWXyv0VOlKMf0zZPr5DIQ6sZ3khVoR/view?usp=share_link'
        elif index == 1 :
            link='https://drive.google.com/file/d/1q57LywhdRWs6BocEVKC_5P-huqx1j40t/view?usp=share_link'
        elif index == 2 :
            link='https://drive.google.com/file/d/11d2IccAGjcP1BIp2TUIMk6WxQBUrbXG_/view?usp=share_link'
         
        elif index == 3 :
            link='https://drive.google.com/file/d/1JWaXKDGebje2HzZe4v0XS7rIUuEFN5Xy/view?usp=share_link'
        elif index == 4 :
            link='https://drive.google.com/file/d/1YUTOxm63kqXH8ytM-2p0xePRMzkOhqYy/view?usp=share_link'
        elif index == 5 : 
            link='https://drive.google.com/file/d/1jiAPjqHKUjhp7vDGp3QtKhedO_jbzBld/view?usp=share_link' 
        elif index == 6 :
            link='https://drive.google.com/file/d/1_xVMauxgu2qNrzmJMck4LpZvcfVPiQPM/view?usp=share_link'
        elif index == 7 :
            link='https://drive.google.com/file/d/1rvjwNSu8KCxXi7jlfsdttOCOwkacYU2z/view?usp=share_link'
        elif index == 8 :
            link='https://drive.google.com/file/d/122vqQ-eupJXTiEr_v73Nv9VHGGnk8Ds6/view?usp=share_link'
        elif index == 9 :
            link='https://drive.google.com/file/d/1SwTasyTgP58qUmE9g-m2Yc3MdASKEs2Q/view?usp=share_link'
        elif index == 10:
            link='https://drive.google.com/file/d/1RPLZ207SQzmcvmf6az3R0YUWsXL1k6_k/view?usp=share_link'


    
        webbrowser.open(link)
   # def pdf_luncher(self,num):
        #if num == 0 :
           # path='Kivy.pdf'
       # os.startfile(path)

       
       
     

MymainApp().run()
