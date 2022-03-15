from app import db

class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(60))
    users = db.relationship('User', backref='role')

    def __repr__(self) -> str:
        return f'USer {self.role}'


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullabe=False)
    password = db.Column(db.String(120))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    likes = db.relationship('Like', backref='user', passive_deletes=True)

    def __repr__(self) -> str:
        return f'USer {self.username}'


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(200))
    post_body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    likes = db.relationship('Like', backref='post', passive_deletes=True)

    def __repr__(self) -> str:
        return f'USer {self.post_title}'


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id', ondelete='CASCADE'), nullable=False)


class Like(db.Model):

    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    liked_by = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    liked_post = db.Column(db.Integer, db.ForeignKey(
        'post.id', ondelete='CASCADE'), nullable=False)
