from flask import Flask, render_template, request, flash,session

app = Flask(__name__)
app.secret_key='gjfgjgj'
dict = {}
dict.update({'harithasiva007@gmail.com':'haritha', 'subinsreedhar94@gmail.com':'subin', 'yedusiva@gmail.com':'yedhu'})
@app.route('/',methods=['GET','POST'])
def login_form():
    return render_template("login_form.html")

@app.route('/home',methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email'] 
        password = request.form['password']
        for items in dict:
            # if email in dict.keys() and password in dict.values():
            if email in items and password in dict[items]:
               return render_template("home.html")
            else:
                flash("Invalid email or password")
    return render_template("login_form.html")   

if __name__ == '__main__':
    app.run(debug=True)
        
