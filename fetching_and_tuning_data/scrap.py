import lyricsgenius
genius = lyricsgenius.Genius("3bXGOZkScFWpReDHQ5oDCs5_Z1JfahxyPQDcziqqjLV0xTECeOccM_yFMkUvzlgz")

def fetch(song,artist):
    song = genius.search_song(song,artist)
    lyrics = song.lyrics
    lyrics = lyrics.split("\n")
    lyrics = [line for line in lyrics if line and line[0] != '[']
    print(lyrics)
    return lyrics

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
        ans = fetch(artist,song)
        # print(ans)
