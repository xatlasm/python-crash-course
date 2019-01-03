#Cars

def make_car(make, model, **options):
    car = {}
    car['make'] = make
    car['model'] = model
    for key, value in options.items():
        car[key] = value
    return car

car = make_car('subaru','outback', color='blue', tow_package=True)
print(car)