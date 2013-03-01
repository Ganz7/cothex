from flask import Flask, render_template
from scripts import twitterapi
app = Flask(__name__)

@app.route('/')
def home():
	tweets = twitterapi.searchTweets("I hope")
	return render_template('index.html', tweets=tweets)

if __name__=='__main__':
	app.run(debug = True)
