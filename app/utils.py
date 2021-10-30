from models import Users

def insert_user(name, email, password):
    user_ = Users(name=name, email=email, password=password)
    print(user_)
    user_.save()


def update_user(name, password):
    user_ = Users.query.filter_by(name=name).first()
    user_.password = password
    user_.save()


def query_users():
    user_ = Users.query.all()
    print(user_)

def query_user(name):
    user_ = Users.query.filter_by(name=name).first()
    print(user_.name, user_.email, user_.password)

def delete_user(name):
    user_ = Users.query.filter_by(name=name).first()
    user_ = Users.delete(user_.name, user_.email, user_.password)


if __name__ == '__main__':
    name = input('Insert the name of account: ')
    query_users()
    query_user(name)
    delete_user(name)
