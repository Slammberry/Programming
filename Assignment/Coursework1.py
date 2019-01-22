imAlready = ('Tracer','Widowmaker','Bastion','Winston','Genji','McCree')

def Game():

    def Death(reason):
        print(reason)
        Game()

    while True:
        name = input('Whats your name, ladde: ')
        for a in imAlready:
            if name == a:
                print('I\'m already ' + a)
            continue

        while True:
            tem1 = input('Did you say Rainbow Unicorn??? Y/N: ')
            if tem1 == 'n':
                print('\nOk, your name is Rainbow Unicorrn')
                name = 'Rainbow Unicorn'
                break
            if tem1 == 'y':
                print("\nDon't you joke with me, ladde")
            if tem1 == 'kill me':
                print('Ok')
                Death('You died from the old man.')
            else:
                print('\nI dinee catch that?')
        break

    inventory = {"Dagger": 0, "BluePotions": 0, "GoldenFeathers": 0, "Manuscrpits": 0}
    abilities = {"StealthPoints": 0, "FlyPoints": 0}
    while True:
        actionOne = input("You walk through a forest and see a BluePotion, do you pick it up? Y/N: ")
        if actionOne == "y":
            inventory['BluePotions']+=1
            abilities['StealthPoints']=+1
            print("Your BluePotions are at least this much: ", inventory['BluePotions'])
            break
        if actionOne == "n":
            print("You dummy...")
            break
        if actionOne == ' ':
            break
    while True:
        actionTwo = input("You continue walking and find 2 GoldenFeathers, do you pick them up? Y/N: ")
        if actionTwo == 'y' or actionTwo == 'Y':
            print('sorrey, ye kant')
            break
        if actionTwo == 'n' or actionTwo == 'N':
            print('It seems stuck anyways')
            break
        if actionTwo == '...':
            print('...?')

    a =input()

Game()
