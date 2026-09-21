from gensim.models import Word2Vec

sentences=[["the","cat","is","sitting","on","the","mat"],
           ["the","dog","is","sitting","on","the","floor"],
           ["the","cat","and","dog","are","animals"],
           ["dogs","and","cat","are","good","pets"]
          ]

model=Word2Vec(
    sentences,
    vector_size=50,
    window=2,
    min_count=1,
    workers=1,
)

print("Vector of cat:")
print(model.wv["cat"])

print("\nWord similar to 'cat' ")
print(model.wv.most_similar("cat",topn=3))