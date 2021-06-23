from flask import Flask, make_response, jsonify
import uuid

EXCHANGE = {
	"USD": 75,
	"EUR": 80,
	"AUD": 55,
	"CAD": 60
}
app = Flask(__name__)

@app.route('/')
def index():
	return make_response(jsonify({"health": "pass"}), 200)
	
@app.route('/exchange/<country>/to/INR')
def home(country):
	if country in EXCHANGE.keys():
		res = make_response(jsonify({
			"id": uuid.uuid1(),
			"fromCountry": country,
			"toCountry": "INR",
			"rate" : EXCHANGE[country]
			}), 200)
	else:
		res = make_response(jsonify({"error": "exhange country not found" }), 400)

	return res	

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000)
