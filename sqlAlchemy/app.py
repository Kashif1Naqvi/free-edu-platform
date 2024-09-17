import random
from sqlalchemy.orm import sessionmaker
from models import engine, User


Session = sessionmaker(bind=engine)

session = Session()

names = ['Ali', 'Hassan', 'Syed Kashif Naqvi', 'Sara', 'Fatima', 'Zain', 'Imran', 'Baneen', 'Hamza', 'Bilal', 'Mariam', 'Kashif', 'Yasmin', 'Ibrahim']
ages = [12, 29, 10, 54, 78, 12, 21, 45, 34, 18, 60, 32, 25, 41, 23, 30, 27]

for item in range(20):
    user = User(name=random.choice(names), address=random.choice(ages))
    # session.add(user)
    # session.commit()

# Query Order By Age and Name
users = session.query(User).order_by(User.name, User.address)
for user in users:
    user_information = f"""
    Hey my name is {user.name}. I live in {user.address}.
    """
    print(user_information)
