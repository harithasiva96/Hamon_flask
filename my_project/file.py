
from flask import Flask, render_template, request, flash,redirect, url_for
app = Flask(__name__)   
  
# @app.route('/', methods=['GET','POST'])   
# def main(): 
#     if request.method == 'POST':   
#         f = request.files['file'] 
#         f.save('/home/user/my_project/upload_files/fileupload')  
#         return render_template("fileupload_2.html")
#     return render_template("fileupload_1.html")   

@app.route('/<int:number1>/<int:number2>')
def num(number1,number2):
    return f'{number1} + {number2} = {number1 + number2}'

  
# @app.route('/home', methods = ['GET','POST'])   
# def fileupload():   
#     if request.method == 'POST':   
#         f = request.files['file'] 
#         f.save('/home/user/my_project/upload_files/fileupload')  
#         return render_template("fileupload_2.html")   
  
if __name__ == '__main__':   
    app.run(debug=True)
