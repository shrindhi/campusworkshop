"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa3rbhp8u791gs1uu0-a.oregon-postgres.render.com",
        database="shri",
        user="shrinidhi",
        password="uSWY3cVTgNkS3UZV3Ygo6RZKP91uADJB")

# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
