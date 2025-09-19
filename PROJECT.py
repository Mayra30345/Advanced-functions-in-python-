number=int(input("You want odd and even numbers under what value:   "))
odd_list=[i for i in range(number) if i%2!=0]
print("List of odd number:",odd_list,"\n")

even_list=[i for i in range(number) if i%2==0]
print("List of even number:",even_list,"\n")

fruits=['apple','banana','mango','papaya','grapes']
Fruits=[x[0].upper()+x[1:] for x in fruits]
print("Fruits as proper nouns: ",Fruits)







