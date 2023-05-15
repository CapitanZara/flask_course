from flask import Flask, render_template

app = Flask(__name__)


@app.route('/blog/post1')
def blog_post1():
    post = {'id': 'post1', 'title': 'First Post', 'content': 'This is the first post.'}
    return render_template('blog_post.html', post=post)

@app.route('/blog/post2')
def blog_post2():
    post = {'id': 'post2', 'title': 'Second Post', 'content': 'This is the second post.'}
    return render_template('blog_post.html', post=post)

@app.route('/blog/post3')
def blog_post3():
    post = {'id': 'post3', 'title': 'Third Post', 'content': 'This is the third post.'}
    return render_template('blog_post.html', post=post)
