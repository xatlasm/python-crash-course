#Rivers
rivers = {
    'nile' : 'egypt',
    'mississippi' : 'united states',
    'seine' : 'france',
    }
for k,v in rivers.items():
    print('The ' + k.title() + " runs through " + v.title() + '.')
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())