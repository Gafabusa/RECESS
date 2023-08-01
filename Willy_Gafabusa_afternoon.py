Mylist=["Willy","Perez","Amooti", "WillyTech","Gafs"]
print(Mylist[1])

#changing items
Mylist[0]="Harriet"
print(Mylist)

#Adding a sixth item to the list
Mylist.append("Kcee")
print(Mylist)

#Adding a third item to the list
Mylist[2]="Kaguta"
print(Mylist)

#Removing the 4th item from the list
Mylist.pop(3)
print(Mylist)

#Using negative indexing to print the last item in the list
print(Mylist[-1])

#List with seven items
Willytech=["orange","mango","apple","banana","cucumber", "pumpkin","pineapple"]
#using a range of indexes to print the 3rd,4th and 5th items in the list
print(Willytech[3:5])

#Newlist
Countries=["US", "Uganda","kenya","algeria","mozambique","Tanzania","Sudan"]
#making a copy of the list
Countries2=Countries.copy()
print(Countries2)

#Looping through the list
for x in Countries:
    print(x)

    #List of animals
    Animals=["Dog","Cat","Bird","Fox"]
    #arranging in ascending order
    Animals.sort()
    print(Animals)

#arranging in descending order
Animals.sort(reverse=True)
print(Animals)

#outputting only animal names with a in them
for x in Animals:
    if "a" in x:
        print(x)

myname=["GAFABUSA"]
myname2=["WILLY"]
#joining the two lists
myname.extend(myname2)
print(myname)


#Tuples
myphones =("iphone","redmi","tecno","ipad")

     #outputting my favorite brand
print(myphones[0])
     #negative indexing to print the second last item in the tuple
print(myphones[-2])

myphones=list(myphones)
#updating iphone to itel
myphones[0]="itel"
print(myphones)

#adding Huawei to the tuple
myphones.append("Huawei")
print(myphones)

#looping through the tuple
for x in myphones:
    print(x)

    #deleting the first item in the tuple
    myphones.pop(0)
    print(myphones)

    #using a tuple() constructor to write a tuple of cities in uganda
    mycities=tuple(["Kampala","Jinja","Masaka","Gulu"])
    print(mycities)

    #unpacking my tuple above
    print(mycities[0],mycities[1],mycities[2],mycities[3])

    #using a range of indexes to print the second,third and fourth cities in the tuple
    print(mycities[1:3])

    firstname=("Willy")
    lastname=("Gafabusa")
    #joining the two tuples
    fullname=firstname+lastname
    print(fullname)

    #tuple of colors
    colors=("red","blue","green","yellow")
    #multiplying the tuple by three
    colors=colors*3
    print(colors)

    thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    #return the number of times 8 appears in this tuple
    print(thistuple.count(8))


#Use the set() constructor to create a set of 3 of your favorite beverages
myfavorites=set(["soda","bear","juice"])
#adding two more items to the set
myfavorites.add("alcohol")
myfavorites.add("powerplay")
print(myfavorites)

mySet={"oven","kettle","microwave","rerigerator"}
#check if microwave is present in the set
print("microwave" in mySet)

#removing kettle from the set
mySet.remove("kettle")
print(mySet)

#looping through the set
for x in mySet:
    print(x)

    mylist2=["Pcee","Tech"]
    myset2={"Kenzo","Pallaso","Cool"}
    #adding items in the list to the items in the set
    myset2.update(mylist2)
    print(myset2)

    myages={20,21,23}
    myfirstnames={"John","Doe","Dally"}
    #joining the two sets
    myfirstnames.update(myages)
    print(myfirstnames)

    #STRINGS
    x=30
    y="Hello"
    #concatenating the above string and an integer
    mystring=str(x)+y
    print(mystring)

    txt=" Hello,   Uganda!  "
    #ouput the above string without spaces
    print(txt.strip())

    #python program to convert the value of 'txt' to uppercase
    print(txt.upper())

    #How to replace the value of 'U' with 'V'
    print(txt.replace("U","V"))

    y="I am proudly Ugandan" 
    #return a range of characters in the 2nd,3rd and 4th position
    print(y[1:4])

    #Dictionaries
    #no1
Shoes ={
    "brand": "nick",
    "color": "black",
    "size": 40
}
Shoes["size"]=50
#no2
Shoes["brand"]="adidas"
#no3
Shoes.update({"type": "sneakers"})
print(Shoes)
#no4
v =Shoes.keys
print(v)
#no5
s= Shoes.values()
print(s)
#no6
x="size" in Shoes
print(x)
#no7
for n in Shoes:
 print(n)
    #no8
Shoes.pop("color")
print(Shoes)
#no9
Shoes.clear()
print(Shoes)
#no10
hady= Shoes.copy()
print(hady)
#no11
jail = {
  "adam" : {
    "name" : "jati",
    "year" : 1994
  },
  "mariam"  : {
    "name" : "daniel",
    "year" : 1995
  },
  "hadijah" : {
    "name" : "adam",
    "year":1998
}}



