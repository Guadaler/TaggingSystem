#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：函数功能模块
# Author: zx
# Software: PyCharm Community Edition
# File: function.py
# Time: 17-1-16 上午11:14
# -------------------------------------------
import urllib

from PyQt4 import QtGui

import jieba.posseg as pseg
from PyQt4.QtGui import QMessageBox

import globe


def __fill_data(qt):
    qt.setStyleSheet("QLabel{font-size:16px;font-family:'微软雅黑';}")

    temp = ""
    for n in range(len(globe.word_all)):
        w = globe.word_all[n]

        if n == globe.word_index:
            temp += "\t" + "<span style='color:#FF0033;font-weight:bold;'>%s</span>" % w.word
        else:
            temp += "\t" + w.word

    qt.label.setText(temp)
    qt.label_2.setText(globe.word.word)
    qt.label_3.setText(globe.word.flag + "\t" + globe.tag_dict.get(globe.word.flag, u"未知词性"))


# 哈工大
def cut_ltp(text):
    print text
    url_get_base = "http://api.ltp-cloud.com/analysis/"
    args = {
        'api_key': 'o9g0E8g50ZtwuZsmfx4A7juNyw0E0M7fic4dgHSK',
        'text': text,
        'pattern': 'ws',
        'format': 'plain'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip(" ")
    print "结果 ", content


# 切词
def cut_word(text):
    seg = pseg.cut(text)
    return seg


# 读取文件
def read_file():
    for f in open(globe.input_path):
        globe.text_all.append(f.strip("\n"))


# 初始化文本
def init_text(tcurrent):
    globe.text = globe.text_all[tcurrent]
    globe.text_index = tcurrent
    globe.word_all = list(cut_word(globe.text))


# 初始化词
def init_word(wcurrent):
    globe.word = globe.word_all[wcurrent]
    globe.word_index = wcurrent


# 数据填充
def fill(self):
    self.text.setText("")
    __fill_data(self)


# 向前合并
def merge_pre(self):
    if globe.word_index > 0:
        pre_word = globe.word_all[globe.word_index - 1]

        pre_word.word = pre_word.word + globe.word.word
        pre_word.flag = u"UnKnown"
        globe.word_all[globe.word_index - 1] = pre_word
        globe.word_all.remove(globe.word)

        globe.word = pre_word
        globe.word_index -= 1
        fill(self)
    else:
        msg(self, u"当前第一个词")


# 向后合并
def merge_next(self):
    if globe.word_index < len(globe.word_all):
        next_word = globe.word_all[globe.word_index + 1]

        globe.word.word = globe.word.word + next_word.word
        globe.word.flag = u"UnKnown"
        globe.word_all[globe.word_index] = globe.word
        globe.word_all.remove(next_word)

        fill(self)
    else:
        msg(self, u"当前最后一个词")


# 按位拆分
def split_position(self):
    position = self.text.toPlainText()

    # 默认进行第一位置拆分
    if position == "":
        pre_word_word = globe.word.word[:1]
        next_word_word = globe.word.word[1:]

        globe.word.word = pre_word_word
        globe.word.flag = "UnKnown"
        globe.word_all[globe.word_index] = globe.word

        insert_word = pseg.pair(next_word_word, "UnKnown")
        globe.word_all.insert(globe.word_index + 1, insert_word)
        fill(self)
    elif int(position) > len(globe.word.word) - 1:
        msg(self, u"拆分位置越位")
    else:
        pre_word_word = globe.word.word[:int(position)]
        next_word_word = globe.word.word[int(position):]

        globe.word.word = pre_word_word
        globe.word.flag = "UnKnown"
        globe.word_all[globe.word_index] = globe.word

        insert_word = pseg.pair(next_word_word, "UnKnown")
        globe.word_all.insert(globe.word_index + 1, insert_word)
        fill(self)


# 前一个词
def word_pre(self):
    if globe.word_index == 0:
        msg(self, u"当前第一个词")
    else:
        init_word(globe.word_index - 1)
        fill(self)


# 后一个词
def word_next(self):
    if globe.word_index == len(globe.word_all) - 1:
        msg(self, u"当前最后一个词")
    else:
        init_word(globe.word_index + 1)
        fill(self)


# 词性标注
def pos_tag(self, pos):
    globe.word.flag = pos
    globe.word_all[globe.word_index] = globe.word
    word_next(self)


# 下一篇
def next_text(self):
    if globe.text_index == len(globe.text_all) - 1:
        msg(self, u"下一篇没有了")
    else:
        msg_confirm(self, u"是否保存当前标注结果？")
        init_text(globe.text_index + 1)
        init_word(0)
        fill(self)


# 结果保存
def save(self):
    writer = open(globe.output_path, "a")
    for w in globe.word_all:
        writer.write(w.word + "/" + w.flag + "\t")
    writer.write("\n")
    writer.flush()
    writer.close()
    msg(self, u"当前保存成功！")


# 弹窗
def msg(self, text_msg):
    msgbox = QMessageBox(self)
    msgbox.setWindowTitle(u"信息提醒")
    msgbox.setText(text_msg)
    msgbox.exec_()


# 确认保存提示
def msg_confirm(self, text):
    msgbox = QMessageBox(self)
    msgbox.setWindowTitle(u"信息提醒")
    msgbox.setText(text)
    ok_button = msgbox.addButton(unicode("OK"), QMessageBox.ActionRole)
    cancle_button = msgbox.addButton(unicode("Cancle"), QMessageBox.ActionRole)
    msgbox.exec_()

    button = msgbox.clickedButton()
    if button == ok_button:
        save(self)

