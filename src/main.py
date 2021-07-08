import csv
import re
import requests
import time

from lxml import html, etree
from bs4 import BeautifulSoup

# スキル(タイプ)
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

# スキル(効果)
ICON_FS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_fs.png'
ICON_HS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_hs_nashi_clear.png'
ICON_CCS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_ccs.png'
ICON_TS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_ts_nashi_clear.png'
ICON_IS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_is_nashi_clear.png'
ICON_LEVX = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_lvx_clear.png'
ICON_US = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_us_clear.png'
ICON_AS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_as_nashi_clear.png'
ICON_CF = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_cf_clear.png'
ICON_DB = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_db_nashi_clear.png'
ICON_BS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_bs_clear.png'
ICON_RYUMYAKU = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_ryumyaku_clear.png'
ICON_LIS = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_lis_nashi_clear.png'
ICON_CP = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/skill/icon_cp_nashi_clear.png'

# スキル(支援)
ICON_DEFENCE = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/supportskill/icon_defence_clear.png'
ICON_ATTACK = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/supportskill/icon_attack_clear.png'

# スキル(その他)
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

# タイプ
ICON_ANKOKU = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/symbol/icon_ankoku.png'
ICON_KAKUSEI = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/symbol/icon_kakusei.png'
ICON_BYAKUYA = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/symbol/icon_byakuya.png'
ICON_ANYA  = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/symbol/icon_anya.png'
ICON_SOUEN = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/symbol/icon_souen.png'
ICON_HUUIN = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/symbol/icon_huuin.png'
ICON_SEISEN = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/symbol/icon_seisen.png'
ICON_MEGAMIMON = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/symbol/icon_megamimon.png'
ICON_MAN = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/gender/icon_man_clear.png'
ICON_WOMAN = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/gender/icon_woman_clear.png'
ICON_SWORD = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/arms/icon_sword_clear.png'
ICON_SPEAR = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/arms/icon_spear_clear.png'
ICON_AX = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/arms/icon_ax_clear.png'
ICON_BOW = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/arms/icon_bow_clear.png'
ICON_MAGIC = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/arms/icon_magic_clear.png'
ICON_STICK = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/arms/icon_stick_clear.png'
ICON_DORAGONSTONE = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/arms/icon_dragonstone_clear.png'
ICON_DARKWEAPON = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/arms/icon_darkweapon_clear.png'
ICON_FANG = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/arms/icon_fang_clear.png'
ICON_FIST = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/arms/icon_fist_clear.png'
ICON_ARMOR = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/type/icon_armor_clear.png'
ICON_FLY = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/type/icon_fly_clear.png'
ICON_MOUNTED = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/type/icon_mounted_clear.png'
ICON_DRAGON = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/type/icon_dragon_clear.png'
ICON_SHARP = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/type/icon_sharp_clear.png'
ICON_EVIL = 'https://fecipher.jp/wp-content/themes/cipher/dist/images/cards/icon/type/icon_evil_clear.png'


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


def get_unit_type(elements_dict):
	"""指定したHTMLElementからユニットタイプを抽出する
		elementが取得できない場合は空文字を返却する
		フォーマット：{シンボル名}／{性別}／{武器}／..{タイプ}

		Args:
			(dict(list((HTMLElement))) elements_dict 抽出対象
				symbol, gender, weapon, types
		Resutns:
			(str) テキスト
	"""
	elm_symbol = elements_dict['symbol']	
	elm_gender = elements_dict['gender']	
	elm_weapon = elements_dict['weapon']	
	elm_types = elements_dict['types'][0]

	symbol = elm_symbol[0].get('alt')
	gender = elm_gender[0].get('alt')
	weapon = elm_weapon[0].get('alt')
	types_arr = []

	result = f'{symbol}／{gender}／{weapon}'
	if elm_types != []:
		for elm_type in elm_types.findall('img'):
			types_arr.append(elm_type.get('alt'))
		for type_str in types_arr:
			result += f'／{type_str}'

	return result


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

	result_arr = []
	for img in elements[0].findall('img'):
		src = img.get('src')
		if src == ICON_ZIDOU:
			result_arr.append('自動型')
		elif src == ICON_KIDOU:
			result_arr.append('起動型')
		elif src == ICON_ZYOUZI:
			result_arr.append('常時型')
		elif src == ICON_KIZUNA:
			result_arr.append('絆型')
		elif src == ICON_TEFUDA:
			result_arr.append('手札型')
		elif src == ICON_SIEN:
			result_arr.append('支援型')
		elif src == ICON_TOKUSYU:
			result_arr.append('特殊型')
		elif src == ICON_DEFENCE:
			result_arr.append('防御型')
		elif src == ICON_ATTACK:
			result_arr.append('攻撃型')
	return '／'.join(result_arr)


