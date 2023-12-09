import pandas as pd
import os
from app import app

def select_best_matching_song(predicted_emotions):
    # Load the songs dataset
    songs_df = pd.read_csv(os.path.join(app.root_path, '..', 'data', 'Processed_songs.csv'))

    # Filter songs based on predicted emotions and compute match count
    matching_songs = songs_df.loc[:, predicted_emotions].sum(axis=1)
    songs_df['Matched_Emotions'] = matching_songs

    # Filter songs that match the most number of predicted emotions
    max_matched_emotions = matching_songs.max()
    best_matching_songs = songs_df[songs_df['Matched_Emotions'] == max_matched_emotions]

    # If multiple songs match the same highest number of emotions, choose one
    if len(best_matching_songs) > 1:
        best_matching_songs = best_matching_songs.sort_values(by='Times_played', ascending=False)
    
    # Return the track ID of the top song
    return best_matching_songs.iloc[0]['Track_ID']