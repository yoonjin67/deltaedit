#!/usr/bin/python3
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk,Gio
import sys
class CAL(Gtk.ApplicationWindow):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		grid=Gtk.Grid.new()
		btn0=Gtk.Button.new_with_label('0')
		btn1=Gtk.Button.new_with_label('1')
		btn2=Gtk.Button.new_with_label('2')
		btn3=Gtk.Button.new_with_label('3')
		btn4=Gtk.Button.new_with_label('4')
		btn5=Gtk.Button.new_with_label('5')
		btn6=Gtk.Button.new_with_label('6')
		btn7=Gtk.Button.new_with_label('7')
		btn8=Gtk.Button.new_with_label('8')
		btn9=Gtk.Button.new_with_label('9')
		grid.attach(btn1,0,0,1,1)
		grid.attach(btn2,1,0,1,1)
		grid.attach(btn3,2,0,1,1)
		grid.attach(btn4,0,2,1,1)
		grid.attach(btn5,1,2,1,1)
		grid.attach(btn6,2,2,1,1)
		grid.attach(btn7,0,4,1,1)
		grid.attach(btn8,1,4,1,1)
		grid.attach(btn9,2,4,1,1)
		grid.attach_next_to(btn0,btn8,Gtk.PositionType.BOTTOM,1,1)
		self.entry=Gtk.Entry();
		grid.attach(self.entry,3,8,1,1)
		btn0.connect('clicked',self.b1)
		btn1.connect('clicked',self.b1)
		btn2.connect('clicked',self.b1)
		btn3.connect('clicked',self.b1)
		btn4.connect('clicked',self.b1)
		btn5.connect('clicked',self.b1)
		btn6.connect('clicked',self.b1)
		btn7.connect('clicked',self.b1)
		btn8.connect('clicked',self.b1)
		btn9.connect('clicked',self.b1)
		plus=Gtk.Button.new_with_label("+")
		plus.connect("clicked",self.pl);
		minus=Gtk.Button.new_with_label("-")
		minus.connect("clicked",self.mn)
		div=Gtk.Button.new_with_label("÷")
		div.connect("clicked",self.dv)
		mult=Gtk.Button.new_with_label("×")
		mult.connect("clicked",self.mt)
		res=Gtk.Button.new_with_label("=")
		res.connect("clicked",self.ev)
		grid2=Gtk.Grid.new()
		grid2.attach(plus,0,0,1,1)
		grid2.attach(minus,1,0,1,1)
		grid2.attach(div,2,0,1,1)
		grid2.attach(mult,0,1,1,1)
		grid2.attach(res,1,1,1,1)
		grid.attach(grid2,0,8,1,1)
		self.add(grid)
		self.show_all()
	def b0(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"0")
	def b1(self,widget):
		txt=str(self.entry.get_text())
		self.entry.set_text(txt+"1")
	def b2(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"2")
	def b3(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"3")
	def b4(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"4")
	def b5(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"5")
	def b6(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"6")
	def b7(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"7")
	def b8(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"8")		
	def b9(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"9")		
	def pl(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"+")		
	def mt(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"*")		
	def dv(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"/")		
	def mn(self,widget):
		txt=str(self.entry.get_text())
		self.entry_set_text(txt+"-")		
	def ev(self,widget):
		txt=entry.get_text()
		self.entry.set_text(eval(text))
class App(Gtk.Application):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,application_id="org.dedit.gcalc",**kwargs)
	def do_startup(self):
		Gtk.Application.do_startup(self)
	def do_activate(self):
		self.window=CAL(application=self,title="GCALC")
app=App()
app.run(sys.argv)
