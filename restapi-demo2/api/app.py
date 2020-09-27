from flask import Flask, render_template 

app = Flask(__name__,instance_relative_config=True)

from . import views, views_post

if __name__ == '__main__':
    print('Inside Main')
    app.run(debug=True)