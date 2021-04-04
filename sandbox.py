#Run this script: 'python sandbox.py' to generate a kivy GUI
#that can reload fresh code from 'reloadable_code.py'
#use keyboard key 'r'

#Happy hacking
#Jonathan Valiente


#Standard libraries
import sys
from importlib import reload #magic library

#Kivy
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

#Reloadable code
import reloadable_code
from reloadable_code import Sandbox_Widget




#Parent structure to facilitate dynmaic code reload
class Sandbox(App):


	def build(self, **kwargs):

		super(Sandbox,self).__init__(**kwargs)

		self.keyboard = Window.request_keyboard(self.keyboard_cleanup, self.root)
		self.keyboard.bind(on_key_down=self.keyboard_trigger)


		
		self.SB_widget = Sandbox_Widget(Window) #Sandbox_Widget is the container whose code changes can be reloaded at will
		self.reload_container = BoxLayout()
		self.reload_container.add_widget(self.SB_widget)

		return self.reload_container



	def keyboard_cleanup(self):
		self.keyboard.unbind(on_key_down=self.keyboard_trigger)
		self.keyboard = None


	def keyboard_trigger(self, keyboard, keycode, text, modifiers):
		#print(self, keyboard, keycode, text, modifiers)



		if keycode[1] == 'r': #this is where the magic happens
			try:
				self.reload_container.remove_widget(self.SB_widget)

				reload(reloadable_code)
				from reloadable_code import Sandbox_Widget

				self.SB_widget = Sandbox_Widget(Window)
				self.reload_container.add_widget(self.SB_widget)

			except:
				print("failed to reload!")
				print(sys.exc_info())


		if keycode[1] == 'c':
			self.SB_widget.clear_canvas()



if __name__ == "__main__":
	app = Sandbox().run()
