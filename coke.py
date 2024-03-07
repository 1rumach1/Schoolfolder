def main():
  coins = 50
  print("$ python coke.py")
  print("Amount Due:", coins)
  while True:
    if coins < 0:
     break
    c = int(input("Insert Coin:"))
    if coins > 0:
        if c!=20 and c!=10 and c!=5:
            print("Amount Due:", coins)
            continue
        else:
         coins = coins - c 
    
    if coins <= 0:
        print(f"Change Owed: {(coins)* -1 }")
        break
    else:
        print("Amount Due:", coins)



main()







#





#