from flask import render_template, jsonify, request,abort
from . import app
from . import views

@app.app.route('/task',methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id':views.tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    views.tasks.append(task)
    return  jsonify({'task':task}),201
        
    