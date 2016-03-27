# -*- coding: utf-8 -*-

import urllib
import codecs
from BeautifulSoup import BeautifulSoup
from sys import argv
import re,time

class BaiDuTranslate():
    def Start(self,textword=''):
        self.text = textword
        self._get_html_sourse()
        self._get_content("en-content")
        self._remove_tag()
        result = self.print_result()
        return  result
    def _get_html_sourse(self):
        word=argv[1] if len(argv)>1 else self.text
        url="http://dict.baidu.com/s?wd=%s&tn=dict" %  word
        self.htmlsourse=urllib.urlopen(url).read()
    def _get_content(self,div_id):
        soup=BeautifulSoup("".join(self.htmlsourse))
        self.data=str(soup.find("div",attrs={"class":div_id}))

    def _remove_tag(self):
        soup=BeautifulSoup(self.data)
        self.outtext=''.join([element  for element in soup.recursiveChildGenerator() if isinstance(element,unicode)])

    def print_result(self):
        for item in range(1,10):
            self.outtext=self.outtext.replace(str(item),"\n%s" % str(item))
        self.outtext=self.outtext.replace("  ","\n")
        #print self.outtext
        return self.outtext

#from sharejs.com
if __name__=="__main__":
     BaiDuTranslate().Start()