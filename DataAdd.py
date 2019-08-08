from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///catalogproject.db')
Base.metadata.bind = engine

# Create database session
DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(
    name='Tristan',
    email='Tristannutman@gmail.com'
)

session.add(user1)
session.commit()

category1 = Category(name='Skateboarding', user_id=1)

session.add(category1)
session.commit()

item1 = Item(
    name='Skateboard',
    description='It is use for entertainment, enjoy the speed!',
    category=category1,
    user_id=1
)

session.add(item1)
session.commit()

print('Finished populating the database!')
