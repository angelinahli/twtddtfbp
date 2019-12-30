from twtddtfbp.app import db

class Tweet(db.Model):

    __tablename__ = 'tweets'

    id = db.Column(db.Integer, primary_key=True)
    tweet_id = db.Column(db.String, unique=True)
    date = db.Column(db.DateTime, index=True)
    retweets = db.Column(db.Integer, index=True)
    likes = db.Column(db.Integer, index=True)
