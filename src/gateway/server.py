#!/usr/bin/env python
"""
Script for API Gateway Service
"""
import os, gridfs, pika, json
from flask import Flask, request, send_file, render_template
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util
from bson.objectid import ObjectId


app = Flask(__name__)

mongo_video = PyMongo(app, uri="mongodb://host.minikube.internal:27017/videos")

mongo_mp3 = PyMongo(app, uri="mongodb://host.minikube.internal:27017/mp3s")

fs_videos = gridfs.GridFS(mongo_video.db)
fs_mp3s = gridfs.GridFS(mongo_mp3.db)

connection = pika.BlockingConnection()
channel = connection.channel()


@app.route("/login", methods=["POST"])
def login():
    """
    API Interface for AUTH service
    """
    token, err = access.login(request)

    if not err:
        return token
    else:
        return err


@app.route("/upload", methods=["GET", "POST"])
def upload():
    """
    API Interface for uploading
    """
    if request.method == "POST":
        access, err = validate.token(request)
        if err:
            return err
        access = json.loads(access)

        if access["admin"]:
            file = request.files.get("file")
            if not file:
                return "No file submitted", 400

            err = util.upload(file, fs_videos, channel, access)
            if err:
                return err

            return "Successfully uploaded", 200
        else:
            return "Not authorized", 401
    else:
        return render_template("upload.html"), 200


@app.route("/download", methods=["GET"])
def download():
    """
    API Endpoint to download item
    """
    access, err = validate.token(request)

    if err:
        return err

    access = json.loads(access)

    if access["admin"]:
        fid_string = request.args.get("fid")

        if not fid_string:
            return "fid is required", 400

        try:
            out = fs_mp3s.get(ObjectId(fid_string))
            return send_file(out, download_name=f"{fid_string}.mp3")
        except Exception as err:
            print(err)
            return "internal server error", 500

    return "not authorized", 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)