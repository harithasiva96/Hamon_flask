from flask_sqlalchemy import SQLAlchemy
import logging
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker,DeclarativeBase, relationship
from typing import List
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)

class Category(db.Model):
    __tablename__ = "category"
    id    : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(50))

    products: Mapped[List["Product"]] = relationship()

  

class Product(db.Model):
    __tablename__ = "product"
    productId: Mapped[int] = mapped_column(primary_key=True)
    productname: Mapped[str] = mapped_column(String(50))  
    price: Mapped[int] = mapped_column(Integer)  
    offer: Mapped[str] = mapped_column(String(50))  
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    
    category: Mapped["Category"] = relationship("Category", back_populates="products")
    image: Mapped["Image"] = relationship(back_populates="product")



class Image(db.Model):
    __tablename__ = "image"
    imageId: Mapped[int] = mapped_column(primary_key=True)
    image: Mapped[str] = mapped_column(String(255))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.productId"))

    product: Mapped["Product"] = relationship("Product",back_populates="image")

    



# def __repr__(self):
#     return f"Category(id={self.id}, name={self.name})"

def init_db(db_uri='postgresql+psycopg2://postgres:password@localhost:5432/flaskdb'):
    logger = logging.getLogger("FlaskApp")
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    logger.info("Created database")

def get_session(db_uri):
    engine = create_engine(db_uri)
    Session = sessionmaker(bind = engine)
    session = Session()
    return session
    





