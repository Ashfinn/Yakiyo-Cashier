print("1. Start Purchasing")
print("2. Show available stock")
print("3. Exit")

x = input()
   
def purchase ():  
    print("Enter the item code")
    text = open("item.txt", "r").read()
    y = text.split()
    code = input()
    for i in range(len(y)):
        counter = 0
        if y[i] == code:
            return print(y[i+1] + " " + y[i+2])
            counter+=1
    if counter < 1:
        return print("Item not found")

if x == "1":
      purchase()
 
if x == "2":
    for line in open("item.txt", "r"):
        print(line)
    purchase()


if x == "3":
    exit()

