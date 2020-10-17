# This Python file uses the following encoding: utf-8
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from .preprocessings.tokenizer import JanomeTokenizer
from .preprocessings.normalizer import normalize
#from preprocessings.livedoor import load_df
from .preprocessings.original_data import load_df
from . import predict
import os
import base64


def train():

    # janomeでトークナイズ
    janome = JanomeTokenizer()
    def tokenize(word):
        tokens = [normalize(janome.surface(token)) for token in janome.tokenize(word)]
        return " ".join(tokens)

    # ラベル付きでDataFrameとして読み込み
    df = load_df()
    print(df)

    # 文全てをtokenize
    df['docs'] = df['docs'].apply(tokenize)

    #print(df)

    # BOWで文をベクトル化
    count = CountVectorizer()
    X_count = count.fit_transform(df['docs'].values)
    import pickle
    #with open('./model/count.pickle', mode='wb') as fp:
    #    pickle.dump(count, fp)
    str_count = base64.b64encode(pickle.dumps(count)).decode("utf-8")
    json_count = {"pickle": str_count}


    # トレーニング:テスト = 8:2で分ける
    X_train, X_test, Y_train, Y_test = train_test_split(X_count, df['labels'], test_size=0.1,random_state=3)
    #X_train=X_count
    #Y_train= df['labels']


    # LogisticRegressionで分類
    clf = LogisticRegression()
    clf.fit(X_train, Y_train)

    #学習モデルを保存
    #import pickle
    #with open('./model/model.pickle', mode='wb') as fp:
    #    pickle.dump(clf, fp)

    str_clf= base64.b64encode(pickle.dumps(clf)).decode("utf-8")
    json_clf = {"pickle": str_clf}

    #DBにアップロード
    predict.upload_db(str_clf,str_count)


    # テストデータで正確性(accuracy)を表示
    #print(clf.score(X_train, Y_train))
    print(clf.score(X_test, Y_test))

