from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    return "Inventory App Running (No DB)"

@app.route("/add/<item>")
def add_item(item):
    r.lpush("items", item)
    return jsonify({"message": f"{item} added"})

@app.route("/items")
def get_items():
    items = r.lrange("items", 0, -1)
    items = [item.decode("utf-8") for item in items]
    return jsonify({"items": items})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)