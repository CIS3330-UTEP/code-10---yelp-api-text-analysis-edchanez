import nltk
import pandas as pd
from yelpapi import YelpAPI
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


api_key = "r_PCQETtPYslevCCq0RBsvxh6rHtnGbO7yfGlUf451AKoAYAQ5hTW82lNR4jWkGOuKuEm1BYFWmbyMNdl1uQoSh3tmtU3RaroUnvEWBlMovUT79iSXjKlqaoB60zZHYx"

yelp_api = YelpAPI(api_key)

#search query
search_term = "coffee"
search_location = "El Paso, TX"
search_sort_by = "rating" #best_match, rating, review_count, distance
search_limit = 20

search_results = yelp_api.search_query(term=search_term,location=search_location,sort_by=search_sort_by, limit=search_limit)
print(search_results)

result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df['alias'])
# result_df.to_csv("yelpAPI_TEST.csv")
id_for_reviews = "ambers-coffee-bar-horizon-city"





reviews_result = yelp_api.reviews_query(id=id_for_reviews)

print(reviews_result)


reviews_df= pd.DataFrame.from_dict(reviews_result['reviews'])

print(reviews_df['text'])

#adjectives 
for review in reviews_df['text']:
    tokens = nltk.word_tokenize(review)
    pos_tags = nltk.pos_tag(tokens)
    for tag in pos_tags:
        if tag[1] == 'JJ' or tag[1] == 'JJS' or tag[1] == 'NN':
            print(tag[0])
    print(pos_tags)   

#common adjectives and nouns for each coffee shop
# id_for_reviews = "2ten-coffee-roasters-el-paso" #friendly, attentive, service, atmosphere, location, tasty
# id_for_reviews = "viejo-coffee-el-paso-4" #little, spot, minimalist, modern, vibes, latte, horchata
# id_for_reviews = "café-con-leche-el-paso-6" #atmosphere, coffee, artsy, latte, hidden gem
# id_for_reviews = "lucys-coffee-shop-el-paso" #small, breakfast, great service, kitchen, food
# id_for_reviews = "ambers-coffee-bar-horizon-city" #pic, sweet staff,local, adorable, caramel, macchiato, good atmosphere


#sentiment
analyzer = SentimentIntensityAnalyzer()

for review in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print("\n")

#average sentiment scores
# id_for_reviews = "2ten-coffee-roasters-el-paso" avg 'neg' score:0.026, avg 'neu'score:0.738, avg 'pos' score: 0.236
# id_for_reviews = "viejo-coffee-el-paso-4" avg 'neg' score:0.044, avg 'neu'score:0.758, avg 'pos' score:0.197
# id_for_reviews = "café-con-leche-el-paso-6" avg 'neg' score:0.0, avg 'neu'score:0.717, avg 'pos' score: 0.85
# id_for_reviews = "lucys-coffee-shop-el-paso" avg 'neg' score:0.0, avg 'neu'score:0.762, avg 'pos' score: 0.713
# id_for_reviews = "ambers-coffee-bar-horizon-city" avg 'neg' score:0.032, avg 'neu'score:0.577, avg 'pos' score:0.391
