from flask import Flask

app = Flask(__name__)

@app.route('/')
def logfile():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return "Log is done successfully"

if __name__ == '__main__':   
    app.run(debug=True)
