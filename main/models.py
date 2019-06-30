from main import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(20), nullable = False)
    kind = db.Column(db.String(10), nullable = False)
    age = db.Column(db.Integer(), nullable = False)

    def __repr__(self):
        return '{} {}, age: {}'.format(self.kind, self.nickname, self.age)