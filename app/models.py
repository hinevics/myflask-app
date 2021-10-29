from app import db


class User(db.Document):
    name = db.StringField()
    text = db.StringField()
    
    
    def to_json(self):
        return {
            'name': self.name,
            'text': self.email
        }
