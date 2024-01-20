from app import db

from werkzeug.security import generate_password_hash, check_password_hash

managers = db.Table('managers',
    db.Column('manager_id', db.Integer, db.ForeignKey('wrestler.id')),
    db.Column('managed_id', db.Integer, db.ForeignKey('wrestler.id'))
)

class WrestlerModel(db.Model):

    __tablename__= "wrestlers"

    id = db.Column(db.Integer, primary_key = True)
    athlete = db.Column(db.String(50), nullable = False, unique = True)
    nickname = db.Column(db.String(75), nullable = False, unique = True)
    town_from = db.Column(db.String(150))
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(75), nullable = False, unique = True)
    password_hash = db.Column(db.String(250), nullable = False)
    managed = db.relationship('WrestlingModel',
                               secondary = "managers",
                               primaryjoin = managers.c.manager_id == id,
                               secondaryjoin = managers.c.managed_id == id,
                               backref = db.backref("managers", lazy = 'dynamic')
                                 )
    posts = db.relationship("StatModel", back_populates ="wrestler", lazy="dynamic", cascade="all, delete")


    def __repr__(self):
        return f'<Wrestler: {self.athlete}>'

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, user_dict):
        for k, v in user_dict.items():
            if k != "password":
                setattr(self, k, v)
            else:
                setattr(self, "password_hash", generate_password_hash(v))
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_managing(self, wrestler):
        return wrestler in self.managed
  
    def manage(self, wrestler):
        if self.is_managing(wrestler):
            return
        self.managed.append(wrestler)

    def fired(self,wrestler):
        if not self.is_following(wrestler):
            return
        self.managed.remove(wrestler)                



class StatModel(db.Model):

    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key = True)
    moves = db.Column(db.String, nullable = False)
    wrestler_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def __repr__(self):
        return f'<Post: {self.moves}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()