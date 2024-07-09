import flask
from models import *
from models import Category, init_db, get_session
from flask import jsonify
from flask import request
from flask_cors import CORS,cross_origin
from sqlalchemy import desc



app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:password@localhost:5432/flaskdb"
CORS(app)
db.init_app(app)

@app.route("/")
def home():
    return "Hello, world"


@app.route("/category")
def list_category():
    categoryList = db.select(Category).order_by(Category.id.desc())
    category = db.session.execute(categoryList).scalars()
    result = []
    for item in category:
      details = {"id" : item.id,
         "name" : item.name
         }
      result.append(details)
    return jsonify(result)


@app.route('/addcategory', methods=['POST'])
def insertCatagory():
    input=request.get_json
    id=input.get('id')
    name=input.get('name')
    new_category=Category(id=id,name=name)
    db.session.add(new_category)
    db.session.commit()
    return flask.jsonify("Category inserted")


@app.route("/product")
def listProduct():
    productList = (
        db.session.query(
            Product.productId,
            Product.productname,
            Product.price,
            Product.offer,
            Product.category_id,
            Category.name.label("categoryName"),
            Image.image

        )
        .join(Category, Product.category_id == Category.id)
        .outerjoin(Image, Product.productId == Image.product_id).order_by(desc(Product.productId))
    )

    products = db.session.execute(productList).fetchall()

    ret = []
    for item in products:
        details = {
            "productid": item.productId,
            "productname": item.productname,
            "price": item.price,
            "offer": item.offer,
            "categoryId": item.category_id,
            "categoryName": item.categoryName,
            "image": item.image
        }
        ret.append(details)
    
    return jsonify(ret)


@app.route("/products",methods=['POST'])
@cross_origin()
def addProducts():
    input = request.get_json()
    
    if not input:
        return jsonify({"error": "Invalid input"}), 400
    
    productname = input.get('productName')
    price = input.get('price')
    offer = input.get('offer')
    category_name = input.get('categoryName')
    image_url=input.get('image')
    
    if not all([productname, price, category_name, image_url]):
        return jsonify({"error": "Missing required fields"}), 400
    category = db.session.query(Category).filter_by(name = category_name).first()   
    if category == None :
        category= Category(name=category_name)
        db.session.add(category)
        db.session.commit()  
        
    new_product=Product(productname=productname,price=price,offer=offer,category_id=category.id)
    db.session.add(new_product)
    db.session.commit()    
    new_image = Image(image=image_url,product_id=new_product.productId)
    db.session.add(new_image)
    db.session.commit()
    return jsonify({'message':"Product added successfully"})





with app.app_context():
    db.create_all()
if __name__ == '__main__':
    init_db()
    app.run(port=5000)







