#Even length words in a String
a = input("Enter a String : ")
words = a.split(" ")
for i in words:
    if len(i)%2==0:
        print(str(i)+" ", end="")