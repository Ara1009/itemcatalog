import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()


user1 = User(name="Test User", email="test123@gmail.com")

category1 = Category(name="Soccer")
category2 = Category(name="Basketball")
category3 = Category(name="Baseball")
category4 = Category(name="Frisbee")
category5 = Category(name="Snowboarding")
category6 = Category(name="Rock Climbing")
category7 = Category(name="Foosball")
category8 = Category(name="Skating")
category9 = Category(name="Hockey")
category10 = Category(name="E-Sports")


db_session.add(category1)
db_session.add(category2)
db_session.add(category3)
db_session.add(category4)
db_session.add(category5)
db_session.add(category6)
db_session.add(category7)
db_session.add(category8)
db_session.add(category9)
db_session.commit()

item1 = Item(name="Soccer Ball",
             description="A ball used in the sport that is called football or "
             "soccer. It is Sperical and is composed of 32 black and white "
             "panels. The FIFA standard weight of a size 5 ball is between "
             "14 and 16 oz.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category1,
             user=user1)

item2 = Item(name="Yellow Card",
             description="A card awarded to a player as a warning penelty."
             "The player may continue to play the game. If he/she receives "
             "another warning, the player must leave the field immediately ",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category1,
             user=user1)

item3 = Item(name="Basketball Hoop",
             description="A goal that is used in the sport of basketball."
             "NBA and collegiate regulation states that it must be 10 feet "
             "in height and use a tempered glass backboard. ",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category2,
             user=user1)

item4 = Item(name="Red Card",
             description="A card that is used to signify a player's ejection "
             "from the game. A red card may also be given if the player has "
             "a previous infraction that resulted in a yellow card.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category1,
             user=user1)

item5 = Item(name="Basketball Shoe",
             description="A shoe used to play the game of basketball. These "
             "types of shoes often have increased support and stability to "
             "handle the explosiveness of the players. Basketball shoes are "
             "often wore for style purposes and are developed by many brands.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category2,
             user=user1)

item6 = Item(name="Chalk",
             description="Chalk is a substance often used in rock climbing "
             "to provide friction between hands and the rocks.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category6,
             user=user1)

item7 = Item(name="Frisbee Disc",
             description="A circular object that is thrown to players "
             "while playing frisbee.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category4,
             user=user1)

item8 = Item(name="Field Shorts",
             description="Very elastic shorts worn by frisbee players. "
             "The shorts allow for maximum range of movement and allow "
             "players to dynamically move their body in order to extend "
             "their reach.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category4,
             user=user1)

item9 = Item(name="Gatorade Bottle",
             description="A green bottle with a tip that squirts out water. "
             "It is massively adopted by frisbee players for its significant "
             "volume and its material. It is often thrown around and is able "
             "withstand harsh interaction.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category4,
             user=user1)

item10 = Item(name="Battlefield",
              description="Battlefield is a first-person shooter video game "
              "developed by video game developer EA DICE and published by "
              "Electronic Arts. It is available for Microsoft Windows, "
              "PlayStation 3, PlayStation 4, Xbox 360 and Xbox One.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item11 = Item(name="Leage of Legends",
              description="League of Legends is a game created by Riot Games "
              "and is regarded as the most popular game in the world. It is "
              "an MOBA that requires a team of 5 to come together to destroy "
              "enemy nexus. This game has a global playerbase and has a huge "
              "professional scene.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item12 = Item(name="Fortnite",
              description="Fortnite is a battle-royale game created by Epic "
              "Games. It is a third-person shooter and has been extremely "
              "popular over the last year. Gameplay videos are often created "
              "by content creators and streams can be found on twitch.tv and "
              "youtube.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item13 = Item(name="Hearthstone",
              description="Hearthstone is an online card game created to "
              "to showcase characters from the Blizzard universe. The goal "
              "of the game is to take your opponents lifepoints to 0 by "
              "attacking with monsters and magic.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item14 = Item(name="FIFA",
              description="FIFA is a sports video game in the FIFA "
              "series. This game uses the Frostbite game engine. "
              "On 21 July 2016, it was announced that, after a public vote, "
              "Marco Reus would feature on the cover of the game. The demo "
              "was released on 13 September 2016. The Play First Trial was "
              "released on 22 September 2016 in Microsoft Windows's "
              "Origin Access and Xbox One's EA Access.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item15 = Item(name="Hockey Stick",
              description="Hockey sticks are used in the game of hockey in "
              "order to shoot a puck into a goal. It is usually black and is "
              "is often used to check other players in acts of aggression.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category9,
              user=user1)

