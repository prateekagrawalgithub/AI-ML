list=[]
result=[]
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    no = int(input()) 
    if no>0:
      result.append(no)
    list.append(no)   
print("This is yout input list:", list)
print("Desired result:", result)
