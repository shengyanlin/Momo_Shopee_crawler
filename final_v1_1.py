import sys
import math
import time
import copy
import random
import requests
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

now = dt.datetime.now()
#only kepp the "now" into hh:mm
now = now.strftime("%H_%M")
now = str(now)

begin = dt.datetime.now()

def generate_random_header():
    random_user_agents = {'chrome': ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
      'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
      'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
      'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36',
      'Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
      'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14'],
     'opera': ['Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
      'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
      'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
      'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
      'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00',
      'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00',
      'Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00',
      'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00',
      'Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0',
      'Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62',
      'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62',
      'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
      'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',
      'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51',
      'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',
      'Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50',
      'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
      'Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11',
      'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11',
      'Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10',
      'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10',
      'Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10',
      'Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; U; en) Presto/2.8.149 Version/11.1',
      'Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 5.1; U;) Presto/2.7.62 Version/11.01',
      'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62 Version/11.01',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
      'Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
      'Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01',
      'Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00',
      'Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.1; U; fi) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62 Version/11.00',
      'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.7.39 Version/11.00'],
     'firefox': ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
      'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
      'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0',
      'Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0',
      'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3',
      'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0',
      'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
      'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
      'Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0',
      'Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Firefox/22.0',
      'Mozilla/5.0 (Microsoft Windows NT 6.2.9200.0); rv:22.0) Gecko/20130405 Firefox/22.0',
      'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
      'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:21.0.0) Gecko/20121011 Firefox/21.0.0',
      'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0',
      'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20130514 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.2; rv:21.0) Gecko/20130326 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130401 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130330 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130401 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130331 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 5.0; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 6.2; Win64; x64;) Gecko/20100101 Firefox/20.0',
      'Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/19.0',
      'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/18.0.1',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0)  Gecko/20100101 Firefox/18.0',
      'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6'],
     'internetexplorer': ['Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
      'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko',
      'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
      'Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
      'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
      'Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)',
      'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))',
      'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)',
      'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)',
      'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)'],
     'safari': ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
      'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
      'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; ko-KR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; fr-FR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; cs-CZ) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; sv-se) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ko-kr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; it-it) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-fr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; es-es) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-gb) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; de-de) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; hu-HU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/534.16+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-ch) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; ar) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; tr-TR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5']}
    random_headers = [
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36 OPR/56.0.3051.104'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 OPR/54.0.2952.64'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36 OPR/56.0.3051.104'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36 OPR/57.0.3098.116'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Safari/537.36'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
    {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1; rv:52.1.0) Gecko/20100101 Firefox/52.1.0'},
    ]
    browser = random.choice(list(random_user_agents.keys()))
    user_agent = random.choice(random_user_agents[browser])
    header = copy.copy(random.choice(random_headers))
    header['User-Agent'] = user_agent
    return header
try:
    #url_table = pd.read_csv('Momo_Crawler.csv')
    url_table = pd.read_csv('Momo_Crawler.csv', encoding='utf-8', encoding_errors='ignore')

except:
    #if fail to read csv file, print error message and exit
    print('Error: fail to read csv file. Please check the file name and try again.')
    sys.exit()

#url_table.dropna(inplace=True)
url_table.dropna(subset=url_table.columns, how='all', inplace=True)

momo_ulr = []
shopee_url = []

try:
    momo_ulr = url_table['Momo_Link'].tolist()
except:
    print('Error: fail to read Momo_Link column. Please check the file name and try again.')
    sys.exit()

try:
    shopee_url = url_table['Shopee_Link'].tolist()
except:
    print('Error: fail to read Shopee_Link column. Please check the file name and try again.')
    sys.exit()

#check if the url list is empty
if len(momo_ulr) == 0 and len(shopee_url) == 0:
    url_table = pd.read_csv('Momo_Crawler.csv')
    momo_ulr = []
    shopee_url = []

    momo_ulr   = url_table['Momo_Link'].tolist()
    shopee_url = url_table['Shopee_Link'].tolist()

