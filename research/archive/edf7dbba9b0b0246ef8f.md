---
title: python3でwebスクレイピング(Beautiful Soup)
tags: Python Python3 scrape crawl
author: mtskhs
slide: false
---
python3でwebスクレイピングのために、
Beautiful Soupを利用した方法を紹介します

* ドキュメント：https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## 環境

```console
$ cat /etc/redhat-release 
CentOS Linux release 7.4.1708 (Core) 

$ python3 -V
Python 3.5.4

$ pip -V
pip 9.0.1
```

# install

下記を使ってスクレイピングします。

- requests: HTTP ライブラリ
- beautifulsoup4: htmlパーサー(pythonから呼び出し)
- lxml: htmlパーサー(beautifulsoup4内部で利用)

```sh
pip install requests
pip install beautifulsoup4
pip install lxml
```

## インストール確認

```sh
pip freeze | grep -e request -e lxml -e beautiful 

beautifulsoup4==4.6.0 
lxml==4.0.0
requests==2.18.4
```

# 使い方

まずはインポートします。

```py
import requests
from bs4 import BeautifulSoup
```

次に、HTMLを取得してきます。

```python3
target_url = '***'
r = requests.get(target_url)         #requestsを使って、webから取得
```

htmlパース用のオブジェクト作成します。内部で利用するパーサーを指定する場合は、"html.parser"の部分を"lxml"などに変更します。

```py
soup = BeautifulSoup(r.text, "html.parser")
 or
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出
```
lxmlは速度が早いのでおすすめらしい。下記がわかりやすかった。

>パーサの良し悪しを考えるとlxmlでチャレンジしてダメならhtml5libを試すのが良さそう。
[PythonでWebスクレイピングする時の知見をまとめておく][html-parser]
[html-parser]:http://vaaaaaanquish.hatenablog.com/entry/2017/06/25/202924

## 特定のタグを取得

```python3
soup.find_all("a")
soup.find("a")
soup.find_all("a", attrs={"class": "link", "href": "/link"})

import re
soup.find_all(re.compile("^b"))
soup.find_all("a", text=re.compile("hello"))

soup.select('a[href^="http://"]')
```

## サンプルコード

全てのaタグを取得し、リンク先URL（href属性）を表示します

```python3

import requests
from bs4 import BeautifulSoup

target_url = '***'
r = requests.get(target_url)         #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

for a in soup.find_all('a'):
      print(a.get('href'))         #リンクを表示
```

