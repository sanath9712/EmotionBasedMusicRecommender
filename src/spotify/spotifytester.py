import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from credentials import APIKeys

client_id = APIKeys.get_client_id()
client_secret = APIKeys.get_client_secret()

# printing values to see if they are accessible
print(client_id)
print(client_secret)

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

redirect_uri = 'http://localhost:8889/callback'
playlist_id = '54FWKfSRIHnwkq0trEyT5h'  # Our project's playlist ID

# Set up authorization
scope = "playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Fetch tracks from the playlist
results = sp.playlist_tracks(playlist_id)
tracks = results['items']

# If the playlist is large, paginate through the results
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# Print track names and artists
for idx, item in enumerate(tracks):
    track = item['track']
    print(f"{idx+1}. {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")




