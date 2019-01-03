#Favorite places
favorite_places = {
    'alice' : ['paris', 'marseille'],
    'bob' : ['tokyo'],
    'charlie' : ['london'],
}
for person, places in favorite_places.items():
    print(person.title() + ':')
    for place in places:
        print(place.title())
    print('\n')