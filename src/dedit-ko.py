#!/usr/bin/python3
import gi
import subprocess
from subprocess import Popen
import sys
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
gi.require_version('GtkSource', '4')
from gi.repository import Gtk, GtkSource
from gi.repository import WebKit2 as WebKit
print("DeltaEdit____________________0000 0000 0000 0111")
print("_______________Welcome__________________________")
class AppWindow(Gtk.ApplicationWindow):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.set_default_size(500,800)
		titleforwin=Gtk.HeaderBar()
		titleforwin.props.title="DeltaEdit-'Korean'"
		titleforwin.set_show_close_button(False)
		self.set_titlebar(titleforwin)
		container=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=1)
		buttonwin=Gtk.Button.new_with_label("Popup Memo")
		buttonwin.connect("clicked", self.newwin)
		container.pack_end(buttonwin, True, True, 0)
		self.scrollwin=Gtk.ScrolledWindow()
		self.add(self.scrollwin)
		box = Gtk.Grid.new()
		box.set_row_spacing(1)
		self.scrollwin.add(box)
		self.Text = Gtk.Entry()
		licensetitle="COPYING"
		self.Text.set_text(licensetitle)
		box.attach(self.Text, 0, 0, 1, 1)
		self.Text1 = GtkSource.Buffer()
		gnu="This file is part of DeltaEdit.\nDeltaEdit is free software:\nyou can redistribute it and/\nor modify it\nunder the terms of the\nGNU General Public License\nas published by the Free Software Foundation,\neither version 3 of the License,\nor(at your option) any later version.\nDeltaEdit is distributed in the hope \nthat it will be useful,\nbut WITHOUT ANY WARRANTY;\nwithout even the implied warranty of MERCHANTABILITY\nor FITNESS FOR A PARTICULAR PURPOSE.\nSee the GNU General Public License\nfor more details.\nYou should have received\na copy of the GNU General Public License\nalong with DeltaEdit.\nIf not, see <https://www.gnu.org/licenses/"
		insertstart=self.Text1.get_start_iter()
		self.Text1.insert(insertstart, gnu)
		self.Text1v = GtkSource.View.new_with_buffer(self.Text1)
		self.Text1v.set_tab_width(2)
		box.attach_next_to(self.Text1v, self.Text, Gtk.PositionType.BOTTOM, 1, 1)
		button = Gtk.Button.new_with_label("Save")
		button.connect("clicked", self.Save)
		container.pack_start(button, True, True, 0)
		button2 = Gtk.Button.new_with_label("Open")
		button2.connect("clicked", self.Open)
		container.pack_start(button2, True, True, 0)
		info = Gtk.Button()
		imageattach=Gtk.Image()
		imageattach.set_from_file('/usr/share/pixmaps/dedit_logo.png')
		info.connect("clicked", self.Egg)
		info.add(imageattach)
		container.pack_end(info, True, True, 0)
		cleanbtn = Gtk.Button.new_with_label("*CLEAN ALL LINES*You can't recover deleted lines!")
		cleanbtn.connect("clicked", self.CLEAN)
		box.attach_next_to(cleanbtn, self.Text1v, Gtk.PositionType.BOTTOM, 1, 1)
		lbl = Gtk.Label.new_with_mnemonic("command to Execute/or type URL")
		box.attach_next_to(lbl, cleanbtn, Gtk.PositionType.BOTTOM, 1, 1)
		self.memo = Gtk.Entry()
		self.memo.set_text("put your command!/or Type URL and Press ENTER To go to URL")
		box.attach_next_to(self.memo, lbl, Gtk.PositionType.BOTTOM,  1, 1)
		command = Gtk.Button.new_with_label("EXECUTE!")
		command.connect("clicked", self.Execute)
		box.attach_next_to(command, self.memo, Gtk.PositionType.BOTTOM, 1, 1)
		label_slot=Gtk.Label.new_with_mnemonic("Specify Encoding if you don't like to open it in utf-8 or cp949")
		box.attach_next_to(label_slot, command, Gtk.PositionType.BOTTOM, 1, 1)
		self.paper_encoding=Gtk.Entry()
		self.paper_encoding.set_text("cp949")
		box.attach_next_to(self.paper_encoding, label_slot,Gtk.PositionType.BOTTOM, 1, 1)
		self.helper=Gtk.Button.new_with_label("Show Encoding Helper")
		self.helper.connect("clicked", self.doc)
		box.attach_next_to(self.helper, self.paper_encoding, Gtk.PositionType.BOTTOM, 1, 1)
		self.hide_helper=Gtk.Button.new_with_label("Hide Encoding Helper")
		self.hide_helper.connect("clicked", self.hidedoc)
		box.attach_next_to(self.hide_helper, self.helper, Gtk.PositionType.BOTTOM, 1, 1)
		label_quit=Gtk.Label.new_with_mnemonic("-Description-")
		box.attach_next_to(label_quit, self.hide_helper, Gtk.PositionType.BOTTOM, 1, 1)
		quitbutton=Gtk.Button.new_with_label("Quit Dedit")
		quitbutton.connect("clicked", self.Quit)
		container.pack_end(quitbutton, False, False, 0)
		titleforwin.add(container)
		self.help_buffer=Gtk.TextBuffer()
		self.sherpa=Gtk.TextView(width_request=1, height_request=1, buffer=self.help_buffer)
		box.attach_next_to(self.sherpa, label_quit, Gtk.PositionType.BOTTOM, 1, 1)
		launch_gmemo=Gtk.Button.new_with_label("Execute External Memo App")
		launch_gmemo.connect("clicked", self.gmemo)
		box.attach_next_to(launch_gmemo, self.sherpa, Gtk.PositionType.BOTTOM, 1, 1)
		combine=Gtk.Button.new_with_label("Combine")
		combine.connect("clicked", self.combiner)
		container.pack_start(combine, True, True, 0)
		self.memo.connect("activate", self.webpage)
		self.webview=WebKit.WebView()
		box.attach_next_to(self.webview, self.Text1v, Gtk.PositionType.RIGHT, 1000,1000)
		self.btnforward=Gtk.Button.new_with_label(">")
		self.btnback=Gtk.Button.new_with_label("<")
		self.btnforward.connect("clicked", self.forward)
		self.btnback.connect("clicked", self.back)
		box.attach_next_to(self.btnback,self.webview, Gtk.PositionType.TOP, 1,1)
		box.attach_next_to(self.btnforward,self.btnback,Gtk.PositionType.RIGHT,1,1)
		self.hide_web=Gtk.Button.new_with_label("Hide Web Browser")
		self.hide_web.connect("clicked", self.hide_web_func)
		box.attach_next_to(self.hide_web,self.btnforward,Gtk.PositionType.RIGHT,1,1)
		self.show_web=Gtk.Button.new_with_label("Show Web Browser")
		self.show_web.connect("clicked", self.show_web_func)
		box.attach_next_to(self.show_web,self.hide_web,Gtk.PositionType.RIGHT,1,1)
		self.blanklabel=Gtk.Label.new_with_mnemonic("                                                                                                                                                                                                                                                                                                            ")
		box.attach_next_to(self.blanklabel,self.show_web,Gtk.PositionType.RIGHT,1,1)
		self.webview.load_uri("https://www.google.com/")
		self.langmode=Gtk.Button.new_with_label("Programming Mode")
		box.attach_next_to(self.langmode,launch_gmemo,Gtk.PositionType.BOTTOM,1,1)
		self.langmode.connect("clicked",self.langmod)
		self.langentry=Gtk.Entry()
		self.langentry.set_text('Insert Programming Language')
		box.attach_next_to(self.langentry,self.langmode,Gtk.PositionType.BOTTOM,1,1)
		self.show_all()
		self.show_web.hide()
		self.Text1v.set_highlight_current_line(True)
		start=self.Text1.get_start_iter()
		end=self.Text1.get_end_iter()
		text=self.Text1.get_text(start,end,True)
		self.count=0
	def webpage(self,widget):
		urlget=str(self.memo.get_text())
		wc=urlget[0:4]
		checkhead=urlget[0:8]
		checkhead2=urlget[0:7]
		if checkhead=='https://':
			chkdt=urlget[8:12]
			if chkdt=='www.':
				self.webview.load_uri(urlget)
			else:
				urlget_last=urlget[8:]
				newurl_adj="https://www.%s" % urlget_last
				self.webview.load_uri(newurl_adj)
		elif checkhead2=='http://':
			chkdt__=urlget[7:11]
			if chkdt__=='www.':
				self.webview.load_uri(urlget)
			else:
				urllast=urlget[7:]
				newurl_adj2="http://www.%s" % urllast
				self.webview.load_uri(newurl_adj2)
		elif wc == 'www.':
			try:
				urlll="https://%s" % urlget
				self.webview.load_uri(urlll)
			except:
				urllle="http://%s" % urlget
				self.webview.load_uri(urllle)
		else:
			urllll="https://www.%s" % urlget
			urlllll="http://www.%s" % urlget
			try:
				self.webview.load_uri(urllll)
			except:
				self.webview.load_uri(urlllll)
	def forward(self,widget):
		try:
			self.webview.go_forward()
		except:
			print("BIT_TIME_KS/DEV")
	def back(self,widget):
		try:
			self.webview.go_back()
		except:
			print("@@@~@@@~@@@~BIT_TIME~@@@~@@@~@@@")
	def gmemo(self, widget):
		try:
			Popen('gmemo')
		except:
			Popen('/usr/bin/gmemo')
	def CLEAN(self, widget):
		cleanstart = self.Text1.get_start_iter()
		cleanend = self.Text1.get_end_iter()
		clean = self.Text1.delete(cleanstart, cleanend)
	def Save(self, widget):
		txtpre = self.Text.get_text()
		txtpre= str(txtpre)
		dialog = Gtk.FileChooserDialog("Save...", self, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
		Gtk.FileChooser.set_current_name(dialog, txtpre)
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			savefile = dialog.get_filename()
			startt = self.Text1.get_start_iter()
			endt = self.Text1.get_end_iter()
			text = self.Text1.get_text(startt, endt, True)
			encoding_defined=self.paper_encoding.get_text()
			try:
				with open(savefile, 'w', encoding='utf-8') as f:
					f.write(text)
					f.close()
				dialog.destroy()
			except:
				with open(savefile, 'w', encoding=encoding_defined) as f:
					f.write(text)
					f.close()
				dialog.destroy()
		elif response == Gtk.ResponseType.CANCEL:
			dialog.destroy()
		dialog.destroy()
	def Open(self, widget):
		encoding_defined=self.paper_encoding.get_text()
		start2 = self.Text1.get_start_iter()
		end2 = self.Text1.get_end_iter()
		dialog = Gtk.FileChooserDialog("Open File...", self,  Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			self.Text.set_text("")
			self.Text1.delete(start2, end2)
			w = dialog.get_filename()
			try:
				try:
					with open(w, 'r', encoding='utf8') as f:
						data=f.read()
						self.Text.set_text(w)
						self.Text1.insert(start2,data)
					dialog.destroy()
				except:
					with open(w, 'r', encoding=encoding_defined) as f:
						data=f.read()				
						self.Text.set_text(w)
						self.Text1.insert(start2,data)
					dialog.destroy()
			except:
				dialog.destroy()
		elif response == Gtk.ResponseType.CANCEL:
			dialog.destroy()
		dialog.destroy()
	def combiner(self, widget):
		end1 = self.Text1.get_end_iter()
		dialog = Gtk.FileChooserDialog("Combine...", self,  Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			w = dialog.get_filename()
			encoding_defined=self.paper_encoding.get_text()
			try:
				try:
					with open(w, 'r', encoding='utf-8') as f:
						impdata = f.read()
						self.Text1.insert(end1, impdata)
					dialog.destroy()
				except:
					with open(w, 'r', encoding=encoding_defined) as f:
						impdata=f.read()
						self.Text1.insert(end1, impdata)
					dialog.destroy()
			except:
				dialog.destroy()
		elif response == Gtk.ResponseType.CANCEL:
			dialog.destroy()
		dialog.destroy()
	def Egg(self, widget):
		print("*************")
		print("@#@#@#@#@#@#@")
		print("&&&&&&&&&&&&&")
		print("$   $   $   $")
		print("** *** *** **")
		print("--DeltaEdit--")
	def Execute(self, widget):
		t = self.memo.get_text()
		t = str(t)
		try:
			Popen(t)
		except:
			print("--------____________--------")
	def newwin(self, widget):
		try:
			try:
				Popen("dedit-ko", shell=False)
			except:
				Popen("/usr/bin/dedit-ko", shell=False)
		except:
			print("ERROR")
	def Quit(self, widget):
		print("           Keisung/Bit_Time   ")
		print("DeltaEdit____________________1111 1111 1111 1001")
		print("________________________Turn_Off________________")
		exit()
	def doc(self, widget):
		place=self.help_buffer.get_start_iter()
		place_end=self.help_buffer.get_end_iter()
		document="/etc/dedit/help.txt"
		with open(document, 'r', encoding='utf-8') as f:
			pre_document=f.read()
			document=str(pre_document)
			self.help_buffer.delete(place, place_end)
			self.help_buffer.insert(place, document)
	def hidedoc(self, widget):
		doc_start=self.help_buffer.get_start_iter()
		doc_end=self.help_buffer.get_end_iter()
		self.help_buffer.delete(doc_start, doc_end)
	def hide_web_func(self,widget):
		self.webview.hide()
		self.hide_web.hide()
		self.btnforward.hide()
		self.btnback.hide()
		self.show_web.show()
	def show_web_func(self,widget):
		self.webview.show()
		self.hide_web.show()
		self.btnback.show()
		self.btnforward.show()
		self.show_web.hide()
	def langmod(self,widget):
		self.count+=1
		if (int(self.count%2))!=0:
			language_val=self.langentry.get_text()
			lang=GtkSource.LanguageManager()
			self.Text1.set_language(lang.get_language(language_val))
			self.Text1v.set_auto_indent(True)
			self.Text1v.insert_on_tab(True)
		else:
			lang=GtkSource.LanguageManager()
			self.Text1.set_language(lang.get_language('text'))
class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.dedit.korean",**kwargs)
    def do_startup(self):
        Gtk.Application.do_startup(self)
    def do_activate(self):
        self.window=AppWindow(application=self,title="DeltaEdit-'Korean'") 

app=Application()
app.run(sys.argv)
