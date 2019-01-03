#My Pizzas, Your Pizzas
pizzas = ["cheese", "pepperoni", "veggie"]
friend_pizzas  = pizzas[:]
pizzas.append('pineapple')
friend_pizzas.append('bacon')
for pizza in pizzas:
    print("My favorite pizzas are: " + pizza)
for pizza in friend_pizzas:
    print("My friend's favorite pizzas are: " + pizza)