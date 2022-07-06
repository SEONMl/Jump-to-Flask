from app import db

# db.session.add/delete -> commit | Model.query.all/filter/get

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # db.Integer && pk => 자동 생성
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 답변과 질문을 연결하기 위해 추가한 속성, 부모글 확인
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # 질문 모델 참조하기 위해 추가 | backref 역참조 : 질문에서 답변을 거꾸로 참조하는 것
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(150), unique=True, nullable=False)
    password=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)