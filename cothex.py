from flask import Flask, render_template, request
from scripts import twitterapi
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def crashThatTwitter():
	greeting = {'I Hope' : 'What\'s twitter hoping for?',
	'I Wish' : 'What\'s twitter wishing for?',
	'I Dream' : 'What\'s twitter dreaming about?',
	'I Want' : 'What does twitter want now?',
	'I Think' : 'What\'s twitter thinking about?',}			#Dictionary for the header message.
	if request.method == 'POST':
		getTweets = twitterapi.searchTweets(request.form['tQuery'])
		return render_template('index.html', tweets=getTweets, message=greeting[request.form['tQuery']])
	else:
		getTweets = twitterapi.searchTweets("I hope")
		return render_template('index.html', tweets=getTweets, message=greeting['I Hope'])


@app.route('/logge', methods=['GET', 'POST']) 	#Just for testing reasons
def parse_request():
	if request.method == 'POST':
		print request.form['tQuery']
		return render_template('response.html', valuee = request.form['tQuery'])
	else:
		return render_template('response.html')


if __name__=='__main__':
	app.run()
