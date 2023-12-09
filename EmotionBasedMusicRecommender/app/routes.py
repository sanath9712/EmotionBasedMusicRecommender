# app/routes.py
from flask import render_template, jsonify, request
from app import app
import pandas as pd
import random
import os
from .model.emotion_predictor import get_emotion_from_text
from ..scripts.helper import select_best_matching_song

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

@app.route('/get_emotion_from_text', methods=['POST'])
def get_emotion_from_text():
    # Extract text from the request body
    data = request.json
    text = data.get('text', '')

    # Check if text is provided
    if text:
        predicted_emotions = get_emotion_from_text(text)
        track_id = select_best_matching_song(predicted_emotions)
        return jsonify(track_id=track_id)  # Return the track ID in the specified format
    else:
        return jsonify({"error": "No text provided"}), 400