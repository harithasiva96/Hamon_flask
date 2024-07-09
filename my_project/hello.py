
from flask import Flask
# initialising flask in to app
app = Flask(__name__)
# route is basically the end point.
@app.route("/home")
def hello_world():
    return "<p>Hello, World!</p>"

from markupsafe import escape

@app.route('/user/<username>')
def show_user(username):
    # show the user profile for that user
    return f'User {escape(username)}'



# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# from flask import request

# @app.route('/user/', methods=['GET', 'POST'])
# def show_user_profile():
#     if request.method == 'GET':
#         return "Listing all users"
#     elif request.method == 'POST':
#         return "Creating a new user"

# # @app.route('/user/<int: usser_id', methods=['GET', 'PATCH', 'DELETE'])  
# @app.route('/user/<int:post_id>', methods =['GET','PATCH','DELETE'])
# def show_post(post_id):
#     if request.method == 'GET':
#         return "Listing users"
#     elif request.method == 'PATCH':
#     # show the post with the given id, the id is an integer
#         return f'Post {post_id}'

