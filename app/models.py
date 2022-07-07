from app import db

# db.session.add/delete -> commit | Model.query.all/filter/get

# N:N
question_voter= db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id',ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # db.Integer && pk => 자동 생성
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date=db.Column(db.DateTime(), nullable=True)
    voter=db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))


answer_voter=db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 답변과 질문을 연결하기 위해 추가한 속성, 부모글 확인
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # 질문 모델 참조하기 위해 추가 | backref 역참조 : 질문에서 답변을 거꾸로 참조하는 것
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user=db.relationship('User', backref=db.backref('answer_set'))
    modify_date=db.Column(db.DateTime(), nullable=True)
    voter=db.relationship('User',secondary=answer_voter, backref=db.backref('answer_voter_set'))


class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(150), unique=True, nullable=False)
    password=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)


