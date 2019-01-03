#Restaurant seating
guests = input("How many people are in your party? ")
guests = int(guests)

if guests > 8:
    print("Please wait for your table to be ready.")
else:
    print("Your table is ready.")