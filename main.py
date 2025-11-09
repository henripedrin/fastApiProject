from fastapi import FastAPI
from api.routes import company_routes, stock_routes, product_routes, supplier_routes, type_routes

app = FastAPI()
app.include_router(company_routes.router)
app.include_router(stock_routes.router)
app.include_router(product_routes.router)
app.include_router(supplier_routes.router)
app.include_router(type_routes.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("product/{product_id}")
async def read_product():
    return

@app.get("stock/{stock_id}")
async def read_product():
    return

@app.get("supplier/{supplier_id}")
async def read_product():
    return
