#code written here can be reloaded dynamically using the keyboard key 'r'
#without having to run python over and over again -- those 10 seconds add up :)



from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.graphics import *

#import numpy
#import pandas
import random 
import math





#this class will be imported in sandbox.py and can be reloaded dynamically
class Sandbox_Widget(BoxLayout):

	def __init__(self,  window, **kwargs):
		super(Sandbox_Widget, self).__init__(**kwargs)

		Clock.schedule_interval(self.update, 1/60) #scheduled in Kivy to run every 1/60 of a second

		
		self.window=window
		self.window_size_x = window.size[0]
		self.window_size_y = window.size[1]
		self.center = [window.size[0]/2, window.size[1]/2]

	


	#scheduled in Kivy to run every 1/60 of a second
	def update(self, time_since_call):

		self.canvas.clear()
		with self.canvas:

			Color(1, 1, 1, 1) #change the color and try it :)
			Line(circle=(self.window_size_x/2, self.window_size_y/2, 50))



	# def on_motion(self, window, pos): 
		# response =  super(Sandbox_Widget, self).on_motion(touch)
		# if response:
		# 	print(touch)
		# 	return response
		# self.draw_pos[0], self.draw_pos[1] = pos

		# self.circle_radius = pos[0]
		#self.number_of_objects += 1
		#self.drawing_container.append(Circles(position=pos, count = self.number_of_objects))
		# pass
	



	# def on_touch_down(self, touch): 
	# 	self.number_of_objects += 1
	# 	self.drawing_container.append(Circles(position=touch.pos, count = self.number_of_objects))


	def clear_canvas(self):
		self.canvas.clear()

