import lyricsgenius
import os

genius = lyricsgenius.Genius("3bXGOZkScFWpReDHQ5oDCs5_Z1JfahxyPQDcziqqjLV0xTECeOccM_yFMkUvzlgz")

# Fetch(song,artist) passing song and artist
def fetch(song,artist):
    song = genius.search_song(song,artist)
    lyrics = song.lyrics
    lyrics = lyrics.split("\n")
    lyrics = [line for line in lyrics if line and line[0] != '[']
    # print(lyrics)
    return lyrics

def removepuncutation(lyrics):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    new_lyrics = []
    for lyr in lyrics:
        no_pun = ""
        for char in lyr:
            if char not in punctuations:
                no_pun = no_pun + char
        new_lyrics.append(no_pun)
    return new_lyrics

# Include More artist
artist_to_songs = {

    'Arijit Singh' : [
        'Milne Hai Mujhse Aayi',
        'Humdard',
        
    ],
    'Neha Kakkar':[
        'Hauli Hauli'
    ]

}

# 
for artist in artist_to_songs:
    
    for song in artist_to_songs[artist]:
        final_lyrics = fetch(artist,song)
        final_lyrics = removepuncutation(final_lyrics)
        # print(ans)