#=====Doing shopee web scraping=====#
print("=====Doing shopee web scraping=====")
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') # 啟動無頭模式
# chrome_options.add_argument('--disable-gpu') # windowsd必須加入此行
headers = generate_random_header()
## add the argument and use the header and user agent
chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')

driver = webdriver.Chrome(executable_path="./chromedriver.exe",options=chrome_options)

url = "https://shopee.tw/product-i.690506632.23029188010"
driver.get(url)

# 等待时间上限（秒）
wait_time = 50

# # 等待login_button加载完成
WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='nGTAZw lyJbNT bQ2eCN']")))

print("Please login to your shopee account.")

myemail = input("Please enter your email:")
mypassword = input("Please enter your password:")

email = driver.find_element(By.NAME, "loginKey")
placeholder = email.get_attribute("placeholder")

if placeholder == "電話號碼/使用者名稱/Email":
    email.send_keys(myemail)
else:
    print("Failed to locate the email input box.")
    print("Program will shut down in 5 sec.")
    time.sleep(5)
    #shut down the program
    sys.exit()

password = driver.find_element(By.NAME, "password")
placeholder = password.get_attribute("placeholder")
if placeholder == "密碼":  
    password.send_keys(mypassword)
else:
    print("Failed to locate the password input box.")
    print("Program will shut down in 5 sec.")
    time.sleep(5)
    #shut down the program
    sys.exit()

login_button = driver.find_element(By.XPATH, "//button[contains(text(), '登入')]")

expected_text = "登入"
if login_button.text == expected_text:
    print("Find login button successfully.")
else:
    print("Can't find login button.")
    print("Program will shut down in 5 sec.")
    time.sleep(5)
    #shut down the program
    sys.exit()

time.sleep(2)

login_button.click()

while(login_button.is_enabled()):
    login_button.click()

WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CLASS_NAME,"E62KYV")))
doublecheck = driver.find_element(By.CLASS_NAME,"E62KYV")

expected_text = "使用連結驗證"

if doublecheck.text == expected_text:
    print("Double check button text correct")
else:
    print("Double check button text incorrect")
    print("Program will shut down in 5 sec.")
    time.sleep(5)
try:
    while(True):
        if doublecheck.is_enabled():
            print("Try to click double check button")
            doublecheck.click()
            time.sleep(1)
        else:
            print("Wait for double check button to be enabled")
            break
except:
    pass

while(True):
    try:
        price_elements = driver.find_element(By.CLASS_NAME, "pqTWkA")
        print("Logging in successfully")
        break
    except:
        pass


count = 0
success = 0
Sprice_list = []

wait_time = 10
for url in shopee_url:
    print("Crawling", count, "th out of", len(shopee_url),"...")

    if isinstance(url, float) and math.isnan(url):
        print("Empty URL")
        Sprice_list.append("")
        count+=1
        continue

    if "https://" not in url:
        url = "https://" + url

    try:
        driver.get(url)
        #sleep random tim in float
        time.sleep(random.uniform(5, 6))
        #wait until "直接購買" is clinkable
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "直接購買")]')))
        print("Page loaded successfully.")
    
    except:
        print("載入網站失敗")
        Sprice_list.append("載入網站失敗")
        count+=1
        continue
    
    try:
        #check if the item is still on sale
        element = driver.find_element(By.XPATH, '//div[@class="OWROcY" and contains(text(), "未上架")]')
        print("未上架")
        Sprice_list.append("未上架")
        count+=1
        continue
    except:
        pass

    try:
        element = driver.find_element(By.XPATH, '//div[@class="OWROcY" and contains(text(), "已售完")]')
        print("已售完")
        Sprice_list.append("已售完")
        count+=1
        continue
    except:
        pass
    
    try:
        price_elements = driver.find_element(By.CLASS_NAME, "pqTWkA")
        Sprice_list.append(price_elements.text)
        print("Price:",price_elements.text)
        count+=1
        success+=1
    except:
        print("取得價格失敗")
        Sprice_list.append("取得價格失敗")
        count+=1

