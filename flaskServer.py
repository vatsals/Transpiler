from flask import Flask, jsonify, json
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index(): 
	return 'Works!'


@app.route('/access/<username>/<password>/<servername>/<hostname>', methods=['POST'])
def access(username, password, servername, hostname): 
	data = { "role": "admin", "username": username, "password": password }
	
	headers = {'Content-Type': 'application/json'}
	url = "https://www.teqschool.com/users/admin/login/"
	# url = "authentication_url"
	
	r = requests.post(url, headers=headers, json=data).json()
	tok = r['token']
	if(tok):
		newUrl = "https://www.teqschool.com/get/user/notifications?user_id=1&page=0&maxResults=10&user_name="
		# newUrl = "base_url" + servername + '/link/' + hostname
		headers = {'Content-Type': 'application/json', 'Token': tok}
		res = requests.get(newUrl, headers=headers).json()
		result = {}
		for key, value in res.items():
			result[key] = value
		print(result)

	return jsonify({"result": result})


if __name__ == '__main__':
	app.run(debug=True)

