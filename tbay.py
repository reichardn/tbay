from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    ### Table for items ###
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    bids = relationship("Bid", backref="item")

class User(Base):
    ### Table of all users ###
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    items = relationship("Item", backref="user")
    bids = relationship("Bid", backref="user")

class Bid(Base):
    ### Table of all users ###
    __tablename__ = "bid"
    
    id = Column(Integer, primary_key=True)
    bid = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)

Base.metadata.create_all(engine)