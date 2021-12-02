import random
print("This Application has 3 services for you")
while(1):
    print("1)Dice Roller with GUI")
    print("2)Dice Roller with out GUI")
    print("3)Tossing a coin")
    print("To exit from application press 0")
    a=int(input())
    if a==0:
        break
    elif a==3:
        while(1):
            print("1)You want to toss the coin?")
            print("2)Exit")
            b=int(input())
            if b==1:
                x=random.randint(1,2)
                if x==1:
                    print("You got heads")
                else:
                    print("You got tails")
            else:
                break
    elif a==2:
        while(1):
            print("Press 1 if you want to roll the dice")
            print("press 2 if you want to exit from this service")
            c=int(input())
            if c==1:
                y=random.randint(1,6)
                print("You got",y)
                print("\n")
            else:
                break
    else:
        while(1):
            print("Press 1 if you want to roll the dice")
            print("press 2 if you want to exit from this service")
            d=int(input())
            if d==1:
                z=random.randint(1,6)
                if z==1:
                    print("\n")
                    print("[     ]")
                    print("[  0  ]")
                    print("[     ]")
                    print("You got",z)
                    print("\n")
                elif z==2:
                    print("\n")
                    print("[0    ]")
                    print("[     ]")
                    print("[    0]")
                    print("You got",z)
                    print("\n")
                elif z==3:
                    print("\n")
                    print("[0    ]")
                    print("[  0  ]")
                    print("[    0]")
                    print("You got",z)
                    print("\n")
                elif z==4:
                    print("\n")
                    print("[0   0]")
                    print("[     ]")
                    print("[0   0]")
                    print("You got",z)
                    print("\n")
                elif z==5:
                    print("\n")
                    print("[0   0]")
                    print("[  0  ]")
                    print("[0   0]")
                    print("You got",z)
                    print("\n")
                else:
                    print("\n")
                    print("[0 0 0]")
                    print("[     ]")
                    print("[0 0 0]")
                    print("You got",z)
                    print("\n")
            else:
                break