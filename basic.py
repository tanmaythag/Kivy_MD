
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
	def build(self):
		f=FloatLayout()
		s= Scatter()
		l = Label(text="Tanmay",font_size=140)
		
		f.add_widget(s)
		s.add_widget(l)
		return f
	
if __name__ == "__main__":
	TestApp().run()