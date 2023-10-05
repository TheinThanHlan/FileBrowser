from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


arr=[1,[1,2,3,4,5,6],3,4,5,6,7,8,9]



class CustomLayout(BoxLayout):
	def __init__(self,name,**kwargs):
		super(CustomLayout,self).__init__(**kwargs)
		print(name)

class MainLayout(BoxLayout):
	def __init__(self,**kwargs):
		super(MainLayout,self).__init__(**kwargs)
		for a in arr:
			if(type(a)==type(list())):
				c=CustomLayout(name="___")
				for b in a:
					c.add_widget(CustomLayout(name=b))
							
				self.add_widget(c)

			else:
				self.add_widget(CustomLayout(name=a))

class TestApp(App):
	def build(self):
		return MainLayout()


if __name__=="__main__":
	TestApp().run()
