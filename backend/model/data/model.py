from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base
from fastapi_users.db import SQLAlchemyBaseUserTable



class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    review = relationship("Review", back_populates="user")


# class Address(Base):
#     __tablename__ = 'address'
#     id = Column(Integer, primary_key=True)
#     address_line = Column(String(150), nullable=False)
#     postal_code = Column(String(50), nullable=False)

#     user_address = relationship("UserAddress", back_populates="address")



# class UserAddress(Base):
#     __tablename__ = 'user_address'
#     user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
#     address_id = Column(Integer, ForeignKey('address.id'), primary_key=True)

#     user = relationship("User", back_populates="user_address")
#     address = relationship("Address", back_populates="user_address")