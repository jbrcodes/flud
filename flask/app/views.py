# docker1/app/views.py

from flask import flash, redirect, render_template, request, url_for

from app import app, db, jinja
from app.models import Post



@app.route('/')
def home():
    postQuery = Post.GetAll()
    vars = {
        'title': 'Latest Posts',
        'postQuery': postQuery
    }
    
    return render_template('index.html', vars=vars);


@app.route('/hello/<name>/')
def hello(name):
    vars = {
        'title': 'Hello {}'.format(name),
        'body': 'Well... hello {}! How are you?!?'.format(name)
    }
    
    return render_template('page.html', vars=vars);


@app.route('/posts/<id>/delete/')
def deletePost(id):
    blah = Post.Delete(id)  # ignore response
    
    return redirect( url_for('home') )


@app.route('/posts/add/')
def addPost():
    vars = { 'title': 'Add Post' }
    
    return render_template('form.html', vars=vars);


@app.route('/posts/<id>/edit/')
def editPost(id):
    vars = { 
        'title': 'Edit Post', 
        'post': Post.Get(id) 
    }
    
    return render_template('form.html', vars=vars);


@app.route('/posts/save/', methods=['POST'])
def savePost():
    formData = request.form
    if 'id' in formData:
        post = Post.Get( formData['id'] )
        post.update( formData )
    else:
        Post.Insert( formData )

    return redirect( url_for('home') )
