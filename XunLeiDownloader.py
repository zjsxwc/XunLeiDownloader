#!/usr/bin/python
# -*- coding: utf-8 -*

# 该脚本依赖pywin32，需要保证已经执行了  `pip install pywin32`

# 存在一个迅雷BUG，一定要在迅雷已经启动的情况下执行本脚本，
# 如果是从本脚本启动迅雷那么第一个下载会报连接超时而下载失败

import win32gui
import win32api
import win32con
import win32clipboard
from ctypes import *

import os
import time
import sys

# 解决中文转码
reload(sys)
sys.setdefaultencoding( "utf-8" )



class XunLeiDownloader:
	xunleiExePath = ""

	def __init__(self, xunleiExePath = r"C:\Program Files (x86)\Thunder Network\Thunder9\Program\Thunder.exe"):
		self.xunleiExePath = xunleiExePath

	def ctrlV(self):
		win32api.keybd_event(win32con.VK_CONTROL, 0,0,0)
		time.sleep(0.1)
		win32api.keybd_event(ord('V'), 0,0,0)
		time.sleep(0.1)
		win32api.keybd_event(ord('V'), 0,win32con.KEYEVENTF_KEYUP,0)
		time.sleep(0.1)
		win32api.keybd_event(win32con.VK_CONTROL, 0,win32con.KEYEVENTF_KEYUP,0)

	def leftMouseClick(self, posX, posY):
		win32api.SetCursorPos([posX, posY])
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
		time.sleep(0.5)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
		time.sleep(0.5)	


	def startDownload(self, downloadUrls):
		gdi32 = windll.gdi32
		user32 = windll.user32
		hdc = user32.GetDC(None)

		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardData(win32con.CF_TEXT, "")
		win32clipboard.CloseClipboard()

		os.startfile(self.xunleiExePath)
		wndMain = None
		while not wndMain:
			time.sleep(1)
			wndMain = win32gui.FindWindow(None, u"迅雷")
		wndMainRect = win32gui.GetWindowRect(wndMain)
		self.leftMouseClick(wndMainRect[0]+35, wndMainRect[1]+100)
		time.sleep(0.1)
		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardData(win32con.CF_TEXT, downloadUrls.decode('utf-8').encode('gbk'))
		win32clipboard.CloseClipboard()

		wndCreateDownload = win32gui.FindWindow(None, u"新建下载")
		
		if wndCreateDownload:
			wndCreateDownloadRect = win32gui.GetWindowRect(wndCreateDownload)
			self.leftMouseClick(wndCreateDownloadRect[0]+60, wndCreateDownloadRect[1]+70)
			self.ctrlV()
			self.leftMouseClick(wndCreateDownloadRect[0]+10, wndCreateDownloadRect[1]+10)
			
			win32api.SetCursorPos([wndCreateDownloadRect[0] + 150,wndCreateDownloadRect[1]+ 215])
			time.sleep(1)
			c = gdi32.GetPixel(hdc,wndCreateDownloadRect[0] + 150,wndCreateDownloadRect[1]+ 215)
			chex = hex(c)
			print chex
			if ((chex == "0xfefefe") or (chex == "0xffffff")):
				# 开始下载
				self.leftMouseClick(wndCreateDownloadRect[2]-150, wndCreateDownloadRect[3]-250)
			else:
				# 无效链接地址取消下载
				self.leftMouseClick(wndCreateDownloadRect[2]-30, wndCreateDownloadRect[1]+15)
			

			print "关闭[新建下载]\r\n"
			alreadyExistDlg = win32gui.FindWindowEx(None,None,'XLUEModalHostWnd',"MessageBox")
			if alreadyExistDlg:
				alreadyExistDlgRect = win32gui.GetWindowRect(alreadyExistDlg)
				self.leftMouseClick(alreadyExistDlgRect[0]+390, alreadyExistDlgRect[1]+35)
				# win32gui.SendMessage(wndCreateDownload, win32con.WM_CLOSE) 这么关闭迅雷自己撸的非标准GUI框架窗体会有BUG
		else:
			print "[新建下载]不存在\r\n"
