#!/bin/env python
# version: 0.01
# author: Minto Joseph
# email: mintojoseph@gmail.com
# Timer which would interrupt you after specified number of seconds.
# Requires wxPython

import sys
import datetime
import time
try:
	import wx
except ImportError:
	sys.exit("Please install wxPython")

class MyFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self,None)
		m_close = wx.Button(self, id=-1)
		m_close.Bind(wx.EVT_BUTTON, self.OnClose)
		m_close.SetToolTip(wx.ToolTip("ALARM!!! Click to hide"))

	def OnClose(self, event):
		self.Close(True)
try:
	time_new=float(raw_input("After how many seconds you need to be interrupted?: "))
except (ValueError):
	sys.exit("Error: Please enter an integer")

time_now=time.time()
time_trigg=time_now+time_new

while time_now<=time_trigg:
	time_now=time.time()


app = wx.App()
Frame = MyFrame()
Frame.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
app.MainLoop()
