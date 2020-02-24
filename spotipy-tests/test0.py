
# Taken from https://spotipy.readthedocs.io/en/2.9.0/
# 23 02 2020 
# TODO Not currently working

import spotipy

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify()

sp.trace = True # turn on tracing
sp.trace_out = True # turn on trace out

artist = sp.artist(urn)
print(artist)

user = sp.user('plamere')
print(user)