print("Crawling finished, ", success, "out of", len(shopee_url), "success in Shopee.")

#remove $ and antything after first price in Sprice_list
for i in range(len(Sprice_list)):
    if Sprice_list[i] == "取得價格失敗" or Sprice_list[i] == "未上架" or Sprice_list[i] == "已售完" or Sprice_list[i] == "載入網站失敗":
        continue
    Sprice_list[i] = Sprice_list[i].replace("$","")
    Sprice_list[i] = Sprice_list[i].split(" ")[0]


#recheck url_table["Shopee_Price"], if =="載入網站失敗"，doing the crawling again for those url
for i in range(len(Sprice_list)):
    if Sprice_list[i] == "載入網站失敗":
        print("RE Crawling", i, "th out of", len(shopee_url),"...")
        url = shopee_url[i]
        if "https://" not in url:
            url = "https://" + url

        try:
            driver.get(url)
            #sleep random tim in float
            time.sleep(random.uniform(5, 6))
            #wait until "直接購買" is clinkable
            WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "直接購買")]')))
            print("Page loaded successfully.")
        
        except:
            print("載入網站失敗")
            Sprice_list[i] = "載入網站失敗"
            continue
        
        try:
            #check if the item is still on sale
            element = driver.find_element(By.XPATH, '//div[@class="OWROcY" and contains(text(), "未上架")]')
            print("未上架")
            Sprice_list[i] = "未上架"
            continue
        except:
            pass

        try:
            element = driver.find_element(By.XPATH, '//div[@class="OWROcY" and contains(text(), "已售完")]')
            print("已售完")
            Sprice_list[i] = "已售完"
            continue
        except:
            pass
        
        try:
            price_elements = driver.find_element(By.CLASS_NAME, "pqTWkA")
            Sprice_list[i] = price_elements.text
            print("Price:",price_elements.text)
            success+=1
        except:
            print("取得價格失敗")
            Sprice_list[i] = "取得價格失敗"
            continue
## close the browser
driver.close()

for i in range(len(Sprice_list)):
    if Sprice_list[i] == "取得價格失敗" or Sprice_list[i] == "未上架" or Sprice_list[i] == "已售完" or Sprice_list[i] == "載入網站失敗":
        continue
    Sprice_list[i] = Sprice_list[i].replace("$","")
    Sprice_list[i] = Sprice_list[i].split(" ")[0]

url_table["Shopee_Price"] = Sprice_list

#=====Doing Momo web scraping=====#
print("=====Doing Momo web scraping=====")

Mtitle_list = []
Mprice_list = []
Mpromo_list = []
Mevent_list = []
#Mbrand_list = []

count = 0
success = 0

