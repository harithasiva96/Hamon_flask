from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/square', methods=['GET'])
def squarenumber():
    
    if request.method == 'GET':
   # If 'num' is None, the user has requested page the first time
        if(request.args.get('num') == None):
            return render_template('squarenum.html')
          # If user clicks on Submit button without 
          # entering number display error
        elif(request.args.get('num') == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
          # User has entered a number
          # Fetch the number from args attribute of 
          # request accessing its 'id' from HTML
            number = request.args.get('num')
            sq = int(number) * int(number)
            # pass the result to the answer HTML
            # page using Jinja2 template
            return render_template('answer.html', 
                                   squareofnum=sq, num=number)
        
if(__name__ == "__main__"):
    app.run(debug=True)
 