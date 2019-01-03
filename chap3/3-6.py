#More guests
guests = ["yuka", "sabrina", "ilka"]
print(guests[0].title() + ", you are cordially invited to dinner with me!")
print(guests[1].title() + ", you are cordially invited to dinner with me!")
print(guests[2].title() + ", you are cordially invited to dinner with me!")

print("Unfortunately, " + guests[2].title() + " cannot make it to dinner.")

#Replace Ilka
guests[2]="simone"

#Resend invites
print(guests[0].title() + ", you are cordially invited to dinner with me!")
print(guests[1].title() + ", you are cordially invited to dinner with me!")
print(guests[2].title() + ", you are cordially invited to dinner with me!")

print("A larger table has been located!")

#Expand guest lists
guests.insert(0,"shani")
guests.insert(2,"monica")
guests.append("lauren")

#Re-resend invites
print(guests[0].title() + ", you are cordially invited to dinner with me!")
print(guests[1].title() + ", you are cordially invited to dinner with me!")
print(guests[2].title() + ", you are cordially invited to dinner with me!")
print(guests[3].title() + ", you are cordially invited to dinner with me!")
print(guests[4].title() + ", you are cordially invited to dinner with me!")
print(guests[5].title() + ", you are cordially invited to dinner with me!")