import glob
import os
import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from .preprocessings.tokenizer import JanomeTokenizer
from .preprocessings.normalizer import normalize
from testpredict.models import load_NLP
from testpredict.models import load_NLP2
import base64
import json

def load_model_file():
  '''
  
  #import pickle
  with open('testpredict/NLP/model/count.pickle', mode='rb') as fp_count:
    bow = pickle.load(fp_count)

  #学習済みデータの読み出し 
  with open('testpredict/NLP/model/model.pickle', mode='rb') as fp_clf:
    model = pickle.load(fp_clf)
  '''
  d_count = {}
  with open("testpredict/NLP/model/count.json") as f:
    d_count = json.load(f)
  count = d_count["pickle"]

  #count = pickle.loads(base64.b64decode(s.encode()))

  d_clf = {}
  with open("testpredict/NLP/model/model.json") as f:
    d_clf = json.load(f)
  clf = d_clf["pickle"]

  #clf = pickle.loads(base64.b64decode(s.encode()))
  
  #return  bow,model
  #return fp_count,fp_clf
  return count,clf

def upload_db(count,clf):
  
  #書き込み
  #count,clf=load_model_file()
  #count_by= pickle.dumps(count)
  #clf_by= pickle.dumps(clf)
  #count_str=base64.b64encode(pickle.dumps(count)).decode("utf-8")
  #clf_str=base64.b64encode(pickle.dumps(clf)).decode("utf-8")
  #z=load_NLP(NLP_bow=count, NLP_clf=clf)

  z=load_NLP()
  z.NLP_bow=count
  z.save()

  q=load_NLP2()
  q.NLP_clf=clf
  q.save()
  
  print('ok')



#input_task1='資格の勉強'

def predict(input_task1='資格の勉強',debug=False):

  print(input_task1)
  # janomeでトークナイズ
  # BOWで文をベクトル化
  janome = JanomeTokenizer()
  def tokenize(word):
      tokens = [normalize(janome.surface(token)) for token in janome.tokenize(word)]
      return " ".join(tokens)


  docs  = [input_task1]
  df = pd.DataFrame(data = { 'docs': docs})

  #print(df)
  df['docs'] = df['docs'].apply(tokenize)

  import pickle
  if debug:
    
    count,clf=load_model_file()
  else:
    print('ok')
    #upload_db()
    
    data1=load_NLP.objects.get(pk=1)
    #bow={}
    bow=data1.NLP_bow
    data2=load_NLP2.objects.get(pk=1)
    #model={}
    model=data2.NLP_clf

    #print("aaaaaaaaaaaaaaaaaaaaaaaaa")
    #print(model)
    #count= pickle.load(bow)
    #clf= pickle.load(model)


    
    #clf = model["pickle"]
    #clf = pickle.loads(base64.b64decode(clf.encode()))
    #count = bow["pickle"]
    #count = pickle.loads(base64.b64decode(count.encode()))

    
    
    clf = pickle.loads(base64.b64decode(model.encode()))
    count = pickle.loads(base64.b64decode(bow.encode()))
    

 

  #fit_transformすると再学習しちゃうからあかん。
  X_test = count.transform(df['docs'].values)
  '''    
  #学習済みbowの呼び出し。
  #import pickle
  with open('testpredict/NLP/model/count.pickle', mode='rb') as fp:
    count = pickle.load(fp)
  #fit_transformすると再学習しちゃうからあかん。
  X_test = count.transform(df['docs'].values)

  #学習済みデータの読み出し 
  with open('testpredict/NLP/model/model.pickle', mode='rb') as fp:
    clf = pickle.load(fp)
  '''
 




  #推論
  pred=clf.predict_log_proba(X_test)

  category = {
      'study': 0,
      'work':1,
      'training':2,
      'buy':3,
      'contact':4,
      'programming':5,
      'kaji':6,
    }

  #逆引き
  def inverse_lookup(d, x):
      for k,v in d.items():
          if x == v:
              return k

  print(pred)


  if pred.max()<-1.1:
    return 'other'
    #print('else')
  else:
    return inverse_lookup(category,pred.argmax())
    #print(inverse_lookup(category,pred.argmax()))


#print(predict(input_task1))