for url in momo_ulr:
    count += 1
    print("Crawling", count, "th out of", len(momo_ulr),"...")

    if isinstance(url, float) and math.isnan(url):
        print("Empty URL")
        Mprice_list.append("")
        Mpromo_list.append("")
        Mevent_list.append("")
        #Mbrand_list.append("")
        continue

    #sleep for a random time between 0~0.5 sec
    time.sleep(random.random()/2)

    he = generate_random_header()
    
    try:
        resp = requests.get(url, headers=he)

        if resp.status_code == 200:
            #print('OK')
            soup = BeautifulSoup(resp.text,features="html.parser")
        else:
            print('Error, cralwer seems to be blocked.')
            pass
        
        #try if the page is type1
        try:
            # Title
            title = soup.find('meta',{'property':'og:title'})['content']
            
            if "-momo購物網" in title:
                title = title.replace("-momo購物網","")
            
            Mtitle_list.append(title)

            # Price
            #drop comma in price
            price = soup.find('meta',{'property':'product:price:amount'})['content']
            price = price.replace(',','')
            price = int(price)
            price = (format(price, ',d'))
            Mprice_list.append(price)
        
        #try if the page is type2
        except:
            # title of type2
            meta_tag = soup.find("meta", attrs={"name": "Title"})
            #if meta_tag and "content" in meta_tag.attrs:
            title = meta_tag.attrs["content"]

            if "-momo購物網" in title:
                title = title.replace("-momo購物網","")

            Mtitle_list.append(title)
            
            #price of type2
            li_tag = soup.find("li", class_="special")
            #if li_tag:
            price = li_tag.text.strip()
            price = ''.join(filter(str.isdigit, price))  # 只保留数字部分
            price = int(price)

            price = (format(price, ',d'))
            Mprice_list.append(price)


        # Promo
        prdwarp_div = soup.find('div', class_='prdwarp')

        if prdwarp_div:
            promo = prdwarp_div.find('p', class_='gmclass specialText').text.strip()
            if promo != "":
                Mpromo_list.append(promo)
            else:
                Mpromo_list.append("-")
        else:
            Mpromo_list.append("-")
            promo = "-"

        # Event
        ul_element = soup.find('ul', class_='ineventArea')

        if ul_element:
            li_elements = ul_element.find_all('li')
            
            if len(li_elements) > 0:
                if len(li_elements) > 1:
                    oriEvent = li_elements[0].get_text(strip=True) + " "
                    for i in range(1,len(li_elements)):
                        event = li_elements[i].get_text(strip=True) 
                        oriEvent += event 
                    #Mevent_list.append(oriEvent)
                else:
                    oriEvent = li_elements[0].get_text(strip=True)
            else:
                oriEvent = "-"
            
            if "(說明)" in oriEvent:
                oriEvent = oriEvent.replace("(說明)","")
            #print(oriEvent)
            Mevent_list.append(oriEvent)
        else:
            Mevent_list.append("-")
            oriEvent = "-"

        # Brand
        #brand = soup.find('meta',{'property':"product:brand"})['content']
        try:
            brand = title.split("【")[1].split("】")[0]
        except:
            brand = "N/A"
        #Mbrand_list.append(brand)

        print("Title:", title, "Price:", price, "Promo:", promo, "Event:", oriEvent, "Brand:", brand)
        success += 1
    except:
        print("Error, check if the link is correct.")
        Mprice_list.append('無效網址，商品可能已下架')
        Mpromo_list.append('無效網址，商品可能已下架')
        Mevent_list.append('無效網址，商品可能已下架')
        #Mbrand_list.append('無效網址，商品可能已下架')

today = dt.date.today()
today = str(today)

url_table["Momo_Price"] = Mprice_list

#Get the list of Mprice_list-Mshopee_list, named Diff
Diff = []
for i in range(len(Mprice_list)):
    if Mprice_list[i] == '無效網址，商品可能已下架' or Sprice_list[i] == "取得價格失敗" or Sprice_list[i] == "載入網站失敗" or Sprice_list[i] == "已售完" or Sprice_list[i] == "未上架" or Sprice_list[i] == "" or Mprice_list[i] == "":
        Diff.append("-")
        continue
    else:
        #replace $ and , in both price list and convert to int and calculate the difference in percentage
        #add % to the end of the number
        Diff.append( str(round( (int(Sprice_list[i].replace(',','')) - int(Mprice_list[i].replace(',',''))) / int(Sprice_list[i].replace(',','')) * 100, 2)) + "%" )

url_table["Diff."] = Diff
url_table["Promo"] = Mpromo_list
url_table["Event"] = Mevent_list
# url_table[today] = Mprice_list

print("Crawling finished, ", success, "out of", len(momo_ulr), "success in Momo.")

#save to csv by the name of date of today
url_table.to_csv("Result_"+today+"_"+now+'.csv', index=False, encoding='utf-8-sig')

#url_table.to_csv("Result_"+today+'.csv', index=False, encoding='utf-8-sig')

end = dt.datetime.now()

print("Total time used:", end-begin)

print("File saved as Result_"+today+"_"+now+'.csv')
print("Done, window will close in 5 seconds.")
time.sleep(5)
