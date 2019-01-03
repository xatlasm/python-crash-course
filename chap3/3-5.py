#Changing guest list
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