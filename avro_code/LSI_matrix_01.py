#算出文本之间的相似度,结果以矩阵的形式输出
from gensim import corpora, models, similarities
import logging
import csv
import re
from nltk.corpus import stopwords
from decimal import Decimal
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
flag=0
query_float=''
test=''
#打开包含所有文件名的目录
file = open('filename2.csv', 'r')
# 读取文件内容
topic_filename = csv.reader(file)
#去除停用词，得到有用的信息文本
documents=[]
for topics in topic_filename:
    file_name = open(topics[0] +".csv", 'r')
    # 读取文件内容
    files_names = csv.reader(file_name)
    str1= ""
    str_text=""
    flag1=-2
    for files_name in files_names:
        if flag1<0:
            flag1+=1
            continue
        if (files_name[1] == "Comment" or files_name[1] == "Identifier"):
                str1 += " " + files_name[0]

    str1=str1.lower()
    text_list = re.sub("[^a-zA-Z]", " ", str1).split()

    # 2 q去掉标点符号和停用词
    # 去掉标点符号
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', '"', '//*',
                            '*//','apache','license','asf','licensed','software']
    text_list = [word for word in text_list if word not in english_punctuations]
    # 去掉停用词
    stops = set(stopwords.words("english"))
    text_list = [word for word in text_list if word not in stops]
    for list in text_list:
        str_text += ' ' + list
    documents.append(str_text)

texts = [[word for word in document.lower().split()] for document in documents]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=50)
corpus_lsi = lsi[corpus_tfidf]
index = similarities.MatrixSimilarity(lsi[corpus])
for docu in documents:
    query = docu
    query_bow = dictionary.doc2bow(query.lower().split())
    query_lsi = lsi[query_bow]
    sims = index[query_lsi]
    # 将一行的数据储存起来
    str_txt = ""
    for i, element in enumerate(sims):
        if element>=0.8:
            element1=1
        else:
            element1=0
        str_txt += str(element1) + " "
    print(str_txt)
    f= open('C:\\Users\sherlock\Desktop\\avro_1.7.7matrix_01.txt', 'a')
    f.write(str_txt + '\n')
    f.close()
    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
    print(len(sims))
    print(sort_sims)
#将文件信息写入
#打开包含所有文件名的目录
file = open('filename_path.csv', 'r')
# 读取文件内容
topic_filename = csv.reader(file)
for topics in topic_filename:
    f = open('C:\\Users\sherlock\Desktop\\avro_1.7.7matrix_01.txt', 'a')
    f.write(topics[0] + '\n')
f.close()


