#!/usr/bin/python3
import subprocess
from subprocess import call, Popen
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class WIN(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="INSTALLER")
        _all=Gtk.Button.new_with_label("ALL")
        _all.connect("clicked", self.INST_ALL)
        self.add(_all)
    def INST_ALL(self,widget):
        try:
            call('./Install.sh')
            ww=Gtk.Window()
            ll=Gtk.Label.new_with_mnemonic("SUCCESSFULLY INSTALLED")
            ww.add(ll)
            ww.connect("destroy", Gtk.main_quit)
            ww.show_all()
            Gtk.main()
        except:
            w=Gtk.Window()
            l=Gtk.Label.new_with_mnemonic("INSTALL FAILED")
            w.add(l)
            w.connect("destroy", Gtk.main_quit)
            w.show_all()
            Gtk.main()
win=WIN()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
