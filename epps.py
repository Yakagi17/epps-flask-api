# import os
# import sys


# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(APP_ROOT)

# app = app


# @app.route('/')
# def index():
#     return 'welcome to EPPS API'


# if if __name__ == "__main__":
#     app.run(debug=True)
import os
from flask_migrate import Migrate
from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default'))
migrate = Migrate(app, db)

app.run(debug=True)