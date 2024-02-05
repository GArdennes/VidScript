#!/usr/bin/env python
"""
Script for API Gateway Service
"""
import os, gridfs, pika, json
from flask import Flask, request, send_file
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    """
    """
    pass

@app.route("/upload", methods=["POST"])
def upload():
    """
    """
    pass

@app.route("/download", methods=["POST"])
def download():
    """
    """
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)