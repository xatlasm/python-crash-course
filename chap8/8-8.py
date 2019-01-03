#User Albums
def make_album(artist, album, tracknum = ''):
    """Returns a dictionary of an album"""
    albuminfo = {'artist' : artist, 'album' : album}
    if tracknum:
        albuminfo['tracks'] = tracknum
    return albuminfo
while True:
    artist = input('Artist: ')
    if artist == 'q':
        break
    album = input('Album: ')
    if album == 'q':
        break
    tracks = input('Tracks: ')
    if tracks == 'q':
        break
    output = make_album(artist, album, tracks)
    print(output)