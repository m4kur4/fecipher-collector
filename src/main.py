import requests
import time

from lxml import html, etree
from bs4 import BeautifulSoup

# スキルタイプ
BASE_URL = 'https://fecipher.jp/cards/'
ICON_ACT = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_act_clear.png'
ICON_ONCE = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_once_clear.png'
ICON_ZIDOU = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_zidou_clear.png'
ICON_KIDOU = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_kidou_clear.png'
ICON_ZYOUZI = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_zyouzi_clear.png'
ICON_SIEN = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_sien_clear.png' # ルルブに載ってるけどカード見つからないので決め打ち
ICON_TOKUSYU = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_tokusyu_clear.png'
ICON_KIZUNA = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_kizuna_clear.png'
ICON_TEFUDA = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_tefuda_clear.png'

# スキル
ICON_FS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_fs_nashi_clear.png'
ICON_HS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_hs_nashi_clear.png'
ICON_CCS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_ccs.png'
ICON_TS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_ts_nashi_clear.png'
ICON_IS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_is_nashi_clear.png'
ICON_LEVX = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_lvx_clear.png'
ICON_US = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_us_nashi_clear.png'
ICON_AS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_as_nashi_clear.png'
ICON_CF = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_cf_clear.png'
ICON_DB = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_db_clear.png'
ICON_BS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_bs_clear.png'
ICON_RYUMYAKU = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_ryumyaku_clear.png'
ICON_LIS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_lis_nashi_clear.png'
ICON_CP = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_cp_nashi_clear.png'

# その他
ICON_REV_1 = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_rev1_clear.png'
ICON_REV_2 = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_rev2_clear.png'
ICON_REV_3 = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_rev3_clear.png'
ICON_REV_4 = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_rev4_clear.png'
ICON_REV_5 = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_rev5_clear.png'
ICON_LEV1 = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_lev1_clear.png'
ICON_LEV2 = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_lev2_clear.png'
ICON_LEV3 = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_lev3_clear.png'
ICON_LEV4 = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_lev4_clear.png'
ICON_LEV5 = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_lev5_clear.png'

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

def get_xpath_str(elements):
	"""指定したHTMLElementからテキストを抽出する
		elementが取得できない場合は空文字を返却する

		Args:
			(list(HTMLElement)) elements 抽出対象
		Resutns:
			(str) テキスト
	"""
	if elements == []:
		return ''
	return elements[0].text


def get_unit_type(soup_converted):
	"""ユニットタイプを取得する
		例：光の剣／男／槍／アーマー

		Args:
			(element) lxmlに変換したsoup 
		Returns:
			(str) ユニットタイプのテキスト
	"""


def get_skill_type(elements):
	"""指定したHTMLElementからスキルタイプを抽出する
		elementが取得できない場合は空文字を返却する

		Args:
			(list(HTMLElement)) elements 抽出対象
		Resutns:
			(str) テキスト
	"""
	if elements == []:
		return ''

	###print(elements[0].findall('img'))
	for img in elements[0].findall('img'):
		src = img.get('src')
		if src == ICON_ZIDOU:
			return '自動型'
		elif src == ICON_KIDOU:
			return '起動型'
		elif src == ICON_ZYOUZI:
			return '常時型'
		elif src == ICON_KIZUNA:
			return '絆型'
		elif src == ICON_TEFUDA:
			return '手札型'
		elif src == ICON_SIEN:
			return '支援型'
		elif src == ICON_TOKUSYU:
			return '特殊型'


