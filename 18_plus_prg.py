# user ne pucho kai rand chodvi che 
# mia ne chodvi hoi to 1st floor 
# dennie D ne chodvi hoi to 2nd floor 
# brandi ne chodvi hoi to 3rd floor 
# jasmine ne chodvi hoi to 4rd floor 
menu = ("Mia", "Denni", "Brandi", "Jasmine")

print("Avalable randu")
for inx, rand in enumerate(menu):
    print(inx+1, rand)
# Rename-Item -Path "c:/Users/jayki/Untitled-3.py" -NewName "18_plus_prg.py"

rand_nu_naam = input("Rand nu naam kyo: ").lower()
print("Tamari pasand sari che")

if rand_nu_naam == "mia":
    print("1st floor uper che ")
elif rand_nu_naam == "denni":
    print("2nd floor uper che")
elif rand_nu_naam == "brandi":
    print("3rd floor uper che")
elif rand_nu_naam == "jasmine":
    print("4th floor uper che")
else:
    print("E to maa chodava gai se")