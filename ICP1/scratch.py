name = input("enter a string")
ch1 = input("enter a character1 to be deleted")
ch2 = input("enter a character2 to be deleted")
newname = name.replace(ch1,'')
newname1 = newname.replace(ch2,'')
rname=""
for i in newname1:
    rname = i + rname
print("The reverse string is %s"%(rname))