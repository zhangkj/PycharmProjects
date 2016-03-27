# -*- coding:utf-8 -*-
import  pandas as pd
import  re
from  fn_BaiduTranslate import  BaiDuTranslate
import xlrd

def FindSrtUnKnowWord():
        srtFilePath = 'SrtFiles/Kung.Fu.Panda_English.srt'
        strKnowedWordPath = 'Knowed.csv'
        captionContentlist = []
        captionWordlist = []
        knowedWord = []
        with open(srtFilePath,'r') as fn:
                content = fn.read().lower()
                captionContentlist = re.findall('\d\n(\D.*?)\n.*?',content) #将字幕中的序列数字和时间等信息过滤掉，值提取了行英语内容
                content = re.sub('<.*?.>','',content)   #将数据中的<i>等html字符替换掉
                captionWordlist = re.findall('([a-zA-Z].*?)[\s.*!?,\n]',content)
                #print captionWordlist

        #获取已经认识的单词数据
        SKnowed = pd.read_csv(strKnowedWordPath, header=None,names=["word"]).values
        #print SKnowed

        #将匹配后的纯字幕文本写入到txt文件中
        """
        with open("newCaption.txt",'w') as fnW:
            for strText in captionContentlist:
                fnW.writelines(strText+"\n")
            fnW.close()
        """
        #用pandans对文件中提取的单词进行计数汇总
        wordframe = pd.Series(captionWordlist).value_counts()
        clean_word = {}
        wordTranslate =[]
        for word in wordframe.index:
                if word not in SKnowed:           #过滤掉已经认识的word
                        clean_word[word]=BaiDuTranslate().Start(word.strip())
                        print clean_word[word]
        #print clean_word
        Serise_word= pd.Series(clean_word)
        print Serise_word.head()
        print len(Serise_word)
        Serise_word.to_csv("word_count.csv", encoding='utf-8')

FindSrtUnKnowWord()