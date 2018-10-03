
借助win32接口，使用迅雷下载

该脚本依赖pywin32，需要保证已经执行了  `pip install pywin32`，我目前是 Python 2.7 的环境。

存在一个迅雷BUG，一定要在迅雷已经启动的情况下执行本脚本，如果是从本脚本启动迅雷那么第一个下载会报连接超时而下载失败。

```
xld = XunLeiDownloader()

xld.startDownload("http://cdn2.ime.sogou.com/6d5e6e18998276c3bff1bc6b69da3ee6/5bb4638d/dl/index/1535443172/sogou_pinyin_91a.exe")
```


