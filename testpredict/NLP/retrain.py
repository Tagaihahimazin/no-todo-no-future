# This Python file uses the following encoding: utf-8
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from .preprocessings.tokenizer import JanomeTokenizer
from .preprocessings.normalizer import normalize
#from preprocessings.livedoor import load_df
from .preprocessings.original_data import load_df
import os
import pickle
import base64
import json
import pandas as pd
import numpy as np

from testpredict.models import Taskclassification as task_class
'''
docs2=[]
docs2=task_class.objects.values_list('item', flat=True)
label_name=[]
label_name=task_class.objects.values_list('True_pred', flat=True)
category = {
      'study': 0,
      'work':1,
      'training':2,
      'buy':3,
      'contact':4,
      'programming':5,
      'kaji':6,
    }

label=[0]*len(label_name)
for i,name in enumerate(label_name):
  label[i]=category[name]
'''



# janomeでトークナイズ
# BOWで文をベクトル化
# LogisticRegressionで分類
#docs2  = ['洗濯機','ぞうきん']
#label=[6,6]

#def retrain(docs2,label):
def retrain():
    docs2=[]
    docs2=task_class.objects.values_list('item', flat=True)
    print("okkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    print(docs2)
    label_name=[]
    label_name=task_class.objects.values_list('True_pred', flat=True)
    category = {
        'study': 0,
        'work':1,
        'training':2,
        'buy':3,
        'contact':4,
        'programming':5,
        'kaji':6,
        }
    label=[0]*len(label_name)
    for i,name in enumerate(label_name):
        label[i]=category[name]


    # janomeでトークナイズ
    janome = JanomeTokenizer()
    def tokenize(word):
        tokens = [normalize(janome.surface(token)) for token in janome.tokenize(word)]
        return " ".join(tokens)

    # livedoorの記事をラベル付きでDataFrameとして読み込み
    df = load_df()


    #docs2  = ['洗濯機','ぞうきん']
    #label=[6,6]

    df2 = pd.DataFrame(data = { 'docs': docs2,'labels':label})
    # 文全てをtokenize
    df2['docs'] = df2['docs'].apply(tokenize)

    #print(df)

    # BOWで文をベクトル化(追加学習)
    count = CountVectorizer()

    #要素の追加
    df=pd.concat([df, df2]).reset_index(drop=True)
    #インデックスをシャッフル
    #np.random.seed(0)
    df=df.reindex(np.random.permutation(df.index))
    X_count = count.fit_transform(df['docs'].values)

    print(df)

    s = base64.b64encode(pickle.dumps(count)).decode("utf-8")
    d = {"pickle": s}
    with open("testpredict/NLP/model/count.json", "w") as f:
        json.dump(d, f)
        



    # トレーニング:テスト = 8:2で分ける
    X_train, X_test, Y_train, Y_test = train_test_split(X_count, df['labels'], test_size=0.2,random_state=3)
    #X_train=X_count
    #Y_train= df['labels']


    # LogisticRegressionで分類
    clf = LogisticRegression()
    clf.fit(X_train, Y_train)

    #学習モデルを保存
    #with open('./model/model.pickle', mode='wb') as fp:
        #pickle.dump(clf, fp)
    s = base64.b64encode(pickle.dumps(clf)).decode("utf-8")
        
    ###########
    d = {"pickle": s}
    with open("testpredict/NLP/model/model.json", "w") as f:
        json.dump(d, f)
    ############    

    # テストデータで正確性(accuracy)を表示
    #print(clf.score(X_train, Y_train))
    print(clf.score(X_test, Y_test))


#retrain(docs2,label)