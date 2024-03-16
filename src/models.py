from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(240), nullable=True)
    done = db.Column(db.Boolean, default=False)
    todo_list_id = db.Column(db.Integer, db.ForeignKey("todo_list.id"))

    def __init__(self, label):
        self.label = label



class TodoList(db.Model): # PascalCase -> snake_case = todo_list
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    full_name = db.Column(db.String(240), nullable=False)

    def __init__(self, username, full_name): 
        self.username = username        
        self.full_name = full_name
        db.session.add(self)
        try:  
            db.session.commit()
        except Exception as error:  
            db.session.rollback()
            print(error)

    def transform_into_dictionary(self):
        """ return a dictionary that 
        represents an user."""
        return {
            "id": self.id, 
            "username": self.username,
            "full_name": self.full_name
        }