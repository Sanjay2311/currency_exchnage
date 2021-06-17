from flask import Flask, make_response, jsonify
import requests as rq
import json
import os

app = Flask(__name__)
	
@app.route('/conversion/<country>/to/INR/<count>', methods=['GET'])
def home(country, count):
	url = "{0}:3000/exchange/{1}/to/INR".format(os.environ.get('CURRENCY_EXCHANGE_SERVICE_HOST'), country)
	try:
		conversion_rate = rq.get(url).text
		data = json.loads(conversion_rate)
		res = make_response(jsonify({
			"id": data['id'],
			"fromCountry": country,
			"toCountry": "INR",
			"current rate": data['rate'],
			"value": data['rate'] * int(count)}), 200)
		return res
	except rq.exceptions.HTTPError as e:
		print('Error {0}'.format(e))
		raise e
		