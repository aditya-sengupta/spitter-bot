# spitterbot

This README contains instructions for having your tweets included in the Spitter Bot!

Since Twitter API scrapers are all paid services that would also take a while to run, I'm making use of Twitter's feature (that they're obligated to have under the General Data Protection Regulation) where they let you download all data associated with your account.

First, to get your data, follow the steps at [this link](https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive). They'll usually take about a day to do this, and the download will be available for a week, so make sure you do the next steps in that time!

Next, download your data, open the .zip, and move the file called `data/tweet.js` into a new folder that also contains `extract.py` in this repo. Then, run `python3 extract.py`, which will extract only the text of tweets, filter out retweets, and filter out @s to other people. It'll save this to a text file named `tweets.txt`, which I'd appreciate if you could manually rename to your @, such as `adiastra99.txt`. (There's a way to automate this, but it'd need me to look in a different js file, so this is simpler.)

The file `tweet.js` should only contain tweets you made that are publicly viewable (other things are elsewhere in the directory); the only edge case I can think of is if your account used to be private and is now public, I don't know whether the tweets you made privately are now publicly viewable. If there's anything in there that you'd rather I didn't see, most of the filtering will have to be done manually by you, but I've provided one tool: if you instead run `python3 extract.py badword1 badword2 badword3`, with as many bad words as you'd like, the script will remove any tweets you've made with those words. For example, if I've made some controversial tweets about milk products that I don't want the Dairy Lobby to see, I might run `python3 extract.py milk yogurt cheese`, and that would probably cover me.

Once you're satisfied with the content of your `(at).txt`, send it over to me! If you trust me and don't want to deal with Python stuff yourself, you're welcome to send me your `tweet.js` directly. As an example of what you should get, I've included my own `tweet.js` and the resulting file `adiastra99.txt`.

Thanks for your help with this project!
