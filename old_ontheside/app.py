import os
from flask import Flask,request, render_template

app = Flask(__name__)

clientid = "fovc0rXg7VytztmT1H8s9ijij4n1CygF"
clientsec = "GQkZfyTloydHizkSfNEFFTkaddv4d4drdtS1Sb71I8ghtJYD0_03TRXdyaKpors3"
authcode = -1

@app.route('/whereiszhuoshi',methods=['GET','POST'])
def zhuoshi():
	if authcode == -1:
		return """
			<html><head><meta http-equiv="Refresh" content="0;
			url="https://api.moves-app.com/oauth/v1/authorize?response_type=code&client_id={}&scope=<scope>"></head></html>
		       """.format(clientid)


@app.route('/whereiszhuoshi_auth',methods=['GET','POST'])
def zhuoshi_auth():
	params = request.args
	return 'meh'

@app.route('/')
def hello():
	return render_template('hello.html')

@app.route('/dino')
def dinosaur():
	return render_template('dino.html')

@app.route('/uist')
def uist():
	return render_template('uist.html')

@app.route('/aug14')
def uist():
	return render_template('aug14.html')


@app.route('/links')
def links():
	return render_template('links.html')

#@app.route('/css/<path:fnc>')
def css_static(fn):
	return send_from_directory('/css/',fnc)

#@app.route('/static/<path:fns>')
def static(fn):
	return send_from_directory('/static/',fns)

#@app.route('/js/<path:fnj>')
def js_static(fn):
	return send_from_directory(app.config['JS_STATIC'],fnj)


@app.route('/temp/<name>')
def temp(name=None):
	return render_template('display.html',name=name)

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000
	port = int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0',port=port,debug=True)
