from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db=SQLAlchemy()
# flask db init 로 데베 초기화
# flask db upgrade
migrate=Migrate()

def create_app(): # 애플리케이션 팩토리
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from views import main_views, question_views, answer_view
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_view.bp)

    return app

# app.py와 app/__init.py 동일한 app 모듈