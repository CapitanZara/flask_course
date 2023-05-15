from flask import Flask, render_template, abort

blog_posts = [
    {'id': 'post1', 'title': 'First Post', 'content': 'This is the first post.'},
    {'id': 'post2', 'title': 'Second Post', 'content': 'This is the second post.'},
    {'id': 'post3', 'title': 'Third Post', 'content': 'This is the third post.'},
    # More blog posts...
]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', posts=blog_posts)


@app.route('/blog/<post_id>')
def blog_post(post_id):
    # Find the blog post with the given ID
    for post in blog_posts:
        if post['id'] == post_id:
            return render_template('blog_post.html', post=post)

    # If we didn't find the blog post, return a 404 error
    abort(404)


app.run()
