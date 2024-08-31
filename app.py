from flask import Flask ,render_template, request, redirect, url_for, flash
import sqlite3
from flask_sqlalchemy import SQLAlchemy

#Data base SQLITE CONFIG
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'key'
db = SQLAlchemy(app)

# Data tabble or model creation
class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)

with app.app_context():
    db.create_all()


# Add data into database
@app.route('/', methods=['GET','POST'])
@app.route('/<int:todo_id>', methods = ['GET','POST'])
def index(todo_id=None):
    if request.method == 'POST':
        title = request.form.get('title')
        if todo_id is None:
         todo = Todo(id=id)
         todo = Todo(title=title)
         db.session.add(todo)
         db.session.commit()

         flash('Todo Item Added Successfully','success')
      
# updating data in database 
        else:
            todo = Todo.query.get(todo_id)
            if todo:
               
                todo.title = title
                db.session.commit()
     
            flash('Todo Item updated Successfully','success')
    

        return redirect(url_for('index'))       
             
    

    todo = None   

    if todo_id is not None:
        todo = Todo.query.get(todo_id)   
    todos = Todo.query.order_by(Todo.id.desc()).all()   


    return render_template ('index.html',todos= todos,todo=todo)



# Delete data from database

@app.route('/delete/<int:todo_id>', methods=["POST"])
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        flash('Todo Item deleted Successfully','success')

    return redirect(url_for('index'))




  


if __name__=='__main__':
    app.run(debug=True)

