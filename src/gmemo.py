#!/usr/bin/python3
import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class AppWindow(Gtk.ApplicationWindow):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.set_default_size(500,500)
		m=Gtk.TextBuffer()
		memo=Gtk.TextView(buffer=m)
		self.add(memo)
		self.show_all()
class Application(Gtk.Application):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, application_id="org.dedit.memo",**kwargs)
	def do_startup(self):
		Gtk.Application.do_startup(self)
	def do_activate(self):
		self.window=AppWindow(application=self,title="Gmemo") 
app=Application()
app.run(sys.argv)
