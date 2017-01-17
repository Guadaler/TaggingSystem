#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------
# 功能：界面设计模块
# Author: zx
# Software: PyCharm Community Edition
# File: main.py
# Time: 17-1-16 上午11:03
# -------------------------------------------
from PyQt4 import QtCore, QtGui
import function
import sys

reload(sys)
sys.setdefaultencoding('utf8')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.names = locals()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setEnabled(True)
        Dialog.resize(740, 752)

        # frame_1 : 原始分词文本
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 10, 701, 271))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 681, 251))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setWordWrap(True)

        # fram_2 : 待标注的关键词
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 290, 291, 101))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 221, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 221, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        # fram_3：切分错误调整区域
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(350, 290, 371, 101))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.text = QtGui.QTextEdit(self.frame_3)
        self.text.setGeometry(QtCore.QRect(260, 10, 91, 31))
        self.text.setObjectName(_fromUtf8("text"))
        self.pushButton_1 = QtGui.QPushButton(self.frame_3)
        self.pushButton_1.setGeometry(QtCore.QRect(140, 10, 91, 31))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 60, 91, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 60, 91, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        # frame_4：主要标注区域
        self.frame_4 = QtGui.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(20, 410, 701, 331))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.pushButton_6 = QtGui.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 121, 41))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 10, 121, 41))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 10, 121, 41))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(430, 10, 121, 41))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.frame_4)
        self.pushButton_10.setGeometry(QtCore.QRect(570, 10, 121, 41))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(self.frame_4)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 70, 121, 41))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(self.frame_4)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 70, 121, 41))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_13 = QtGui.QPushButton(self.frame_4)
        self.pushButton_13.setGeometry(QtCore.QRect(290, 70, 121, 41))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(self.frame_4)
        self.pushButton_14.setGeometry(QtCore.QRect(430, 70, 121, 41))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15 = QtGui.QPushButton(self.frame_4)
        self.pushButton_15.setGeometry(QtCore.QRect(570, 70, 121, 41))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16 = QtGui.QPushButton(self.frame_4)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 130, 121, 41))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.pushButton_17 = QtGui.QPushButton(self.frame_4)
        self.pushButton_17.setGeometry(QtCore.QRect(150, 130, 121, 41))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton_18 = QtGui.QPushButton(self.frame_4)
        self.pushButton_18.setGeometry(QtCore.QRect(290, 130, 81, 41))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.pushButton_19 = QtGui.QPushButton(self.frame_4)
        self.pushButton_19.setGeometry(QtCore.QRect(400, 130, 81, 41))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.pushButton_20 = QtGui.QPushButton(self.frame_4)
        self.pushButton_20.setGeometry(QtCore.QRect(510, 130, 71, 41))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.pushButton_21 = QtGui.QPushButton(self.frame_4)
        self.pushButton_21.setGeometry(QtCore.QRect(610, 130, 81, 41))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.pushButton_22 = QtGui.QPushButton(self.frame_4)
        self.pushButton_22.setGeometry(QtCore.QRect(10, 190, 121, 41))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.pushButton_23 = QtGui.QPushButton(self.frame_4)
        self.pushButton_23.setGeometry(QtCore.QRect(150, 190, 121, 41))
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.pushButton_24 = QtGui.QPushButton(self.frame_4)
        self.pushButton_24.setGeometry(QtCore.QRect(290, 190, 81, 41))
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.pushButton_25 = QtGui.QPushButton(self.frame_4)
        self.pushButton_25.setGeometry(QtCore.QRect(400, 190, 81, 41))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.pushButton_26 = QtGui.QPushButton(self.frame_4)
        self.pushButton_26.setGeometry(QtCore.QRect(510, 190, 71, 41))
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.pushButton_27 = QtGui.QPushButton(self.frame_4)
        self.pushButton_27.setGeometry(QtCore.QRect(610, 190, 81, 41))
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))


        self.pushButton_28 = QtGui.QPushButton(self.frame_4)
        self.pushButton_28.setGeometry(QtCore.QRect(10, 250, 121, 41))
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.pushButton_29 = QtGui.QPushButton(self.frame_4)
        self.pushButton_29.setGeometry(QtCore.QRect(150, 250, 121, 41))
        self.pushButton_29.setObjectName(_fromUtf8("pushButton_29"))
        self.pushButton_30 = QtGui.QPushButton(self.frame_4)
        self.pushButton_30.setGeometry(QtCore.QRect(290, 250, 81, 41))
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.pushButton_31 = QtGui.QPushButton(self.frame_4)
        self.pushButton_31.setGeometry(QtCore.QRect(400, 250, 81, 41))
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.pushButton_32 = QtGui.QPushButton(self.frame_4)
        self.pushButton_32.setGeometry(QtCore.QRect(510, 250, 81, 41))
        self.pushButton_32.setObjectName(_fromUtf8("pushButton_32"))
        self.pushButton_33 = QtGui.QPushButton(self.frame_4)
        self.pushButton_33.setGeometry(QtCore.QRect(610, 250, 81, 41))
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        # 设置空间中文名显示
        self.retranslateUi(Dialog)

        # 绑定激活事件
        QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.merge_pre)  # 向前合并
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.merge_next)  # 向后合并
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.split_position)  # 按位拆分
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.word_pre)  # 上一个单词
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.word_next)  # 下一个单词
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.n)  # 名词
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.v)  # 动词
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.adj)  # 形容词
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.adv)  # 副词
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL(_fromUtf8("clicked()")), self.w)  # 标点符号
        QtCore.QObject.connect(self.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.c)  # 连词
        QtCore.QObject.connect(self.pushButton_12, QtCore.SIGNAL(_fromUtf8("clicked()")), self.p)  # 介词
        QtCore.QObject.connect(self.pushButton_13, QtCore.SIGNAL(_fromUtf8("clicked()")), self.r)  # 代词
        QtCore.QObject.connect(self.pushButton_14, QtCore.SIGNAL(_fromUtf8("clicked()")), self.m)  # 数词 numeral
        QtCore.QObject.connect(self.pushButton_15, QtCore.SIGNAL(_fromUtf8("clicked()")), self.q)  # 量词 quantity
        QtCore.QObject.connect(self.pushButton_16, QtCore.SIGNAL(_fromUtf8("clicked()")), self.u)  # 助词 auxiliary
        QtCore.QObject.connect(self.pushButton_17, QtCore.SIGNAL(_fromUtf8("clicked()")), self.t)  # 时间词 time
        QtCore.QObject.connect(self.pushButton_18, QtCore.SIGNAL(_fromUtf8("clicked()")), self.f)  # 方位词
        QtCore.QObject.connect(self.pushButton_19, QtCore.SIGNAL(_fromUtf8("clicked()")), self.e)  # 叹词 exclamation
        QtCore.QObject.connect(self.pushButton_20, QtCore.SIGNAL(_fromUtf8("clicked()")), self.y)  # 语气词
        QtCore.QObject.connect(self.pushButton_21, QtCore.SIGNAL(_fromUtf8("clicked()")), self.o)  # 拟声词 onomatopoeia
        QtCore.QObject.connect(self.pushButton_22, QtCore.SIGNAL(_fromUtf8("clicked()")), self.s)  # 处所词 space
        QtCore.QObject.connect(self.pushButton_23, QtCore.SIGNAL(_fromUtf8("clicked()")), self.b)  # 区别词
        QtCore.QObject.connect(self.pushButton_24, QtCore.SIGNAL(_fromUtf8("clicked()")), self.z)  # 状态词
        QtCore.QObject.connect(self.pushButton_25, QtCore.SIGNAL(_fromUtf8("clicked()")), self.h)  # 前缀
        QtCore.QObject.connect(self.pushButton_26, QtCore.SIGNAL(_fromUtf8("clicked()")), self.k)  # 后缀
        QtCore.QObject.connect(self.pushButton_27, QtCore.SIGNAL(_fromUtf8("clicked()")), self.x)  # 字符串
        QtCore.QObject.connect(self.pushButton_28, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nr)  # 人名
        QtCore.QObject.connect(self.pushButton_29, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ns)  # 地名
        QtCore.QObject.connect(self.pushButton_30, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nt)  # 机构团体
        QtCore.QObject.connect(self.pushButton_31, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nz)  # 其他专名
        QtCore.QObject.connect(self.pushButton_32, QtCore.SIGNAL(_fromUtf8("clicked()")), self.next_text)  # 下一篇
        QtCore.QObject.connect(self.pushButton_33, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)  # 保存
        # QtCore.QObject.connect(self.pushButton_, QtCore.SIGNAL(_fromUtf8("clicked()")), self.)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "【221数据之人工词性标注系统】", None))
        self.label.setText(_translate("Dialog", "TextLabel", None))
        self.label_3.setText(_translate("Dialog", "TextLabel", None))
        self.label_2.setText(_translate("Dialog", "TextLabel", None))
        self.pushButton_1.setText(_translate("Dialog", "向前合并", None))
        self.pushButton_2.setText(_translate("Dialog", "向后合并", None))
        self.pushButton_3.setText(_translate("Dialog", "拆  分", None))
        self.pushButton_4.setText(_translate("Dialog", "前一个", None))
        self.pushButton_5.setText(_translate("Dialog", "后一个", None))
        self.pushButton_6.setText(_translate("Dialog", "名词", None))
        self.pushButton_7.setText(_translate("Dialog", "动词", None))
        self.pushButton_8.setText(_translate("Dialog", "形容词", None))
        self.pushButton_9.setText(_translate("Dialog", "副词", None))
        self.pushButton_10.setText(_translate("Dialog", "标点符号", None))
        self.pushButton_11.setText(_translate("Dialog", "连词", None))
        self.pushButton_12.setText(_translate("Dialog", "介词", None))
        self.pushButton_13.setText(_translate("Dialog", "代词", None))
        self.pushButton_14.setText(_translate("Dialog", "数词", None))
        self.pushButton_15.setText(_translate("Dialog", "量词", None))
        self.pushButton_16.setText(_translate("Dialog", "助词", None))
        self.pushButton_17.setText(_translate("Dialog", "时间词", None))
        self.pushButton_18.setText(_translate("Dialog", "方位词", None))
        self.pushButton_19.setText(_translate("Dialog", "叹词", None))
        self.pushButton_20.setText(_translate("Dialog", "语气词", None))
        self.pushButton_21.setText(_translate("Dialog", "拟声词", None))
        self.pushButton_22.setText(_translate("Dialog", "处所词", None))
        self.pushButton_23.setText(_translate("Dialog", "区别词", None))
        self.pushButton_24.setText(_translate("Dialog", "状态词", None))
        self.pushButton_25.setText(_translate("Dialog", "前缀", None))
        self.pushButton_26.setText(_translate("Dialog", "后缀", None))
        self.pushButton_27.setText(_translate("Dialog", "字符串", None))
        self.pushButton_28.setText(_translate("Dialog", "人名", None))
        self.pushButton_29.setText(_translate("Dialog", "地名", None))
        self.pushButton_30.setText(_translate("Dialog", "机构团体", None))
        self.pushButton_31.setText(_translate("Dialog", "其他专名", None))
        self.pushButton_32.setText(_translate("Dialog", "下一篇", None))
        self.pushButton_33.setText(_translate("Dialog", "保 存", None))

    # 向前合并
    def merge_pre(self):
        function.merge_pre(self)

    # 向后合并
    def merge_next(self):
        function.merge_next(self)

    # 按位拆分
    def split_position(self):
        function.split_position(self)

    # 前一个词
    def word_pre(self):
        function.word_pre(self)

    # 后一个词
    def word_next(self):
        function.word_next(self)

    # 名词
    def n(self):
        function.pos_tag(self, "n")

    # 动词
    def v(self):
        function.pos_tag(self, "v")

    # 形容词
    def adj(self):
        function.pos_tag(self, "adj")

    # 副词
    def adv(self):
        function.pos_tag(self, "adv")

    # 标点符号
    def w(self):
        function.pos_tag(self, "w")

    # 连词
    def c(self):
        function.pos_tag(self, "c")

    # 介词
    def p(self):
        function.pos_tag(self, "p")

    # 代词
    def r(self):
        function.pos_tag(self, "r")

    # 数词
    def m(self):
        function.pos_tag(self, "m")

    # 量词
    def q(self):
        function.pos_tag(self, "q")

    # 助词
    def u(self):
        function.pos_tag(self, "u")

    # 时间词
    def t(self):
        function.pos_tag(self, "t")

    # 方位词
    def f(self):
        function.pos_tag(self, "f")

    # 叹词
    def e(self):
        function.pos_tag(self, "e")

    # 语气词
    def y(self):
        function.pos_tag(self, "y")

    # 拟声词
    def o(self):
        function.pos_tag(self, "o")

    # 处所词
    def s(self):
        function.pos_tag(self, "s")

    # 区别词
    def b(self):
        function.pos_tag(self, "b")

    # 状态词
    def z(self):
        function.pos_tag(self, "z")

    # 前缀
    def h(self):
        function.pos_tag(self, "h")

    # 后缀
    def k(self):
        function.pos_tag(self, "k")

    # 字符串
    def x(self):
        function.pos_tag(self, "x")

    # 人名
    def nr(self):
        function.pos_tag(self, "nr")

    # 地名
    def ns(self):
        function.pos_tag(self, "ns")

    # 机构团体
    def nt(self):
        function.pos_tag(self, "nt")

    # 专有名词
    def nz(self):
        function.pos_tag(self, "nz")

    # 下一篇
    def next_text(self):
        function.next_text(self)

    # 保存
    def save(self):
        function.msg_confirm(self, u"确认保存么？")
