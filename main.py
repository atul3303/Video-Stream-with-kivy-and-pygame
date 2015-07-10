import time
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
import socket
import pygame
from threading import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
def image_recv():
	host = ""
	port=5000
	while True:
		global passv
		if passv == 1:
			clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			clientsocket.connect((host, port))
			received = []
			while True:
				recvd_data = clientsocket.recv(230400)
				if not recvd_data:
					break
				else:
					received.append(recvd_data)
			dataset = ''.join(received)
			image = pygame.image.fromstring(dataset,(320,240),"RGB") # convert received image from string
			pygame.image.save(image, '1.jpg')
		else:
			pass
		time.sleep(0)
		

            
class logic(BoxLayout):
	status = StringProperty()
	prev = 1
	def initial(self):
		Clock.schedule_interval(self.update,0)
	def start_vid(self):
		global passv
		passv = 1
	def update(self, *args):
		self.ids.ima.reload()
		
	def stop_clock(self):
		global passv
		passv = 0
		
presentation = Builder.load_file("main3.kv")

new_value = 1
passv = 0

t = Thread(target=image_recv)
t.start()
		
class MainApp(App):
    def build(self):
        return presentation

MainApp().run()

			
