inventory = {"Dagger": 0, "BluePotions": 0, "GoldenFeathers": 0, "Manuscrpits": 0}
abilities = {"StealthPoints": 0, "FlyPoints": 0}
while True:
    actionOne = input("You walk through a forest and see a BluePotion, do you pick it up? Y/N: ")
    if actionOne == "y":
        inventory['BluePotions']+=1
        print("Your BluePotions are at least this much: ", inventory['BluePotions'])
        break
    if actionOne == "n":
        print("You dummy...")
        break
    if actionOne == ' ':
        break
while True:
    actionTwo = input("You continue walking and find 2 GoldenFeathers, do you pick them up? Y/N: ")
