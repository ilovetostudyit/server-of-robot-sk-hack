#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from git import Git, Repo
from flask import request, render_template
from flask import make_response, redirect

# Flask app should start in global layout
app = Flask(__name__)
speech = ""

@app.route('/<string:page_name>/')
def render_static(page_name):
	return render_template('%s.html' % page_name)
	 

@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)

	print("Request:")
	print(json.dumps(req, indent=4))

	res = processRequest(req)

	res = json.dumps(res, indent=4)
	# print(res)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	#f = open("templates\test.html","w+")
	#f.close()
	return r

def processRequest(req):
	global speech
	speech ="okay"
	print('Response:')
	try:
		f= open("templates/test.html","w+")
		f.write(speech)
		print(speech)
		f.close()
		if speech == "okay":
			os.remove("templates/test2.html")
			f.open("templates/test.html","w+")
			f.write(speech)
	except:
		print('Some error occured while pushing the code')   
	return  ({
			'speech': speech,
			"fulfillmentText": speech,
			'source' : 'InterestRate'
	})

if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))

	print ("Starting app on port %d" % port)
	f= open("templates/test2.html","w+")
 	f2= open("templates/test.html","w+")
	f.close()
 	f2.close()
	app.run(debug=False, port=port, host='0.0.0.0')
