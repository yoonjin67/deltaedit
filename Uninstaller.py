#!/usr/bin/python3
import subprocess
from subprocess import call
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class WIN(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="UNINSTALLER")
		grid=Gtk.Grid()
		self.add(grid)
		ko=Gtk.Button("KOREAN")
		jp=Gtk.Button("JAPANESE")
		cn=Gtk.Button("CHINESE")
		all=Gtk.Button("ALL")
		grid.attach(ko,0,0,1,1)
		grid.attach_next_to(jp,ko,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(cn,jp,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(all,jp,Gtk.PositionType.BOTTOM,1,1)
		ko.connect("clicked", self.kor)
		jp.connect("clicked",self.jpn)
		cn.connect("clicked",self.chn)
		all.connect("clicked", self.INST_ALL)
	def INST_ALL(self,widget):
		try:
			call('./Uninstall.sh')
			ww=Gtk.Window()
			ll=Gtk.Label("SUCCESSFULLY UNINSTALLED")
			ww.add(ll)
			ww.connect("destroy", Gtk.main_quit)
			ww.show_all()
		except:
			w=Gtk.Window()
			l=Gtk.Label("UNINSTALL FAILED")
			w.add(l)
			w.connect("destroy", Gtk.main_quit)
			w.show_all()
			Gtk.main()
	def kor(self,widget):
		try:
			call('./Uninstall_ko.sh')
			ww=Gtk.Window()
			ll=Gtk.Label("SUCCESSFULLY UNINSTALLED")
			ww.add(ll)
			ww.connect("destroy", Gtk.main_quit)
			ww.show_all()
		except:
			w=Gtk.Window()
			l=Gtk.Label("UNINSTALL FAILED")
			w.add(l)
			w.connect("destroy", Gtk.main_quit)
			w.show_all()
	def jpn(self,widget):
		try:
			call('./Uninstall_jp.sh')
			ww=Gtk.Window()
			ll=Gtk.Label("SUCCESSFULLY UNINSTALLED")
			ww.add(ll)
			ww.connect("destroy", Gtk.main_quit)
			ww.show_all()
		except:
			w=Gtk.Window()
			l=Gtk.Label("UNINSTALL FAILED")
			w.add(l)
			w.connect("destroy", Gtk.main_quit)
			w.show_all()
	def chn(self,widget):
		try:
			call('./Uninstall_cn.sh')
			ww=Gtk.Window()
			ll=Gtk.Label("SUCCESSFULLY UNINSTALLED")
			ww.add(ll)
			ww.connect("destroy", Gtk.main_quit)
			ww.show_all()
		except:
			w=Gtk.Window()
			l=Gtk.Label("UNINSTALL FAILED")
			w.add(l)
			w.connect("destroy", Gtk.main_quit)
			w.show_all()
win=WIN()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
