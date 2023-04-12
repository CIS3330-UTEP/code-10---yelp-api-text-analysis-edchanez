from yelpapi import YelpAPI
import pandas as pd

api_key = "r_PCQETtPYslevCCq0RBsvxh6rHtnGbO7yfGlUf451AKoAYAQ5hTW82lNR4jWkGOuKuEm1BYFWmbyMNdl1uQoSh3tmtU3RaroUnvEWBlMovUT79iSXjKlqaoB60zZHYx"

yelp_api = YelpAPI(api_key)

#search_query

search_term = "pizza"
search_location = "Chicago, IL"
search_sort_by = "rating" #best_match, rating, review_count, distance
search_limit = 20

search_results = yelp_api.search_query(term=search_term,location=search_location,sort_by=search_sort_by, limit=search_limit)

# print(search_results)

# for business in search_results['name']:
#     print(business['name'])
#     print(business['alias'])
#     print("\n")

result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df['alias'])
# result_df.to_csv("yelpAPI_TEST.csv")
id_for_reviews = "montis-chicago"

#reviews query

reviews_result = yelp_api.reviews_query(id=id_for_reviews)

# print(reviews_result)

# for review in reviews_result['reviews']:
#     print(review)
#     print("\n\n")

reviews_df= pd.DataFrame.from_dict(reviews_result['reviews'])

print(reviews_df['text'])






