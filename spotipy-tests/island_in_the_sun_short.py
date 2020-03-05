

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.search(q='weezer', limit=10)
track_info = results['tracks']['items'][1]
aud_anal = sp.audio_analysis(track_info['uri'])

#for key in track_info:
    #print(key)

# printing contents of audio analysis in a readable format

for key in aud_anal:
    isDict = False
    print(key)
    for item  in aud_anal[key]:
        if not isinstance(item,dict):
            print('  ' + str(item))
            item_val = str(aud_anal[key][item])
            item_val = item_val if len(item_val) < 30 else item_val[0:10] + '... truncated'
            if key == 'track':
                print('    ' + str(item_val))
        else:
            isDict = True
    if isDict:
        print('  This section contains tons of timestamped attributes.')
        print('  Run `python audio_analysis_verbose.py` to see the contents.')
    print()


