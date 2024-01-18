from app import db

# from werkzeug.security import generate_password_hash, check_password_hash
# not needed
class WrestlerModel(db.Model):

    __tablename__= "wrestlers"

    id = db.Column(db.Integer, primary_key = True)
    athlete = db.Column(db.String(50), nullable = False, unique = True)
    nickname = db.Column(db.String(75), nullable = False, unique = True)
    town_from = db.Column(db.String(150))

    def __repr__(self):
        return f'<Wrestler: {self.athlete}>'

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()