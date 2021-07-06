import requests
import time

from lxml import html
from bs4 import BeautifulSoup

BASE_URL = 'https://fecipher.jp/cards/'


def fetch_card_id(list_id):
	"""指定した弾に含まれるカードの識別IDを取得する

		Args:
			(num) list_id 弾のID(st**/bt**)
		Returns:
			(list) カード識別ID
	"""
	# DOSにならないようにsleep
	time.sleep(1)
	result = []

	# カード一覧のURL
	list_url = f'https://fecipher.jp/cards_category/{list_id}/'

	# 何かして配列に値をセット
	response = requests.get(list_url)
	soup = BeautifulSoup(response.text, 'html.parser')
	soup_converted = html.fromstring(str(soup))

	# カード詳細のモーダルを開くリンク
	a_card_detail_link_xpath = '/html/body/div[4]/div/main/article/div/div[3]/table/tbody/tr[position()>=1]/td[1]/a'
	for a in soup_converted.xpath(a_card_detail_link_xpath):
		# 形式...https://fecipher.jp/cards/5880/?modal=true
		card_id = a.get('href').split('/')[4]
		result.append(card_id)

	return result


def fetch_card_ids():
	"""全ての弾についてカードの識別IDを取得する

		Returns:
			(list)カード識別ID
	"""
	result = []

	# ブースターパック
	for i in range(1, 23):
		list_id = f'bt00{i:02}'
		result += fetch_card_ids(list_id)
	
	# スターターデッキ
	for i in range(1, 13):
		list_id = f'st00{i:02}'
		result += fetch_card_ids(list_id)

	return result


def get_unit_type(soup_converted):
	"""ユニットタイプを取得する
		例：光の剣／男／槍／アーマー
	"""


def get_skill_text(soup_converted):
	"""スキルのテキストを取得する(画像から判定して頭に【[アクション1]】とかつけないといけないため)
	"""
	pass


def scrape_card(card_id):
	"""指定したIDのカード情報を抽出する

		Args:
			(num) card_id カードID
		Returns:
			(dict) カード情報
	"""
	# DOSにならないようにsleep
	time.sleep(1)
	result = {}

	response = requests.get(f'https://fecipher.jp/cards/{card_id}/')
	soup = BeautifulSoup(response.text, 'html.parser')
	soup_converted = html.fromstring(str(soup))

	# /html/body/div[4]/div/main/div/div[2]/h1
	print(soup_converted.xpath('/html/body/div[4]/div/main/div/div[2]/h1'))

	# データを抽出
	result['ID'] = card_id
	result['Title'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[2]/h1')[0].text.split(' ')[0]
	result['Name'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[2]/h1')[0].text.split(' ')[1]
	result['ClassRank'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[5]/dd')[0].text
	result['ClassName'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[7]/dd')[0].text
	result['EntryCost'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[1]/dd')[0].text
	result['CCCost'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[3]/dd')[0].text
	result['Attack'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[9]/dd')[0].text.replace('\r\n' , '' ).replace(' ' , '' )
	result['Support'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[11]/dd')[0].text.replace('\r\n' , '' ).replace(' ' , '' )
	result['Range'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[10]/dd')[0].text
	result['UnitType'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[8]/dd')[0].text.replace('\r\n' , '' ).replace(' ' , '' )
	result['SkillName1'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tbody/tr/td/dl/dt')[0].text
	# result['SkillType1'] = soup_converted.xpath('')[0].text
	# result['SkillText1'] = soup_converted.xpath('')[0].text
	# result['SkillName2'] = soup_converted.xpath('')[0].text
	# result['SkillType2'] = soup_converted.xpath('')[0].text
	# result['SkillText2'] = soup_converted.xpath('')[0].text
	# result['SkillName3'] = soup_converted.xpath('')[0].text
	# result['SkillType3'] = soup_converted.xpath('')[0].text
	# result['SkillText3'] = soup_converted.xpath('')[0].text
	# result['SkillName4'] = soup_converted.xpath('')[0].text
	# result['SkillType4'] = soup_converted.xpath('')[0].text
	# result['SkillText4'] = soup_converted.xpath('')[0].text

	print(result)
	return result


if __name__ == "__main__":
	# ブースターパックの一覧を取得
	# スターターデッキの一覧を取得

	# ブースターパックに含まれるカードの一覧を取得
	# スターターデッキに含まれるカードの一覧を取得

	# カードページから画像を取得してファイル名 = IDを保存
	# カードページからCSVで使うカード情報を取得して辞書へ保存

	# CSVで使うカード情報を出力

	card_ids = fetch_card_id('bt0001')
	for i in range(1, 2):
		scrape_card(card_ids[i])
	pass