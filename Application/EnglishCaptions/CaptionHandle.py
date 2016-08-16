# -*- coding:utf-8 -*-
import  pandas as pd
import  re
from  fn_BaiduTranslate import  BaiDuTranslate
import xlrd
import  datetime

def FindSrtUnKnowWord():
    # srtFilePath = 'SrtFiles/Kung.Fu.Panda_English.srt'
    srtFilePath = 'SrtFiles/5 tips To Make a Killer First Impression - Personality Development & English lessons by Niharika.srt'
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
    SKnowed = pd.read_csv(strKnowedWordPath, header=None,names=["word"])
    SKnowed = SKnowed.to_dict(orient = 'list')['word'] #将dataframe格式内容转化成list形式
    #print SKnowed

    #将匹配后的纯字幕文本写入到txt文件中
    """
    with open("newCaption.txt",'w') as fnW:
        for strText in captionContentlist:
            fnW.writelines(strText+"\n")
        fnW.close()
    """
    #用pandans对文件中提取的单词进行计数汇总
    series = pd.Series(captionWordlist)
    wordframe = pd.Series(captionWordlist).value_counts()
    dfword =  pd.DataFrame([wordframe.index,wordframe.values]).dropna()
    dfword = dfword.T
    # print SKnowed
    # print dfword
    dfword = dfword[dfword[0].isin(SKnowed)==False]
    dfword[2] = dfword[0].apply(lambda x:BaiDuTranslate().Start(str(x).strip()))
    # for word in dfword.values:
    #         if word not in SKnowed:           #过滤掉已经认识的word
    #                 print "====",word[0],word[2]
    #                 word[2]=BaiDuTranslate().Start(str(word[0]).strip())
    #                 break

    print dfword.head()
    print len(dfword)
    dfword.to_csv("output/wordcount.csv", encoding='utf-8')

FindSrtUnKnowWord()