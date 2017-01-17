#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：全局变量模块
# Author: zx
# Software: PyCharm Community Edition
# File: globe.py
# Time: 17-1-16 上午11:13
# -------------------------------------------
# 输入文件位置
input_path = "/home/zhangxin/work/workplace_python/TaggingSystem/data/input"
output_path = "/home/zhangxin/work/workplace_python/TaggingSystem/data/output"


# 文本集合
text_all = []
text = ""
text_index = 0

# 关键词集合
word_all = []
word = ""
word_index = 0

# 词性标注集
tag_dict = {
    # 名词
    "n": u"名词",

    # 动词
    "v": u"动词",

    # 形容词
    "adj": u"形容词",

    # 副词
    "adv": u"副词",

    # 标点符号
    "w": u"标点符号",

    # 连词
    "c": u"连词",

    # 介词
    "p": u"介词",

    # 代词
    "r": u"代词",

    # 数词
    "m": u"数词",

    # 量词
    "q": u"量词",

    # 助词
    "u": u"助词",

    # 时间词
    "t": u"时间词",

    # 方位词
    "f": u"方位词",

    # 叹词
    "e": u"叹词",

    # 语气词
    "y": u"语气词",

    # 拟声词
    "o": u"拟声词",

    # 处所词
    "s": u"处所词",

    # 区别词
    "b": u"区别词",

    # 状态词
    "z": u"状态词",

    # 前缀
    "h": u"前缀",

    # 后缀
    "k": u"后缀",

    # 字符串
    "x": u"字符串",

    # 人名
    "nr": u"人名",

    # 地名
    "ns": u"地名",

    # 机构团体
    "nt": u"机构团体",

    # 专有名词
    "nz": u"专有名词",
}
