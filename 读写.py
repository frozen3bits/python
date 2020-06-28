try:
    file=open("my file.txt","r")
except Exception as a:
    print(a)
    response=input("do you want to creat a new file:")
    if response=="yes":
        file=open("my file.txt","w")
else:
    file.write("asdf")
    file.close()

