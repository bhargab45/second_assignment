from flask import Flask
import pymongo
from pymongo import MongoClient

mongo = MongoClient('localhost',27017)  

db = mongo.Mydb
collection = db.person
name="name"

collection.insert_many(
   [  
   	 { name: "John",},
     { name: "Jeorge",},
     { name: "Steve", },
     { name: "David", }
   ]
)