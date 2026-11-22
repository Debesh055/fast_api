from fastapi import FastAPI,Request
from mockData import products
from dtos import ProductDto
app=FastAPI()

@app.get("/") #create the end point or route path like http://127.0.1:800/home
def home():
    return "welcome chudir vie in fat api"


@app.get("/products")#route path like http://127.0.1:800/products
def get_product():
    return products

#......................path params by id....

@app.get("/product/{id}")#route path like http://127.0.1:800/product/1 or 2...
def one_product(id:int):
    for i in products:
        if i .get("id")==id:
            return i
    return{
        "details":"product not found in this id"
    }
#................path params by item.........

@app.get("/product_i/{item_count}")#route path like http://127.0.1:800/product/10 or 12...
def one_product(item_count:int):
    for i in products:
        if i .get("count")==item_count:
            return i
    return{
        "product not found"
    }

#................quary params by item.........
@app.get("/user")
def user_details(request:Request):#like http://127.0.1:800/user?name=deb&age=22
    quary_param=dict(request.query_params)
    return{
        "user_details":f"your name {quary_param.get("name") }, your age {quary_param.get("age")} your college {quary_param.get("college")}"
    }

#......post method.......
@app.post("/create_product")
def creat_product(product_data:ProductDto):
    product_data=product_data.model_dump()
    products.append(product_data)
    print(product_data)
    return{
       "status": "new prouduct is created success fully....","data":products
    }

#......put method.......
@app.put("/update_details/{id}")
def update_product(product_data:ProductDto,id:int):
    for index,oneproduct in enumerate(products):
        if oneproduct.get("id")==id:
            products[index]=product_data.model_dump()
            return{
                    "details":"updated sucess fully","product":product_data
                }
    return{
        "details":"this id is not found"
    }

#......delete method.......
@app.delete("/deleted_product/{id}")
def deleted_product(id:int):
    for index,oneproduct in enumerate(products):
            if oneproduct.get("id")==id:
                product_deleted=products.pop(index)
                return{
                   "details":"deleted  sucess fully","product":product_deleted
                     }
    return{
            "details":"this is is not found"
        }