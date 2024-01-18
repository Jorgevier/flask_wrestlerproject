from app import db

class PostModel(db.Model):

    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key = True)
    moves = db.Column(db.String, nullable = False)
    wrestler_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def __repr__(self):
        return f'<Post: {self.moves}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()