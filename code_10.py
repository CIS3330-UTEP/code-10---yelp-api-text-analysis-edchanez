import nltk
import pandas as pd
from yelpapi import YelpAPI
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# nltk.download('stopwords')

api_key = "r_PCQETtPYslevCCq0RBsvxh6rHtnGbO7yfGlUf451AKoAYAQ5hTW82lNR4jWkGOuKuEm1BYFWmbyMNdl1uQoSh3tmtU3RaroUnvEWBlMovUT79iSXjKlqaoB60zZHYx"

yelp_api = YelpAPI(api_key)

#search query
search_term = "pasta"
search_location = "El Paso, TX"
search_sort_by = "rating" #best_match, rating, review_count, distance
search_limit = 20

search_results = yelp_api.search_query(term=search_term,location=search_location,sort_by=search_sort_by, limit=search_limit)
print(search_results)

result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df['alias'])
# result_df.to_csv("yelpAPI_TEST.csv")
id_for_reviews = "buon-giorno-caffe-el-paso"


reviews_result = yelp_api.reviews_query(id=id_for_reviews)

print(reviews_result)


reviews_df= pd.DataFrame.from_dict(reviews_result['reviews'])

print(reviews_df['text'])

#adjectives 
for review in reviews_df['text']:
    tokens = nltk.word_tokenize(review)
    pos_tags = nltk.pos_tag(tokens)
    for tag in pos_tags:
        if tag[1] == 'JJ' or tag[1] == 'JJS':
            print(tag[0])
    print(pos_tags)   

#sentiment
# analyzer = SentimentIntensityAnalyzer()

# for review in reviews_df['text']:
#     sentiment_score = analyzer.polarity_scores(review)
#     print(review)
#     print(sentiment_score)
#     print("\n")

#stop words
stop_words = set(stopwords.words('english'))

new_text = []
for tag in pos_tags:
    if tag[0] not in stop_words:
        print(tag[0])
        new_text.append(tag[0])

print("\nOriginal")
print(review)
print("\nNew")
print(" ".join(new_text))
