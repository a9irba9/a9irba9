import tkinter as tk
from tkinter import messagebox
import json
import random
import string
import os
from flask import Flask, redirect, request

base_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(base_dir, "URLS", "shortened_urls.json")
os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
app = Flask(__name__)

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code


def save_url(original_url, short_code):
    data = {}
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                pass
    shortened_url = f"http://127.0.0.1:5000/{short_code}"
    data[short_code] = {"original_url": original_url, "shortened_url": shortened_url}

    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)

def shorten_url():
    original_url = entry_url.get()
    if not original_url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return
    
    short_code = generate_short_code()
    save_url(original_url, short_code)
    
    short_url = f"http://127.0.0.1:5000/{short_code}"
    messagebox.showinfo("URL Shortened", f"Shortened URL: {short_url}")

    entry_url.delete(0, tk.END)

root = tk.Tk()
root.title("URL Shortener")

label_url = tk.Label(root, text="Enter URL:")
label_url.pack(pady=5)

entry_url = tk.Entry(root, width=40)
entry_url.pack(pady=5)

btn_shorten = tk.Button(root, text="Shorten URL", command=shorten_url)
btn_shorten.pack(pady=10)

@app.route('/<short_code>')
def redirect_url(short_code):

    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            try:
                data = json.load(file)
                if short_code in data:
                    return redirect(data[short_code]["original_url"])
            except json.JSONDecodeError:
                pass
    return "Invalid URL", 404
if __name__ == '__main__':
    from threading import Thread
    thread = Thread(target=lambda: app.run(debug=True, use_reloader=False))
    thread.start()

    root.mainloop()
