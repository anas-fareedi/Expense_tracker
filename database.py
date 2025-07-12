import streamlit as st 
from pymongo import MongoClient

MONGO_URI = st.secrets["MONGO_URI"]
client = MongoClient(MONGO_URI)

db = client["expense_tracker"]
collection = db["records"]

def insert_period(period, incomes, expenses, comment):
    """Insert or update a document for the given period"""
    document = {
        "_id": period,  
        "incomes": incomes,
        "expenses": expenses,
        "comment": comment,
    }
    collection.replace_one({"_id": period}, document, upsert=True)
    return document

def fetch_all_periods():
    """Return a list of all period IDs (e.g., '2025_July')"""
    return [doc["_id"] for doc in collection.find({}, {"_id": 1})]

def get_period(period):
    """Return the document for a specific period"""
    return collection.find_one({"_id": period})