def convert_skill_img_to_text(skill_text):
	"""スキルのテキストに含まれるimgタグを文字列へ変換する

		Args:
			(str) skill_text スキルのテキスト
		Returns:
			(str) 変換後のスキルテキスト
	"""
	result = skill_text
	result = result\
		.replace('<img src="' + ICON_ZIDOU + '"/>', '【自】')\
		.replace('<img src="' + ICON_KIDOU + '"/>', '【起】')\
		.replace('<img src="' + ICON_ZYOUZI + '"/>', '【常】')\
		.replace('<img src="' + ICON_KIZUNA + '"/>', '【絆】')\
		.replace('<img src="' + ICON_TEFUDA + '"/>', '【札】')\
		.replace('<img src="' + ICON_SIEN + '"/>', '【支】')\
		.replace('<img src="' + ICON_TOKUSYU + '"/>', '【特】')\
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
		.replace('<img src="' + ICON_ONCE + '"/>', '[1ターンに1回] ')\
		.replace('<img src="' + ICON_REV_1 + '"/>', '[リバース.1] ')\
		.replace('<img src="' + ICON_REV_2 + '"/>', '[リバース.2] ')\
		.replace('<img src="' + ICON_REV_3 + '"/>', '[リバース.3] ')\
		.replace('<img src="' + ICON_REV_4 + '"/>', '[リバース.4] ')\
		.replace('<img src="' + ICON_REV_5 + '"/>', '[リバース.5] ')\
		.replace('<img src="' + ICON_LEV1 + '"/>', '[レベル.1] ')\
		.replace('<img src="' + ICON_LEV2 + '"/>', '[レベル.2] ')\
		.replace('<img src="' + ICON_LEV3 + '"/>', '[レベル.3] ')\
		.replace('<img src="' + ICON_LEV4 + '"/>', '[レベル.4] ')\
		.replace('<img src="' + ICON_LEV5 + '"/>', '[レベル.5] ')\
		.replace('<img src="' + ICON_ANKOKU + '"/>', '<光の剣>')\
		.replace('<img src="' + ICON_KAKUSEI + '"/>', '<聖痕>')\
		.replace('<img src="' + ICON_BYAKUYA + '"/>', '<白夜>')\
		.replace('<img src="' + ICON_ANYA + '"/>', '<暗夜>')\
		.replace('<img src="' + ICON_SOUEN + '"/>', '<メダリオン>')\
		.replace('<img src="' + ICON_HUUIN + '"/>', '<神器>')\
		.replace('<img src="' + ICON_SEISEN + '"/>', '<聖戦旗>')\
		.replace('<img src="' + ICON_MEGAMIMON + '"/>', '<女神紋>')\
		.replace('<img src="' + ICON_MAN + '"/>', '<男>')\
		.replace('<img src="' + ICON_WOMAN + '"/>', '<女>')\
		.replace('<img src="' + ICON_SWORD + '"/>', '<剣>')\
		.replace('<img src="' + ICON_SPEAR + '"/>', '<槍>')\
		.replace('<img src="' + ICON_AX + '"/>', '<斧>')\
		.replace('<img src="' + ICON_BOW + '"/>', '<弓>')\
		.replace('<img src="' + ICON_MAGIC + '"/>', '<魔法>')\
		.replace('<img src="' + ICON_STICK + '"/>', '<杖>')\
		.replace('<img src="' + ICON_DORAGONSTONE + '"/>', '<竜意思>')\
		.replace('<img src="' + ICON_DARKWEAPON + '"/>', '<暗器>')\
		.replace('<img src="' + ICON_FANG + '"/>', '<牙>')\
		.replace('<img src="' + ICON_FIST + '"/>', '<拳>')\
		.replace('<img src="' + ICON_ARMOR + '"/>', '<アーマー>')\
		.replace('<img src="' + ICON_FLY + '"/>', '<飛行>')\
		.replace('<img src="' + ICON_MOUNTED + '"/>', '<獣馬>')\
		.replace('<img src="' + ICON_DRAGON + '"/>', '<竜>')\
		.replace('<img src="' + ICON_SHARP + '"/>', '<幻影>')\
		.replace('<img src="' + ICON_EVIL + '"/>', '<魔物>')\
		.replace('\n', '')

	# 「&lt;幻影&gt;」のようなやつを消す
	return re.sub('&lt;.+&gt;', '', result)


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


