

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.search(q='weezer', limit=1)
track_info = results['tracks']['items'][0]
aud_anal = sp.audio_analysis(track_info['uri'])

#for key in track_info:
    #print(key)

for key in aud_anal:
    print(key)
    for key0 in aud_anal[key]:
        print('  ' + str(key0))
    print()


