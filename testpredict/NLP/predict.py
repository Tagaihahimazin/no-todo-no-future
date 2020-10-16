import glob
import os
import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from .preprocessings.tokenizer import JanomeTokenizer
from .preprocessings.normalizer import normalize

def load_model_file():
  #import pickle
  with open('testpredict/NLP/model/count.pickle', mode='rb') as fp:
    count = pickle.load(fp)

  #学習済みデータの読み出し 
  with open('testpredict/NLP/model/model.pickle', mode='rb') as fp:
    clf = pickle.load(fp)
  return count,clf




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
    print('test')
  else:
    count,clf=load_model_file()

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


  if pred.max()<-1:
    return 'other'
    #print('else')
  else:
    return inverse_lookup(category,pred.argmax())
    #print(inverse_lookup(category,pred.argmax()))


#print(predict(input_task1))
