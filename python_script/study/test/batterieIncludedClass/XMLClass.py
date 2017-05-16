#coding=utf-8
# 2016-06-28
__author__ = 'yangyang'
'''
XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用，所以，有必要了解如何操作XML。

DOM vs SAX

操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，
优点是可以任意遍历树的节点。
SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
正常情况下，优先考虑SAX，因为DOM实在太占内存。
'''
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self,name, attrs):
        print ('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self,name):
        print ('sax:end_element: %s' % name)

    def char_data(self, text):
        print ('sax:char_data :%s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)