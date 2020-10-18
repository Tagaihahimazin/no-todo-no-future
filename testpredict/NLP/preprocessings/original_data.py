import glob
import os
import numpy as np
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_DIR = os.path.join(BASE_DIR, 'data', 'test_data')



def load_df():
  ##ラベルづけ
  category = {
    'study': 0,
    'work':1,
    'training':2,
    'buy':3,
    'contact':4,
    'programming':5,
    'kaji':6,
    
  }
  docs  = []
  labels = []

  for c_name, c_id in category.items():
    #files = glob.glob(data_DIR + "/text/{c_name}/*.txt".format(c_name=c_name))
    files=glob.glob("testpredict/NLP/data/test_data/text/{c_name}/*.txt".format(c_name=c_name))

    #text = ''
    for file in files:#一応複数データに対応
      with open(file, 'r',encoding="utf-8") as f:#######encoding="utf-8"
        lines = f.read().splitlines()#読み分け区分
        #lines=f.read()

        #url = lines[0]##1行目がURL
        #datetime = lines[1]##日程
        #subject = lines[2]###題名
        #body = "\n".join(lines[3:])###3行目以降本文
        #text = subject + "\n" + body

        #text=lines#今1行しかやってないから
        #print(len(lines))
     

        for i in range (len(lines)):
          docs.append(lines[i])
          labels.append(c_id)

      #docs.append(text)
      #labels.append(c_id)
  df = pd.DataFrame(data = { 'docs': docs, 'labels': labels })
  np.random.seed(0)
  #return df.reindex(np.random.permutation(df.index))
  return df


a=load_df()

#print(a)