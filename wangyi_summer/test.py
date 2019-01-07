#!user/bin/env python
# -*- coding:UTF-8 -*-
# python test.py
# kiki 2018/12/29 python3.5
"""
something write for my roomate_oldSummer
it is use for read and do something with cpp
test code
"""

from PyMacroParser import PyMacroParser

def main():
	a1 = PyMacroParser()
	a2 = PyMacroParser()
	a1.load("a.cpp")
	filename = "b.cpp"
	a1.dump(filename) #没有预定义宏的情况下，dump cpp
	a2.load(filename)
	a2.dumpDict()
	a1.preDefine("MC1;MC2") #指定预定义宏，再dump
	a1.dumpDict()
	a1.dump("c.cpp")

if __name__ == "__main__":
	# main()
	a = PyMacroParser()
	a.load("a.cpp")
	print ("_______________________")
	# print (a.originHong)
	for Hong in a.originHong:
		print (Hong)