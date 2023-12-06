# app/routes.py
from flask import render_template, jsonify
from app import app
import pandas as pd
import random
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_track', methods=['GET'])
def get_random_track():
    # The path to the 'songs.csv' file is relative to the 'app' directory
    csv_path = os.path.join(app.root_path, '..', 'data', 'songs.csv')
    df = pd.read_csv(csv_path)
    # Select a random track ID from the 'Track_ID' column
    random_track_id = random.choice(df['Track_ID'].dropna().tolist())
    return jsonify(track_id=random_track_id)
