import random
from sqlalchemy import or_, and_, func
from sqlalchemy.orm import sessionmaker
from models import engine, User


Session = sessionmaker(bind=engine)

session = Session()

names = ['Ali', 'Hassan', 'Syed Kashif Naqvi', 'Sara', 'Fatima', 'Zain', 'Imran', 'Baneen', 'Hamza', 'Bilal', 'Mariam', 'Kashif', 'Yasmin', 'Ibrahim']
ages = [12, 29, 10, 54, 78, 12, 21, 45, 34, 18, 60, 32, 25, 41, 23, 30, 27]
address = ['Lahore, Pakistan', 'Karachi']
for item in range(20):
    user = User(name=random.choice(names), address=random.choice(address), age=random.choice(ages))
    # session.add(user)
    # session.commit()

# Query Order By Age and Name
users = session.query(User).order_by(User.name, User.address)
for user in users:
    user_information = f"""
    Hey my name is {user.name}. I live in {user.address}.
    """
    # print(user_information)



# Data filters or and where
users = session.query(User).where(or_(User.address == 'Karachi', User.age >= 30)).all()
for user in users:
    user_information = f"""
    Hey my name is {user.name}. I live in {user.address} My age is {user.age}.
    """
    # print(user_information)

# Data filters and ,or, and, filter
users = session.query(User).filter(
    or_(
        and_(User.age > 20),
        or_(User.address == 'Karachi')
    )
).all()
for user in users:
    user_information = f"""
    Hey my name is {user.name}. I live in {user.address} My age is {user.age}.
    """
    # print(user_information)

users = session.query(User.address, func.count(User.id))
users = users.filter(or_(User.address == 'Karachi', User.address=='Lahore, Pakistan')).order_by('address').group_by('address')


for address, count in users:
    user_information = f"""
        In this database {count} users Live in {address}
    """
    print(user_information)
