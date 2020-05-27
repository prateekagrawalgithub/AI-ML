list=[]
result=[]                                         #Defining_empty_lists_for_required_operations

n = int(input("Enter number of elements : "))     #Input_of_Number-of-Elements

for i in range(0, n):                             #Input_data_with_selection_of_Positive-Numbers_to_Result-List
    no = int(input()) 
    if no>0:
      result.append(no)
    list.append(no)  
          
print("This is yout input list:", list)           #Output_of_Input-List_and_Result-List
print("Desired result:", result)
