import gensim.downloader as api
wv = api.load('word2vec-google-news-300')

vec_king = wv['king']
print(vec_king)