item16 = Item(name="Hockey Puck",
              description="A hockey puck is a black disck used to score goals "
              "in the sport of hockey. It is extremely hard and its circular "
              "size makes it very aerodynamic and allows it to fly through "
              "the air.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category9,
              user=user1)

item17 = Item(name="Need for Speed Rivals",
              description="Need for Speed Rivals is an open world racing "
              "video game. Developed by Ghost Games and Criterion Games, it "
              "is the twentieth installment in the Need for Speed series. "
              "The game was released for Microsoft Windows, PlayStation 3 and "
              "Xbox 360 on 19 November 2013, and for PlayStation 4 and "
              "Xbox One as launch titles in the same month.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item18 = Item(name="Baseball Bat",
              description="A wooden bat that is used in the sport of baseball "
              "to hit a ball as far as possible. The bat can crack while "
              "hitting a ball which creates a dangerous situation for fans "
              "sitting in the general area. ",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category3,
              user=user1)

item19 = Item(name="EA Sports UFC",
              description="EA Sports UFC 2 is a mixed martial arts fighting "
              "video game developed by EA Canada, and published in March 2016 "
              "by Electronic Arts for the PlayStation 4 and Xbox One. "
              "It is based on the Ultimate Fighting Championship (UFC) brand."
              "The game's cover features various UFC legends.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item20 = Item(name="Snowboard",
              description="A snowboard is used to speed down a hill laced "
              "with snow. The most famous snowboarder, Shawn White, is an "
              "Olympic gold medalist and is a huge advocate of the sport.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category5,
              user=user1)

item21 = Item(name="Rock Climbing shoes",
              description="Rock climbing shoes are extremely sturdy and "
              "provide as much friction as possible so that users may be able "
              "to stabilize his/her feet. However some athletes choose to not "
              "wear shoes at all in order to be able to have more movement.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category6,
              user=user1)

item22 = Item(name="Counter-Strike: Global Offensive",
              description="Counter-Strike: Global Offensive (abbreviated as "
              "CS:GO) is a multiplayer first-person shooter video game "
              "developed by Hidden Path Entertainment and Valve Corporation. "
              "It is the fourth game in the main Counter-Strike franchise. "
              "Counter-Strike: Global Offensive was released for Microsoft "
              "Windows, OS X, Xbox 360, and PlayStation 3 in August 2012, "
              "with the Linux version being released in September 2014",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item23 = Item(name="Overwatch",
              description="Overwatch is a team-based multiplayer first-"
              "person shooter video game developed and published by Blizzard "
              "Entertainment. It was released in May 2016 for Microsoft "
              "Windows, PlayStation 4, and Xbox One.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

db_session.add(item1)
db_session.add(item2)
db_session.add(item3)
db_session.add(item4)
db_session.add(item5)
db_session.add(item6)
db_session.add(item7)
db_session.add(item8)
db_session.add(item9)
db_session.add(item10)
db_session.add(item11)
db_session.add(item12)
db_session.add(item13)
db_session.add(item14)
db_session.add(item15)
db_session.add(item16)
db_session.add(item17)
db_session.add(item18)
db_session.add(item19)
db_session.add(item20)
db_session.add(item21)
db_session.add(item22)
db_session.add(item23)
db_session.commit()

print "added catalog items!"
