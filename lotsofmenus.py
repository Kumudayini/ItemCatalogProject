from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item, User
import datetime

engine = create_engine('sqlite:///catalogappdb.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Categories if exisitng.
session.query(Category).delete()
# Delete Items if exisitng.
session.query(Item).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create a user
User1 = User(
    name="Kumudayini Krishnappa",
    email="kumudayini@gmail.com",
    picture='/static/blank_user.gif')
session.add(User1)
session.commit()

# Create Categories
Category1 = Category(name='Soccer', user=User1)
session.add(Category1)
session.commit()

Category2 = Category(name='Basketball', user=User1)
session.add(Category2)
session.commit()

Category3 = Category(name='Baseball', user=User1)
session.add(Category3)
session.commit()

Category4 = Category(name='Frisbee', user=User1)
session.add(Category4)
session.commit()

Category5 = Category(name='Snowboarding', user=User1)
session.add(Category5)
session.commit()

Category6 = Category(name='Rock Climbing', user=User1)
session.add(Category6)
session.commit()

Category7 = Category(name='Football', user=User1)
session.add(Category7)
session.commit()

Category8 = Category(name='Skating', user=User1)
session.add(Category8)
session.commit()

Category9 = Category(name='Hockey', user=User1)
session.add(Category9)
session.commit()

print("added categories!")

# Create Items belonging to Category1 - Soccer
Item1 = Item(
    cat_id=Category1.id,
    description="The shoes",
    title="Soccer Cleats",
    user_id=1,
    date=datetime.datetime.now(),
    category=Category1,
    user=User1)
session.add(Item1)
session.commit()

Item2 = Item(
    cat_id=Category1.id,
    description="The shirt",
    title="Jersey",
    user_id=1,
    date=datetime.datetime.now(),
    category=Category1,
    user=User1)
session.add(Item2)
session.commit()

# Create Items belonging to Category2 - Basketball
Item3 = Item(
    cat_id=Category2.id,
    description="Goaliath 54 Warrior In-Ground Basketball Hoop with Pole Pad",
    title="Basket ball hoops",
    user_id=1,
    date=datetime.datetime.now(),
    category=Category2,
    user=User1)
session.add(Item3)
session.commit()

Item4 = Item(
    cat_id=Category2.id,
    description="This outdoor basketball is engineered from tough composite leather with a cross-hatched pebbled pattern to maximize grip while repelling buildup of dust and dirt on any outdoor court. Wide, deep channels provide shooter-friendly ball control, while the strong butyl bladder holds its shape and structure over time.",
    title="Nike True Grip Youth Basketball",
    user_id=1, date=datetime.datetime.now(),
    category=Category2,
    user=User1)
session.add(Item4)
session.commit()

# Create Items belonging to Category3 - Baseball
Item5 = Item(
    cat_id=Category3.id,
    description="Digital embossed synthetic overlays with perforations add support in all the right places Elastic wrist cuffs provide support & a locked-in, powerful feel Perforations over the fingers add increased breathability",
    title="Under Armour Youth Clean Up Batting Gloves",
    user_id=1,
    date=datetime.datetime.now(),
    category=Category3,
    user=User1)
session.add(Item5)
session.commit()

Item6 = Item(
    cat_id=Category3.id,
    description="The Under Armour Leadoff baseball cleat has a full-length EVA midsole that offers maximum padding to help disperse cleat pressure evenly throughout the foot.",
    title="Under Armour Kids Leadoff RM Baseball Cleats",
    user_id=1,
    date=datetime.datetime.now(),
    category=Category3,
    user=User1)
session.add(Item6)
session.commit()

print("added items!")
