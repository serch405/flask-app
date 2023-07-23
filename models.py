from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(254), unique=True, nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    password = db.Column(db.String(254), nullable=False)
    first_name = db.Column(db.String(254))
    last_name = db.Column(db.String(254))
    country = db.Column(db.String(254))
    profile_image = db.Column(db.String(254))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"