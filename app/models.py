from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager

engine = create_engine('sqlite:///auth_login.db')
db_session = scoped_session(sessionmaker(autocommit = False, bind = engine ))
Base = declarative_base()
Base.query = db_session.query_property()


@login_manager.user_loader
def get_user(user_id):
    return Users.query.filter_by(id=user_id).first()

class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    password = Column(String(80), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f'<Users {self.name}>'

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()