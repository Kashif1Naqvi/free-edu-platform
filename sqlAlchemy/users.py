from sqlalchemy.orm import sessionmaker
from models import engine, User


Session = sessionmaker(bind=engine)

session = Session()

""" For Adding Users """
# user_one = User(name="kashif", address="Lahore, Pakistan")
# user_two = User(name="Ali", address="Lahore, Pakistan")
# user_three = User(name="Hassan", address="Lahore, Pakistan")

""" When You have save multiple records at once """
# session.add_all([user_one, user_two, user_three])
# session.commit()

""" User listing """
users = session.query(User).all()

for user in users:
    user_information = f"""
    Hey my name is {user.name}. I live in {user.address}. My unique ID is {user.id}
    """
    #print(user_information)

""" Specific User listing """
user = session.query(User).filter_by(name="kashif").first()

""" Update User """

user = session.query(User).filter_by(id=1).update(values= {"name": "Syed Kashif Naqvi"})
session.commit()

""" Delete User """

user = session.query(User).filter_by(id=4).delete()
session.commit()

