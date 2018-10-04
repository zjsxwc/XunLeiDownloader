#!/usr/bin/python
# -*- coding: utf-8 -*


from XunLeiDownloader import XunLeiDownloader;
import urllib2
import time
import sys

# 解决中文转码
reload(sys)
sys.setdefaultencoding( "utf-8" )


url = "http:/<host>:<port>/task.php?type=fetch_task"
while True:
	req = urllib2.Request(url)
	if (req):
		try:
			res_data = urllib2.urlopen(req)
			task = res_data.read()
			if (task):
				print task
				xld = XunLeiDownloader()
				xld.startDownload(task)
				xld = None
		
		except:
			pass
	time.sleep(5)




