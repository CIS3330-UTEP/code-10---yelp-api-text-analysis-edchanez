import nltk
nltk.download('averaged_perceptron_tagger')
reviews = open('ice_cream_reviews.txt')

for review in reviews:

    tokens = nltk.word_tokenize(review)
    pos_tags = nltk.pos_tag(tokens)
    print(pos_tags)   