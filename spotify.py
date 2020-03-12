import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
import spotipy.util as util
import pandas as pd
import sys

client_id = "3353eeea74f441c3b7e54d53830db121"
client_secret = "d2e91120369a4906a99cedde15e0c376"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

spotify_songs = {}
song_features = {}

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        trackId = track['id']
        audio_features(trackId)
        spotify_songs[trackId] = {}
        spotify_songs[trackId]['name'] = track['name']
        spotify_songs[trackId]['artist'] = track['artists'][0]['name']
        spotify_songs[trackId]['album'] = track['album']['name']
        spotify_songs[trackId]['duration'] = track['duration_ms']
        spotify_songs[trackId]['popularity'] = track['popularity']
        if (track['artists'][0]['name'] == 'Sam Smith'):
            print(spotify_songs[trackId])
        # print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            # track['name']))

def audio_features(track):
    if (track is not None):
        song_features[track] = {}
        features = sp.audio_features([track])
        if (features is not None):
            #Add new key-values to store audio features
        
            song_features[track]['acousticness'] = features[0]['acousticness'] or 0
            song_features[track]['danceability'] = features[0]['danceability'] or 0
            song_features[track]['energy'] = features[0]['energy'] or 0
            song_features[track]['instrumentalness'] = features[0]['instrumentalness'] or 0
            song_features[track]['liveness'] = features[0]['liveness'] or 0
            song_features[track]['loudness'] = features[0]['loudness'] or 0
            song_features[track]['speechiness'] = features[0]['speechiness'] or 0
            song_features[track]['tempo'] = features[0]['tempo'] or 0
            song_features[track]['valence'] = features[0]['valence'] or 0

if __name__ == '__main__':
    spotify_songs = {}
    username = "1212742718"    # Cates Username
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            print()
            print ('  total tracks', playlist['tracks']['total'])
            results = sp.playlist(playlist['id'],
                fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)

    df = pd.DataFrame.from_dict(spotify_songs)

    df.transpose().to_excel("songs.xlsx", engine='xlsxwriter')

    df2 = pd.DataFrame.from_dict(song_features)

    df2.transpose().to_excel("features.xlsx", engine='xlsxwriter')

    dic_df = {}
    dic_df['album'] = []
    dic_df['track_number'] = []
    dic_df['id'] = []
    dic_df['name'] = []
    dic_df['uri'] = []
    dic_df['acousticness'] = []
    dic_df['danceability'] = []
    dic_df['energy'] = []
    dic_df['instrumentalness'] = []
    dic_df['liveness'] = []
    dic_df['loudness'] = []
    dic_df['speechiness'] = []
    dic_df['tempo'] = []
    dic_df['valence'] = []
    dic_df['popularity'] = []


