from flask import Flask, jsonify, request, render_template, url_for, redirect, Response
from flask_pymongo import PyMongo
from bson.json_util import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'todo_db'
app.config['MONGO_URI']='mongodb://todouser123:todouser123@ds123562.mlab.com:23562/todo_db'

mongo = PyMongo(app)

@app.route('/', methods=["GET"])
def get_all_tasks():
    alltasks = mongo.db.tasks
    
    incomplete_output = []         
    for task in alltasks.find({'status':'false'}):    
        incomplete_output.append({'id':task['_id'], 
                        'title':task['title'], 
                        'description':task['description'], 
                        'status':task['status']})
    complete_output = []         
    for task in alltasks.find({'status':'true'}):    
        complete_output.append({'id':task['_id'], 
                        'title':task['title'], 
                        'description':task['description'], 
                        'status':task['status']})

    return  render_template('index.html', incomplete_tasks=incomplete_output, complete_tasks=complete_output)
    #return redirect(url_for(get_all_tasks), jsonify({'result':output})               

@app.route('/tasklist/<_id>', methods=["GET"])
def get_one_task(_id):
    alltasks = mongo.db.tasks
    output = []         
    task = alltasks.find_one({'id':_id})
    if task:
        output.append({'id':task['id'], 
                        'title':task['title'], 
                        'description':task['description'], 
                        'done':task['done']})
    else:
        output ='No results found'              
    return jsonify({'result':output})               

@app.route('/addtask', methods=["POST"])
def add_task():
    alltasks = mongo.db.tasks
    
    data = {
        'title' : request.form['taskTitle'],
        'description' : request.form['taskDescription'],
        'status' : 'false'
        }

    alltasks.insert(data)
    #alltasks.insert({'title':title,
     #               'description':description,
      #              'status':status})
    return redirect(url_for('get_all_tasks'))

 #   new_task = alltasks.find_one({'id':task_id})
 #   output = {'id':new_task['id'],
 #               'title':new_task['title'], 
 #               'description':new_task['description'], 
 #               'done':new_task['done']}               
  #  return jsonify({'result':output})   

@app.route('/deletetask/<_id>')
def delete_task(_id):
    alltasks = mongo.db.tasks     
    alltasks.delete_one({'_id':ObjectId(_id)})
    return redirect(url_for('get_all_tasks'))

@app.route('/completetask/<_id>')
def complete_task(_id):
    alltasks = mongo.db.tasks     
    alltasks.update_one({'_id': ObjectId(_id)}, {'$set' : {'status':'true'}}) 
    return redirect(url_for('get_all_tasks'))

@app.route('/incompletetask/<_id>')
def incomplete_task(_id):
    alltasks = mongo.db.tasks     
    alltasks.update_one({'_id': ObjectId(_id)}, {'$set' : {'status':'false'}}) 
    return redirect(url_for('get_all_tasks'))    

if __name__ == '__main__':
    app.run(debug=True)    