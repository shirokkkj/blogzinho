from flask import Blueprint, render_template
from database.posts.posteds import POSTS

posts_route = Blueprint('posts', __name__)

@posts_route.route('/posts')
def posts():
    return render_template('posts.html', posts=POSTS)