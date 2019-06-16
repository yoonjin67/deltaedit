#!/usr/bin/python3
import subprocess
from subprocess import call, Popen
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class WIN(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="INSTALLER")
		grid=Gtk.Grid()
		self.add(grid)
		pre_installation=Gtk.Button("Click before Installation")
		ko=Gtk.Button("KOREAN")
		jp=Gtk.Button("JAPANESE")
		cn=Gtk.Button("CHINESE")
		all=Gtk.Button("ALL")
		grid.attach(ko,0,0,1,1)
		grid.attach_next_to(jp,ko,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(cn,jp,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(all,jp,Gtk.PositionType.BOTTOM,1,1)
		grid.attach_next_to(pre_installation,all,Gtk.PositionType.BOTTOM,1,1)
		ko.connect("clicked", self.kor)
		jp.connect("clicked",self.jpn)
		cn.connect("clicked",self.chn)
		all.connect("clicked", self.INST_ALL)
		pre_installation.connect("clicked", self.CHMOD)
	def INST_ALL(self,widget):
		try:
			call('./Install.sh')
			ww=Gtk.Window()
			ll=Gtk.Label("SUCCESSFULLY INSTALLED")
			ww.add(ll)
			ww.connect("destroy", Gtk.main_quit)
			ww.show_all()
			Gtk.main()
		except:
			w=Gtk.Window()
			l=Gtk.Label("INSTALL FAILED")
			w.add(l)
			w.connect("destroy", Gtk.main_quit)
			w.show_all()
			Gtk.main()
	def kor(self,widget):
		try:
			call('./Inst_ko.sh')
			ww=Gtk.Window()
			ll=Gtk.Label("SUCCESSFULLY INSTALLED")
			ww.add(ll)
			ww.connect("destroy", Gtk.main_quit)
			ww.show_all()
			Gtk.main()
		except:
			w=Gtk.Window()
			l=Gtk.Label("INSTALL FAILED")
			w.add(l)
			w.connect("destroy", Gtk.main_quit)
			w.show_all()
			Gtk.main()
	def jpn(self,widget):
		try:
			call('./Inst_jp.sh')
			ww=Gtk.Window()
			ll=Gtk.Label("SUCCESSFULLY INSTALLED")
			ww.add(ll)
			ww.connect("destroy", Gtk.main_quit)
			ww.show_all()
			Gtk.main()
		except:
			w=Gtk.Window()
			l=Gtk.Label("INSTALL FAILED")
			w.add(l)
			w.connect("destroy", Gtk.main_quit)
			w.show_all()
			Gtk.main()
	def chn(self,widget):
		try:
			call('./Inst_cn.sh')
			ww=Gtk.Window()
			ll=Gtk.Label("SUCCESSFULLY INSTALLED")
			ww.add(ll)
			ww.connect("destroy", Gtk.main_quit)
			ww.show_all()
			Gtk.main()
		except:
			w=Gtk.Window()
			l=Gtk.Label("INSTALL FAILED")
			w.add(l)
			w.connect("destroy", Gtk.main_quit)
			w.show_all()
			Gtk.main()
	def CHMOD(self,widget):
		Popen("sudo chmod 777 /etc/dedit/output && sudo chmod 777 /etc/dedit/.dedit_cfunc.c")
win=WIN()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
