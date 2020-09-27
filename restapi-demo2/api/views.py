from flask import render_template,jsonify,make_response,abort
from . import app

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.app.route('/',methods = ['GET'])
def index():
    print("Inside Index")
    return render_template("index.html")

@app.app.route('/tasks',methods = ['GET'])
def tasks1():
    return jsonify({'tasks':tasks})

@app.app.route('/tasks/<int:task_id>',methods=['GET'])    
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify({'task':task})
    print("Not Found")
    abort(404)

@app.app.errorhandler(404)
def not_found(error):
    print("Inside Not ffound ",error)
    return make_response(jsonify({'error':'Not Found !!!'}),404)