def convert_skill_img_to_text(skill_text):
	"""スキルのテキストに含まれるimgタグを文字列へ変換する

		Args:
			(str) skill_text スキルのテキスト
		Returns:
			(str) 変換後のスキルテキスト
	"""
	result = skill_text
	# スキルタイプは消す
	result = result\
		.replace('<img src="' + ICON_ZIDOU + '"/>', '')\
		.replace('<img src="' + ICON_KIDOU + '"/>', '')\
		.replace('<img src="' + ICON_ZYOUZI + '"/>', '')\
		.replace('<img src="' + ICON_KIZUNA + '"/>', '')\
		.replace('<img src="' + ICON_TEFUDA + '"/>', '')\
		.replace('<img src="' + ICON_SIEN + '"/>', '')\
		.replace('<img src="' + ICON_TOKUSYU + '"/>', '')

	# それ以外の画像はテキストに差し替える
	result = result\
		.replace('<img src="' + ICON_FS + '"/>', '【FS】')\
		.replace('<img src="' + ICON_HS + '"/>', '【HS】')\
		.replace('<img src="' + ICON_CCS + '"/>', '【CCS】')\
		.replace('<img src="' + ICON_TS + '"/>', '【TS】')\
		.replace('<img src="' + ICON_IS + '"/>', '【IS】')\
		.replace('<img src="' + ICON_LEVX + '"/>', '【LEVX】')\
		.replace('<img src="' + ICON_US + '"/>', '【US】')\
		.replace('<img src="' + ICON_AS + '"/>', '【AS】')\
		.replace('<img src="' + ICON_CF + '"/>', '【CF】')\
		.replace('<img src="' + ICON_DB + '"/>', '【DB】')\
		.replace('<img src="' + ICON_BS + '"/>', '【BS】')\
		.replace('<img src="' + ICON_RYUMYAKU + '"/>', '【竜脈】')\
		.replace('<img src="' + ICON_LIS + '"/>', '【LIS】')\
		.replace('<img src="' + ICON_CP + '"/>', '【CP】')\
		.replace('<img src="' + ICON_REV_1 + '"/>', '【リバース[1]】')\
		.replace('<img src="' + ICON_REV_2 + '"/>', '【リバース[2]】')\
		.replace('<img src="' + ICON_REV_3 + '"/>', '【リバース[3]】')\
		.replace('<img src="' + ICON_REV_4 + '"/>', '【リバース[4]】')\
		.replace('<img src="' + ICON_REV_5 + '"/>', '【リバース[5]】')\
		.replace('<img src="' + ICON_LEV1 + '"/>', '【レベル[1]】')\
		.replace('<img src="' + ICON_LEV2 + '"/>', '【レベル[2]】')\
		.replace('<img src="' + ICON_LEV3 + '"/>', '【レベル[3]】')\
		.replace('<img src="' + ICON_LEV4 + '"/>', '【レベル[4]】')\
		.replace('<img src="' + ICON_LEV5 + '"/>', '【レベル[5]】')

	return result

def get_skill_text(elements):
	"""指定したHTMLElementからスキルテキストを抽出する
		elementが取得できない場合は空文字を返却する

		Args:
			(list(HTMLElement)) elements 抽出対象
		Resutns:
			(str) テキスト
	"""
	if elements == []:
		return ''

	result_arr = []
	for node in elements[0].iterdescendants():
		# スキルのテキストにはimgタグと文字列が混在しているので、innerHTML的な処理をする
		# 参考...https://stackoverflow.com/questions/30772943/get-inner-text-from-lxml
		node_text = etree.tostring(node, encoding='utf-8').decode()  #etree.tostring()はバイト列を返すのでデコードする
		# imgタグを文字列に変換する
		img_tag_converted = convert_skill_img_to_text(node_text)
		result_arr.append(img_tag_converted)

	return ''.join(result_arr)

	#return ''.join([etree.tostring(str(child), encoding="utf-8") for child in elements[0].iterdescendants()])


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

	url = f'https://fecipher.jp/cards/{card_id}/'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	soup_converted = html.fromstring(str(soup))

	print(url)
	# /html/body/div[4]/div/main/div/div[2]/h1
	# print(soup_converted.xpath('/html/body/div[4]/div/main/div/div[2]/h1'))

	# データを抽出
	result['ID'] = card_id
	result['Title'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[2]/h1')).split(' ')[0]
	result['Name'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[2]/h1')).replace(result['Title'] + ' ', '')
	result['ClassRank'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[5]/dd'))
	result['ClassName'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[7]/dd'))
	result['EntryCost'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[1]/dd'))
	result['CCCost'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[3]/dd'))
	result['Attack'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[9]/dd')).replace('\r\n' , '' ).replace(' ' , '' )
	result['Support'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[11]/dd')).replace('\r\n' , '' ).replace(' ' , '' )
	result['Range'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[10]/dd'))
	result['UnitType'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[8]/dd')).replace('[\r\n]' , '' ).replace(' ' , '' )

	### なぜか tbody がxpathに含まれると要素取得できない(´・ω・) メモのため残しておく
	### result['SkillName1'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tbody/tr[1]/td/dl/dt[1]'))
	### lxml.html.HtmlElement ===> https://lxml.de/api/lxml.etree._Element-class.html
	result['SkillName1'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr[1]/td/dl/dt[1]'))
	result['SkillType1'] = get_skill_type(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr/td/dl/dd[1]'))
	result['SkillText1'] = get_skill_text(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr/td/dl/dd[1]'))

	result['SkillName2'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr[1]/td/dl/dt[2]'))
	result['SkillType2'] = get_skill_type(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr/td/dl/dd[2]'))
	result['SkillText2'] = get_skill_text(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr/td/dl/dd[2]'))

	result['SkillName3'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr[1]/td/dl/dt[3]'))
	result['SkillType3'] = get_skill_type(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr/td/dl/dd[3]'))
	result['SkillText3'] = get_skill_text(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr/td/dl/dd[3]'))

	result['SkillName4'] = get_xpath_str(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr[1]/td/dl/dt[4]'))
	result['SkillType4'] = get_skill_type(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr/td/dl/dd[4]'))
	result['SkillText4'] = get_skill_text(soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr/td/dl/dd[4]'))

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

	# card_ids = fetch_card_id('bt0001')
	# for i in range(1, 2):
	# 	scrape_card(card_ids[i])
	scrape_card(27566)
	pass