def merge_skills(elements_dict):
	"""スキルのテキストを支援スキルまで含めて取得し、歯抜けなしの配列へマージする
		/html/body/div[4]/div/main/div/div[4]/table/tr[1]/td/dl/dt
		Args:
			(dict(list((HTMLElement))) elements_dict 抽出対象
				{skill_vanilla, skill_support}
		Resutns:
			(list(dict)) スキル情報の配列
				[{name, type, text}]
	"""
	skill_vanilla = elements_dict['skill_vanilla']
	skill_support = elements_dict['skill_support']
	result = []

	# 通常スキルの設定
	if skill_vanilla != []:
		dts = skill_vanilla[0].findall('dt')
		dds = skill_vanilla[0].findall('dd')
		for i in range(0, len(dts)):
			result.append({
				'name': get_xpath_str([dts[i]]), 
				'type': get_skill_type([dds[i]]), 
				'text': get_skill_text([dds[i]]) 
			})
	
	# 支援スキルの設定
	if skill_support != []:
		dts_s = skill_support[0].findall('dt')
		dds_s = skill_support[0].findall('dd')
		for i in range(0, len(dts_s)):
			# スキル名が img + テキストなので処理
			skill_support_name = [etree.tostring(node, encoding='utf-8').decode() for node in dts_s[i].iterdescendants()][0]
			result.append({
				'name': re.sub('<.+>', '', skill_support_name), 
				'type': get_skill_type([dts_s[i]]), 
				'text': dds_s[i].text 
			})

	return result


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

	unit_types_soup_dict = {
		'symbol': soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[2]/dd/img'),
		'gender': soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[4]/dd/img'),
		'weapon': soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[6]/dd/img'),
		'types': soup_converted.xpath('/html/body/div[4]/div/main/div/div[3]/dl[8]/dd')
	}
	result['UnitType'] = get_unit_type(unit_types_soup_dict)

	### なぜか tbody がxpathに含まれると要素取得できない(´・ω・) メモのため残しておく
	### result['SkillName1'] = soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tbody/tr[1]/td/dl/dt[1]'))
	### lxml.html.HtmlElement ===> https://lxml.de/api/lxml.etree._Element-class.html
	skill_soup_dict = {
		'skill_vanilla': soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr[1]/td/dl'),
		'skill_support': soup_converted.xpath('/html/body/div[4]/div/main/div/div[4]/table/tr[2]/td/dl')
	}
	skills = merge_skills(skill_soup_dict)
	for i in range(0, len(skills)):
		result[f'SkillName{i + 1}'] = skills[i]['name']
		result[f'SkillType{i + 1}'] = skills[i]['type']
		result[f'SkillText{i + 1}'] = skills[i]['text']
	# 最大4まで埋める
	for i in range(4, len(skills), -1):
		result[f'SkillName{i}'] = ''
		result[f'SkillType{i}'] = ''
		result[f'SkillText{i}'] = ''

	# print(result)
	return result


def convert_cart_info_to_list(card_info):
	"""カード情報をCSV出力用のリストへ変換する

		Args:
			(dict) カード情報 card_info scrape_card の戻り値形式
		Returns:
			(list) カード情報の配列
	"""
	result = []
	result.append(card_info['ID'])
	result.append(card_info['Title'])
	result.append(card_info['Name'])
	result.append(card_info['ClassRank'])
	result.append(card_info['ClassName'])
	result.append(card_info['EntryCost'])
	result.append(card_info['CCCost'])
	result.append(card_info['Attack'])
	result.append(card_info['Support'])
	result.append(card_info['Range'])
	result.append(card_info['UnitType'])
	result.append(card_info['SkillName1'])
	result.append(card_info['SkillType1'])
	result.append(card_info['SkillText1'])
	result.append(card_info['SkillName2'])
	result.append(card_info['SkillType2'])
	result.append(card_info['SkillText2'])
	result.append(card_info['SkillName3'])
	result.append(card_info['SkillType3'])
	result.append(card_info['SkillText3'])
	result.append(card_info['SkillName4'])
	result.append(card_info['SkillType4'])
	result.append(card_info['SkillText4'])

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
	####scrape_card(27567) # まもり
	#scrape_card(5242) # ロイ(支援2つ持ち)

	card_ids = fetch_card_id('st0001')
	card_infos = []
	count  =0
	for card_id in card_ids:
		card_info_org = scrape_card(card_id)
		card_info = convert_cart_info_to_list(card_info_org)
		card_infos.append(card_info)

		count += 1
		if count > 0:
			break
	print(card_infos)

	with open('result.csv', 'w', encoding='UTF-8') as f:
		writer = csv.writer(f)
		writer.writerows(card_infos)