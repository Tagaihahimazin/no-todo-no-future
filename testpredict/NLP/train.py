# This Python file uses the following encoding: utf-8
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from preprocessings.tokenizer import JanomeTokenizer
from preprocessings.normalizer import normalize
#from preprocessings.livedoor import load_df
from preprocessings.original_data import load_df
import os

#クラス数
num_class=6

# janomeでトークナイズ
# BOWで文をベクトル化
# LogisticRegressionで分類

# janomeでトークナイズ
janome = JanomeTokenizer()
def tokenize(word):
    tokens = [normalize(janome.surface(token)) for token in janome.tokenize(word)]
    return " ".join(tokens)

# livedoorの記事をラベル付きでDataFrameとして読み込み
df = load_df()

# 文全てをtokenize
df['docs'] = df['docs'].apply(tokenize)

#print(df)

# BOWで文をベクトル化
count = CountVectorizer()
X_count = count.fit_transform(df['docs'].values)
import pickle
with open('./model/count.pickle', mode='wb') as fp:
    pickle.dump(count, fp)


# トレーニング:テスト = 8:2で分ける
X_train, X_test, Y_train, Y_test = train_test_split(X_count, df['labels'], test_size=0.1,random_state=3)
#X_train=X_count
#Y_train= df['labels']


# LogisticRegressionで分類
clf = LogisticRegression()
clf.fit(X_train, Y_train)

#学習モデルを保存
import pickle
with open('./model/model.pickle', mode='wb') as fp:
    pickle.dump(clf, fp)

# テストデータで正確性(accuracy)を表示
#print(clf.score(X_train, Y_train))
print(clf.score(X_test, Y_test))

'''
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import TensorBoard,ModelCheckpoint




def dense(input_shape,output_shape):
    model = Sequential()

    model.add(Dense(64,input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(Dropout(0.25))
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dropout(0.25))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.25))
    model.add(Dense(output_shape))
    model.add(Activation('sigmoid'))

    return model




input_shape=X_train.shape[1:]
#output_shape=num_class
output_shape=Y_train.shape[1:]

model=dense(input_shape,output_shape)

model.compile(loss='categorical_crossentropy',metrics=['accuracy'],optimizer='rmsprop')


#データの記録
log_dir = os.path.join(os.path.dirname(__file__), "logdir")
model_file_name="model_file.hdf5"

#訓練
history = model.fit(
        X_train, Y_train,
         epochs=10,
         validation_split = 0.2,
         batch_size=8,
         callbacks=[
                TensorBoard(log_dir=log_dir),
                ModelCheckpoint(os.path.join(log_dir,model_file_name),save_best_only=True)
                ]
        )

loss,accuracy = model.evaluate(X_test, y_test, batch_size=8)
print('loss=',loss,'accuracy=',accuracy)

'''