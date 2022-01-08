import sys
import re
import os

bad_words = list(sys.argv)[1:]
fname = "tweet.js"

# Functions that clean the data
get_text = lambda t: re.match(r'\"full_text\" : \"(.*)\"', t.strip())[1] # get the text from the correct .js line
word_match = lambda w: ("@" not in w) and ("https://" not in w) # remove people's @s and URLs from tweet text
not_retweet = lambda t: re.match("^RT @.+\:", t) is None # only keep original tweets, not RTs
no_bad_word = lambda t: not any(re.search(w, t, re.I) for w in bad_words) # remove the user-specified bad words
no_at_or_url = lambda t: ' '.join(filter(word_match, t.split(" "))) # looks word by word for @s and URLs
no_single_words = lambda t: len(t.split(" ")) > 1 # removes single-word tweets

tweets = [l for l in open(fname, "r") if "full_text" in l] # get the correct .js lines
# These apply the above functions to the tweets
tweets = map(get_text, tweets) 
tweets = filter(not_retweet, tweets)
tweets = filter(no_bad_word, tweets)
tweets = map(no_at_or_url, tweets)
tweets = filter(no_single_words, tweets)

# This writes the result to a text file
os.remove('tweets.txt')
with open('tweets.txt', 'w') as f:
    for t in tweets:
        f.write(f"{t} \n")