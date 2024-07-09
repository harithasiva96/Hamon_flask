from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template("home.html")



@app.route('/reg',methods=['GET','POST'])
def register():
    if request.method == "POST":      
        email = request.form['email']
        password = request.form['password']

        response = make_response(render_template('reg.html'))
        # Set cookies with user data
        response.set_cookie('email', email)
        response.set_cookie('password', password)
        return response
        
    return render_template("reg.html")


@app.route('/login')
def login():
    return render_template('login_form.html')


@app.post('/login_handle')
def login_handle():
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']

        email_in_cookies = request.cookies.get('email')
        pswd_in_cookie = request.cookies.get('password')
        if email == email_in_cookies and password == pswd_in_cookie:
            return(f"Welcome {email}")




if __name__ == '__main__':   
    app.run(debug=True)