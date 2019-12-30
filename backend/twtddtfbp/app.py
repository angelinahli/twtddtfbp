import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from twtddtfbp.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)

if app.config['ENVIRONMENT'] == 'development':
    cors = CORS(app, resources={r"*": {"origins": "*"}})
else:
    cors = CORS(app, resources={r"*": {"origins": "http://todaywasthedaydonaldtrumpfinallybecamepresident.com"}})


db = SQLAlchemy(app)
migrate = Migrate(app, db)

ma = Marshmallow(app)

from twtddtfbp import queries, process_data

@app.route('/', methods=['GET'])
def index():
    data = {
        "top_by_likes": queries.top_by_likes(),
        "top_by_retweets": queries.top_by_retweets(),
        "all": queries.all_sorted_by_date()
    }
    return jsonify(data)

scheduler = BackgroundScheduler()
scheduler.add_job(func=process_data.process_all_tweets, trigger="interval", seconds=3600)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())
