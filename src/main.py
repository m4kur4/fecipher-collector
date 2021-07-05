import requests
import time

from bs4 import BeautifulSoup

BASE_URL = 'https://fecipher.jp/cards/'

def crowl_caard_list(id):
	"""指定したIDのパックに含まれるカードの識別IDを取得する
	"""
	# DOSにならないようにsleep
	time.sleep(1)	
	# カード一覧のURL
	url = f'https://fecipher.jp/cards_category/{id}/'

	# 何かして配列に値をセット
	result = [1]

	return result

def crowl_caard_lists():
	"""全てのパック(1～22弾)についてカードの識別IDを取得する
	"""
	result = []

	for i in range(1, 23):
		id = f'bt00{i:02}'
		result += crowl_caard_list(id)
	
	print(result)

def scrape_card(id):
	"""指定したIDのカード情報をスクレイピングする
	"""
	# DOSにならないようにsleep
	time.sleep(1)

	req = requests.get(f'https://fecipher.jp/cards/{id}/')
	html = req.text
	soup = BeautifulSoup(html, 'lxml')
	print(soup)



if __name__ == "__main__":
	# ブースターパックの一覧を取得
	# スターターデッキの一覧を取得

	# ブースターパックに含まれるカードの一覧を取得
	# スターターデッキに含まれるカードの一覧を取得

	# カードページから画像を取得してファイル名 = IDを保存
	# カードページからCSVで使うカード情報を取得して辞書へ保存

	# CSVで使うカード情報を出力

	scrape_card(5853)
	pass