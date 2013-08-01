from functools import wraps
from werkzeug import SharedDataMiddleware
from flask import Flask, Response, request, make_response, render_template,redirect
import string
import plivo
import os.path
import os
from os.path import dirname, join as joinpath
import redis
import requests


app = Flask(__name__)

#redis = redis.Redis('localhost')

# This is for heroku redistogo addon #
redis_url = os.getenv('REDISTOGO_URL','redis://localhost:<port>')
redis = redis.from_url(redis_url)
#####################################

gl_autoreply = "Default reply"
gl_voice_recording = ""

auth_id = '<auth_id>'
auth_token = '<auth_token>'


cloud = plivo.RestAPI(auth_id = auth_id, auth_token = auth_token, url = 'https://api.plivo.com')


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'ryan' and password == 'password'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/',methods=['GET','POST'])
def get_home():
	response = make_response(render_template("welcome.html"))
	response.headers['Content-type'] = 'text/html'
	return response


@app.route('/acceptsms/', methods=['POST'])
def accept_and_reply():
	text = request.form.get('Text','')
	src = request.form.get('From','')
	plivo_did = request.form.get('To','')

	send_auto_response(src,plivo_did,text)

	email_SMS(text,src,plivo_did)

	response = make_response("OK")
	response.headers['Content-type'] = 'text/html'
	return response


def get_sms_response():
	sms_response = redis.get('auto_reply')
	return sms_response

@app.route('/set_sms_response/', methods=['POST'])
def set_sms_response():
	autoreply = request.form.get('autoreply','')

	print autoreply
	redis.set('auto_reply',autoreply)
	
	response = make_response(render_template("welcome.html", success_response = "SMS Auto Response saved!"))
	response.headers['Content-type'] = 'text/html'
	return response


@app.route('/set_email_config/', methods=['POST'])
def set_email_config():
	from_email = request.form.get('from_email','')
	mailgun_token = request.form.get('mailgun_token','')
	to_email = request.form.get('to_email','')	
	mail_subject = request.form.get('mail_subject','')
	domain = request.form.get('domain','')

	redis.set('from_email',from_email)
	redis.set('mailgun_token',mailgun_token)
	redis.set('to_email',to_email)
	redis.set('mail_subject',mail_subject)
	redis.set('domain',domain)

	response = make_response(render_template("welcome.html", email_success_response = "Email details saved!"))
	response.headers['Content-type'] = 'text/html'
	return response


def email_SMS(text, src, plivo_did):
	SECRET_KEY = redis.get('mailgun_token')
	from_email = "Ryan %s" % redis.get('from_email')
	to_email = redis.get('to_email')
	subject = redis.get('mail_subject')
	domain = redis.get('domain')

	body = "You have recieved an SMS from %s on your Plivo DID %s. SMS: %s" % (src, plivo_did, text)

	url = "https://api.mailgun.net/v2/%s/messages" % domain

	send_mail_response = requests.post(url, \
		auth=("api", SECRET_KEY), \
		data={"from": from_email, \
			  "to": to_email, \
			  "subject": subject, \
			  "text": body})
	return send_mail_response


def send_auto_response(src, plivo_did, text):
	sms_auto_response = get_sms_response()
	response = cloud.send_message({'src':plivo_did,'dst':src, 'text':sms_auto_response})
	print response



@app.route('/set_recording_voice/', methods=['POST'])
def set_voice_recording():
	play_url = request.form.get('play_url','')

	redis.set('play_url',play_url)

	response = make_response(render_template("welcome.html", playfile_success_response = "Play file details saved!"))
	response.headers['Content-type'] = 'text/html'
	return response

@app.route('/acceptcalls/', methods=['POST'])
def acceptcalls():
	response = plivo.Response()
	play_url = get_play_url()
	print play_url
	response.addPlay(body=play_url)
	response = make_response(response.to_xml())
	response.headers['Content-type'] = 'text/xml'
	return response

def get_play_url():
	return redis.get('play_url')

@app.route('/help/', methods=['POST'])
def help():
	response = make_response(render_template("help.html"))
	response.headers['Content-type'] = 'text/html'
	return response

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5555))
	app.run(host='0.0.0.0', port=port, debug=True)

