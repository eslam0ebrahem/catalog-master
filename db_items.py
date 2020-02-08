from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User, Category, Item, Base
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
User1 = User(name="islam ibrahim", email="Islam4544@gmail.com")
session.add(User1)
session.commit()
category1 = Category(name="Wall Tiles", user_id="1")
session.add(category1)
session.commit()
menuItem1 = Item(name="Johnson NEO Collection",
                     description="Digital Wall Tiles(30x60cm) with recommended Floor Tiles",
                     category_id=1, user_id=1)
session.add(menuItem1)
session.commit()
menuItem2 = Item(name="Johnson Ornato",
                     description="Ceramic 3D Wall Tiles Concepts",
                     category_id=1, user_id=1)
session.add(menuItem2)
session.commit()
menuItem3 = Item(name="Johnson Natura",
                     description="Elevation Wall Tile Collection",
                     category_id=1, user_id=1)
session.add(menuItem3)
session.commit()
category2 = Category(name="Floor Tiles", user_id="1")

session.add(category2)
session.commit()
menuItem1 = Item(name="Johnson Ceramic Stain & Scratch Resistant (SSR)",
                     description="Northen Collection - Rajkot (Available in rest of India)",
                     category_id=2, user_id=1)
session.add(menuItem1)
session.commit()
menuItem2 = Item(name="Johnson Ceramic Stain & Scratch Resistant (SSR)",
                     description="Southern Collection - Vijaywada (Available in South India only)",
                     category_id=2, user_id=1)

session.add(menuItem2)
session.commit()
print "Added items!"
