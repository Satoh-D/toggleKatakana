# -*- coding: utf-8 -*-
import sublime, sublime_plugin, string

dict_multiKana = {
	u'ア': u'ｱ', u'イ': u'ｲ', u'ウ': u'ｳ', u'エ': u'ｴ', u'オ': u'ｵ',
	u'カ': u'ｶ', u'キ': u'ｷ', u'ク': u'ｸ', u'ケ': u'ｹ', u'コ': u'ｺ',
	u'サ': u'ｻ', u'シ': u'ｼ', u'ス': u'ｽ', u'セ': u'ｾ', u'ソ': u'ｿ',
	u'タ': u'ﾀ', u'チ': u'ﾁ', u'ツ': u'ﾂ', u'テ': u'ﾃ', u'ト': u'ﾄ',
	u'ナ': u'ﾅ', u'ニ': u'ﾆ', u'ヌ': u'ﾇ', u'ネ': u'ﾈ', u'ノ': u'ﾉ',
	u'ハ': u'ﾊ', u'ヒ': u'ﾋ', u'フ': u'ﾌ', u'ヘ': u'ﾍ', u'ホ': u'ﾎ',
	u'マ': u'ﾏ', u'ミ': u'ﾐ', u'ム': u'ﾑ', u'メ': u'ﾒ', u'モ': u'ﾓ',
	u'ヤ': u'ﾔ', u'ユ': u'ﾕ', u'ヨ': u'ﾖ',
	u'ラ': u'ﾗ', u'リ': u'ﾘ', u'ル': u'ﾙ', u'レ': u'ﾚ', u'ロ': u'ﾛ',
	u'ワ': u'ﾜ', u'ヲ': u'ｦ', u'ン': u'ﾝ', u'ヴ': u'ｳﾞ',
	u'ァ': u'ｧ', u'ィ': u'ｨ', u'ゥ': u'ｩ', u'ェ': u'ｪ', u'ォ': u'ｫ',
	u'ャ': u'ｬ', u'ュ': u'ｭ', u'ョ': u'ｮ',
	u'ガ': u'ｶﾞ', u'ギ': u'ｷﾞ', u'グ': u'ｸﾞ', u'ゲ': u'ｹﾞ', u'ゴ': u'ｺﾞ',
	u'ザ': u'ｻﾞ', u'ジ': u'ｼﾞ', u'ズ': u'ｽﾞ', u'ゼ': u'ｾﾞ', u'ゾ': u'ｿﾞ',
	u'ダ': u'ﾀﾞ', u'ヂ': u'ﾁﾞ', u'ヅ': u'ﾂﾞ', u'デ': u'ﾃﾞ', u'ド': u'ﾄﾞ',
	u'バ': u'ﾊﾞ', u'ビ': u'ﾋﾞ', u'ブ': u'ﾌﾞ', u'ベ': u'ﾍﾞ', u'ボ': u'ﾎﾞ',
	u'パ': u'ﾊﾟ', u'ピ': u'ﾋﾟ', u'プ': u'ﾌﾟ', u'ペ': u'ﾍﾟ', u'ポ': u'ﾎﾟ',
	u'ー': u'ｰ', u'、': u'､', u'。': u'｡', u'「': u'｢', u'」': u'｣'
}
dict_singleKana = {
}
str_dakuten = u'ﾞ'
str_handakuten = u'ﾟ'


def convertToSinglebyteKatakana(region):
	region = region;
	region = u'%s' % str(region)
	region = region
	ret_region = u''

	for char_current in region:
		if(char_current in dict_multiKana):
			ret_region += dict_multiKana[char_current]
		else:
			ret_region += char_current

	return ret_region

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, toggleKatakana")


class ConvertToMultibyteCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		# select all Region
		region_all = sublime.Region(0, self.view.size())
		region_all = self.view.substr(region_all)

		self.view.insert(edit, self.view.size() - 1, region_all)


class ConvertToSinglebyteCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		# select all Region
		region_all = sublime.Region(0, self.view.size())
		region_all_str = self.view.substr(region_all)
		region_all_converted = convertToSinglebyteKatakana(region_all_str)

		self.view.replace(edit, region_all, region_all_converted)
