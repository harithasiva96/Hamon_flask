from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Flask Cookie Example!'

@app.route('/set_cookie')
def set_cookie():
    response = make_response('Cookie is set')
    response.set_cookie('username', 'flask_user')
    return response

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    if username:
        return f'Hello {username}!'
    else:
        return 'No cookie found.'

if __name__ == '__main__':
    app.run(debug=True)
