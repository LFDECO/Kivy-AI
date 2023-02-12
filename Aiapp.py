from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import openai
Window.size=(375,550)
Builder.load_string(''' 
<SpellWidget>
    GridLayout:
        cols: 1
        height: root.height
        width: root.width
        ScrollView:
            Label:
                id:suggestwords
                text:"Enter Command"
                font_size:25
                text_size: self.width, None
                size_hint_y: None  # Remove size hint to allow explicit height setting
                height: self.texture_size[1]
                background_color:(0.051,0.239,0.239,1)
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos: self.pos
                scroll_y: 1.0
        GridLayout:
            cols:1
            TextInput:
                id:userword
                text:""
                multiline:True
                font_size:25
                size_hint:(0.8,0.7)
            Button:
                id:checkword
                text:"Execute"
                font_size:19
                size_hint:(0.2,0.7)
                background_color:(0,0.6,0.059,1.0)
                background_normal:''
                on_press:root.ai()   
                    
                    ''')

class SpellWidget(Widget):
    def ai(self):
        openai.api_key="Your Secret APi Key"
        prompt=self.ids.userword.text
        mengine="text-davinci-003"
        comp=openai.Completion.create(engine=mengine,prompt=prompt,max_tokens=1024,n=1,stop=None,temperature=0.5)
        response=comp.choices[0].text
        self.ids.suggestwords.text=str(response+'\n')
        
class Ai(App):
    def build(self):
        return SpellWidget()
Ai().run()
