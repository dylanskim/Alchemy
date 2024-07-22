air = 0
earth = 0
fire = 0
water = 0

dust = 0 #earth + air
lava = 0 #earth + fire
mud = 0 #earth + water
inferno = 0 #air + fire
cloud = 0 #air + water
steam = 0 #fire + water

pdust = ""
plava = ""
pmud = ""
pinferno = ""
pcloud = ""
psteam = ""

user_create = ""

print("You begin your alchemy journey with nothing:")

while user_create != "exit":

    printadd = "".join((pdust + plava + pmud + pinferno + pcloud + psteam))  
    print("\nEarth:", earth, "\nAir:", air, "\nFire:", fire, "\nWater:", water, printadd)

    user_create = input("Create: ").casefold().replace(" ", "")

    if user_create == "earth":
        earth += 10
    if user_create == "air":
        air += 10
    if user_create == "fire":
        fire += 10
    if user_create == "water":
        water += 10
    if user_create == "earth+air" and earth > 1 and air > 1:
        dust += 1
        earth -= 1
        air -= 1
        pdust = "\nDust: " + str(dust)
    if user_create == "earth+fire" and earth > 1 and fire > 1:
        lava += 1
        earth -= 1
        fire -= 1
        plava = "\nLava: " + str(lava)
    if user_create == "earth+water" and earth > 1 and water > 1:
        mud += 1
        earth -= 1
        water -= 1
        pdmud = "\nMud: " + str(mud)
    if user_create == "air+fire" and air > 1 and fire > 1:
        inferno += 1
        air -= 1
        fire -= 1 
        pinferno = "\nInferno: " + str(inferno)
    if user_create == "air+water" and air > 1 and water > 1:
        cloud += 1
        air -= 1
        water -= 1
        pcloud = "\nCloud: " + str(cloud)
    if user_create == "fire+water" and fire > 1 and water > 1:
        steam += 1
        fire -= 1
        water -= 1
        psteam = "\nSteam: " + str(steam)
else:
    print("Finished with:\nEarth:", earth, "\nAir:", air, "\nFire:", fire, "\nWater:", water, printadd)