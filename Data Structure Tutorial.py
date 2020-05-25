list1=[1,2,5]
list2=[6,7,9]
tuple=(1,2,6)
dict={"1":"Stop", "2":"Wait", "3":"Go"}

no1=int(input("Enter number to add in list1:"))
no2=int(input("Enter number to add in list2:"))
list1.append(no1)
list2.append(no2)   #Assigning elements to different lists
print("List1:", list1)
print("List2:", list2)

no=int(input("Enter index number of element you want to access fromt the tuple"))
print(tuple[no])   #Accessing elements from a tuple

del dict["2"]  #deleting dictionary element
print(dict)
