import random
import string
from flask import Flask, render_template, redirect, request
import json
import os
import logging

app = Flask(__name__)
shortened_urls = {}

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load existing URLs from the JSON file if it exists
if os.path.exists("\\Python\\Projetcs\\URL Shortener\\URLS\\urls.json"):
    with open("\\Python\\Projetcs\\URL Shortener\\URLS\\urls.json", "r") as f:
        shortened_urls = json.load(f)
    logging.debug(f"Loaded URLs from JSON: {shortened_urls}")

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        long_url = request.form["long_url"]
        short_url = generate_short_url()
        while short_url in shortened_urls:
            short_url = generate_short_url()
        
        shortened_urls[short_url] = long_url
        with open("\\Python\\Projetcs\\URL Shortener\\URLS\\urls.json", "w") as f:
            json.dump(shortened_urls, f)
        logging.debug(f"Shortened URL: {short_url} -> {long_url}")
        return f"Shortened URL: {request.url_root}{short_url}"
    return render_template("index.html")

@app.route("/<short_url>")
def redirect_long_url(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        logging.debug(f"Redirecting to: {long_url}")
        return redirect(long_url)
    else:
        logging.error(f"URL not found for short URL: {short_url}")
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)

