
# Taken from https://github.com/plamere/spotipy
#   on 23 02 2020 by PM

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.search(q='weezer', limit=1)
track_info = results['tracks']['items'][0]
aud_anal = sp.audio_analysis(track_info['uri'])

#for key in track_info:
    #print(key)

for key in aud_anal:
    isDict = False
    print(key)
    for item  in aud_anal[key]:
        if not isinstance(item,dict):
            print('  ' + str(item))
        else:
            isDict = True
    if isDict:
        print('  This section contains tons of timestamped attributes.')
        print('  Run `python audio_analysis_verbose.py` to see the contents.')
    print()


