n = int(input("Enter number of terms required (>2) :"))     #Input

no1=0
no2=1
i=3                                                         #Made_required_initialisations
    
print(no1)
print(no2)                                                  #Printing_first_two_terms_directly
    
while i<=n:                                                 #Loop_for_remaining_elements
    no1 += no2                                              #Defined_no1_as_next_element_after_no2
    no1,no2 = no2,no1                                       #Swapping_no1_&_no2
    print(no2)                                              #Printing_required_next_element
    i+=1                                                    #Counter_up
