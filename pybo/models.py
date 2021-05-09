from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, 
                            db.ForeignKey('question.id', ondelete='CASCADE')) # 모델 간 관계 정의
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan')) # 참조 모델 / 역참조
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)