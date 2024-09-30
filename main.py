"""
    routes: 
        contains the routing rules
    Data: 
        contains code that interacts directly with the DB
        - DB connection string is contained in the `init_db.py` file
    Model: 
        contains the Data model structures
"""

from sys import prefix
from fastapi import FastAPI
from routes import dog, adoption, volunteer
import uvicorn
from pymongo import MongoClient
from dotenv import dotenv_values
from contextlib import asynccontextmanager
from pymongo.server_api import ServerApi



config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(config["ATLAS_URI"], tls=True, tlsCertificateKeyFile=config["TLS_CERT"], server_api=ServerApi('1'))
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")
    yield
    app.mongodb_client.close()


app = FastAPI(lifespan=lifespan)
app.include_router(dog.router, prefix="/api/v1/dog")
app.include_router(adoption.router, prefix="/api/v1/adoption")
app.include_router(volunteer.router, prefix="/api/v1/volunteer")




# file-name:fast-api-instance-name
if __name__=="__main__":
    uvicorn.run("main:app", reload=True)