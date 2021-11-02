from sqlalchemy.sql.expression import false, true
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class UserGroups(Base):
    __tablename__ = "userGroups"
    user_group_id = Column(Integer, primary_key=True, autoincrement= True)
    user_group_name = Column(String(50), nullable=False)
    
    def __str__(self):
        return self.user_group_name

class Users(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement= True)
    user_name = Column(String(50), nullable= False)
    password = Column(String(50), nullable= False)
    user_group_id = Column(Integer, ForeignKey(UserGroups.user_group_id), nullable= False )

    def __str__(self):
        return self.user_name


class HotelGroup(Base):
    __tablename__ = "hotelGroup"
    hotel_group_id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_group_name = Column(String(50), nullable=False)
    description = Column(Text, nullable= True)
    image = Column(String(255), nullable= True)

    def __str__(self):
        return self.hotel_group_name

class HotelRoom(Base):
    __tablename__ = "hotelRoom"
    hotel_room_id = Column(Integer, primary_key=True, autoincrement=True)
    kind_of_room = Column(String(50),nullable= False)
    price = Column(Float, default=0)
    status = Column(String(50), default= True)
    holine_room = Column(Integer, default= False)
    hotel_group_id = Column(Integer, ForeignKey(HotelGroup.hotel_group_id), nullable= False)

    def __str__(self):
        return self.hotel_room_id

class Customer(Base):
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True, autoincrement= True)
    customer_name = Column(String(50), nullable= False)
    phone = Column(Integer, nullable= True)
    id_number = Column(Integer, nullable= False)

    def __str__(self):
        return self.customer_name

class Services(Base):
    __tablename__ = "services"
    service_id = Column(Integer, primary_key=True, autoincrement=True)
    service_name = Column(String(50), nullable= False)
    service_price = Column(Float, default=0)

    def __str__(self):
        return self.service_name

# class BookRoom(db):
#     __tablename__ = "bookRoom"
#     customer_id = Column(Integer, ForeignKey(Customer.customer_id), nullable= False )
#     hotel_room_id = Column(Integer, ForeignKey(HotelRoom.hotel_room_id), nullable= False )
#     arrival_date = Column(Date)

# if __name__ == "__main__":
#     db.create_all()