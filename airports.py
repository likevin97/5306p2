import csv

# Load data
with open("Tweets.csv") as f:
    reader = csv.DictReader(f)
    data = [line for line in reader]

# Preprocess steps
for tweet in data:
    tweet["text"] = tweet["text"].lower()

# Define airports (Top 20 according to Wikipedia)
# https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_the_United_States
airports = [
    # format: airport_code, major_city, [additional potential names ...]
    ["ATL", "Atlanta"],
    ["LAX", "Los Angeles"],
    ["ORD", "Chicago"],
    ["DFW", "Dallas"],
    ["DEN", "Denver"],
    ["JFK", "New York"],
    ["SFO", "San Francisco"],
    ["LAS", "Las Vegas"],
    ["SEA", "Seattle"],
    ["CLT", "Charlotte"],
    ["EWR", "Newark"],
    ["MCO", "Orlando"],
    ["PHX", "Phoenix"],
    ["MIA", "Miami"],
    ["IAH", "Houston"],
    ["BOS", "Boston"],
    ["MSP", "Minneapolis"],
    ["DTW", "Detroit"],
    ["FLL", "Fort Lauderdale"],
    ["PHL", "Philadelphia"],
]

def airportReferenceExists(text):
    return any(map(lambda names: any([name.lower() in text for name in names]), airports))

filt = [tweet for tweet in data if airportReferenceExists(tweet["text"])]

print("Prior to filtering, data points:", len(data))
print("After filtering:", len(filt))
