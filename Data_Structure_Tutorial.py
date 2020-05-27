list1=[1,2,5]
list2=[6,7,9]
tuple=(1,2,6)
dict={"1":"Stop", "2":"Wait", "3":"Go"}            #Defining_these_to_work_and_edit_these_ahead

no1=int(input("Enter number to add in list1:"))
no2=int(input("Enter number to add in list2:"))    #Taking_inputs_for_LISTS_task
list1.append(no1)
list2.append(no2)                                  #Assigning_elements_to_different_LISTS
print("List1:", list1)
print("List2:", list2)

no=int(input("Enter index number of element you want to access fromt the tuple"))
print(tuple[no])                                   #Accessing_elements_from_a_TUPLE

del dict["2"]                                      #deleting_DICTIONARY_element
print(dict)
