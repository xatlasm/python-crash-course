def make_album(artist, album, tracknum = ''):
    """Returns a dictionary of an album"""
    albuminfo = {'artist' : artist, 'album' : album}
    if tracknum:
        albuminfo['tracks'] = tracknum
    return albuminfo
bh6 = make_album('fallout boy','big hero 6')
wa = make_album('weird al','alapalooza',12)
per = make_album('perufme','triangle')
print(bh6)
print(wa)
print(per)