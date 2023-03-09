'''
print("1. Start Purchasing")
print("2. Show available stock")
print("3. Exit")

x = input()

     
def purchase ():  
    print("Enter the item code")
    code = input()
    for line in open("item.txt", "r").readlines():
                    print(code)


if x == "1":
      purchase()
 
if x == "2":
    for line in open("item.txt", "r"):
        print(line)
    purchase()


if x == "3":
    exit()
'''
text = open("item.txt", "r").read()
code = input()
index = text.find(code)
for line in text.split("\n"):
    print(line[index:])
  