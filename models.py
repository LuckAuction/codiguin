from datetime import datetime
class User(db.Model):
__tablename__ = 'users'


id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(80), unique=True, nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
password_hash = db.Column(db.String(128), nullable=False)
role = db.Column(db.String(20), default='user') # user/admin
created_at = db.Column(db.DateTime, default=datetime.utcnow)


bids = db.relationship('Bid', backref='bidder', lazy=True)
auctions = db.relationship('Auction', backref='seller', lazy=True)


def set_password(self, password):
self.password_hash = generate_password_hash(password)


def check_password(self, password):
return check_password_hash(self.password_hash, password)


class Game(db.Model):
__tablename__ = 'games'


id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(200), nullable=False)
platform = db.Column(db.String(50))
description = db.Column(db.Text)
image = db.Column(db.String(200))
created_at = db.Column(db.DateTime, default=datetime.utcnow)


auctions = db.relationship('Auction', backref='game', lazy=True)


class Auction(db.Model):
__tablename__ = 'auctions'


id = db.Column(db.Integer, primary_key=True)
game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
start_price = db.Column(db.Float, nullable=False)
current_price = db.Column(db.Float, nullable=False)
start_time = db.Column(db.DateTime, nullable=False)
end_time = db.Column(db.DateTime, nullable=False)
seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
status = db.Column(db.String(20), default='active') # active, closed, canceled
created_at = db.Column(db.DateTime, default=datetime.utcnow)


bids = db.relationship('Bid', backref='auction', lazy=True)


class Bid(db.Model):
__tablename__ = 'bids'


id = db.Column(db.Integer, primary_key=True)
auction_id = db.Column(db.Integer, db.ForeignKey('auctions.id'), nullable=False)
bidder_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
amount = db.Column(db.Float, nullable=False)
placed_at = db.Column(db.DateTime, default=datetime.utcnow)