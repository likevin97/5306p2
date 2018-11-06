import csv
import matplotlib.pyplot as plt
import numpy as np

# Load data
with open("Tweets.csv") as f:
    reader = csv.DictReader(f)
    data = [line for line in reader]

# Preprocess steps
for tweet in data:
    tweet["text"] = tweet["text"]

# Define airports (Top 20 according to Wikipedia)
# https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_the_United_States
airports = [
    # format: airport_code, major_city, [additional potential names ...]
    ["ATL", "Atlanta", "atlanta"],
    ["LAX", "Los Angeles", "los angeles"],
    ["ORD", "Chicago", "chicago"],
    ["DFW", "Dallas", "dallas"],
    ["DEN", "Denver", "denver"],
    ["JFK", "New York", "new york", "NYC", "nyc"],
    ["SFO", "San Francisco", "san francisco", "SF", "sf"],
    ["LAS", "Las Vegas", "las vegas"],
    ["SEA", "Seattle", "seattle"],
    ["CLT", "Charlotte", "charlotte"],
    ["EWR", "Newark", "newark"],
    ["MCO", "Orlando", "orlando"],
    ["PHX", "Phoenix", "phoenix"],
    ["MIA", "Miami", "miami"],
    ["IAH", "Houston", "houston"],
    ["BOS", "Boston", "boston"],
    ["MSP", "Minneapolis", "minneapolis"],
    ["DTW", "Detroit", "detroit"],
    ["FLL", "Fort Lauderdale", "fort lauderdale"],
    ["PHL", "Philadelphia", "philadelphia", "Philly", "philly"]
]

def airportReferences(text):
    """Returns a list of all the airports detected in the tweet"""
    refs = map(lambda names: names[0] if \
                    any([name in text for name in names]) \
                    else None, airports)
    return list(filter(lambda x: x is not None, refs))

all_filt_tweets = []
airport_tweets = {airport[0] : [] for airport in airports}
for tweet in data:
    refs = airportReferences(tweet["text"])
    if len(refs):
        [airport_tweets[r].append(tweet) for r in refs]
        all_filt_tweets.append(tweet)

# Some print statements for sanity checks
print("Prior to filtering, data points:", len(data))
print("After filtering:", len(all_filt_tweets))
print()
for k,v in airport_tweets.items():
    print(k, len(v))
    print("First tweet: ", v[0]['text'])
    print()

print("====== Sentiment Counts ======")
t_pos_data = []
t_neg_data = []
for airport_code, tweets in airport_tweets.items():
    sents = list(map(lambda twt: twt["airline_sentiment"], tweets))
    pos = list(filter(lambda x: x == "positive", sents))
    neg = list(filter(lambda x: x == "negative", sents))
    neut = list(filter(lambda x: x == "neutral", sents))
    t_pos_data.append((round(len(pos)/len(sents),2), airport_code))
    t_neg_data.append((round(len(neg)/len(sents),2), airport_code))
    #print(airport_code, "[ pos:", round(len(pos)/len(sents),2), "// neg:", round(len(neg)/len(sents),2), "// neut:", round(len(neut)/len(sents),2), "]")

N = len(airports)
ind = np.arange(N)
width = 0.8

t_pos_data.sort()
t_pos_data.reverse()
pos_airports = [t[1] for t in t_pos_data]
pos_data = [t[0] for t in t_pos_data]
t_neg_data.sort()
t_neg_data.reverse()
neg_airports = [t[1] for t in t_neg_data]
neg_data = [t[0] for t in t_neg_data]

p = plt.bar(ind, pos_data, width)
plt.ylabel('Positive Tweet Percentage')
plt.xlabel('Airport')
plt.title('Percentage of Positive Tweets by Airport')
plt.xticks(ind, pos_airports)
plt.yticks(np.arange(0, 0.41, 0.1))
plt.xticks(fontsize=9, rotation=90)
plt.show()
