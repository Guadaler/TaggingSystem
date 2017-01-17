#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：主界面
# Author: zx
# Software: PyCharm Community Edition
# File: main.py
# Time: 17-1-16 上午11:03
# -------------------------------------------

import sys

from PyQt4 import QtGui

import form
import function


def run_form():

    # 初始化：读取文件，初始化第一条文本，初始化第一个词
    function.read_file()
    function.init_text(0)
    function.init_word(0)

    # 显示主页面
    app = QtGui.QApplication(sys.argv)
    win = form.Ui_Dialog()
    win.show()
    # 数据填充
    function.fill(win)
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_form()
