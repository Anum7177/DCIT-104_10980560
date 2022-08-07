highest_value=int(input("Enter a number: "))
print("***********************")
print(f"Prime numbers below {highest_value} are")
def prime_num():
    count_of_prime=0
    total=0
    for first in range(2,highest_value):
            for second in range (2,first):        
                if first%second==0:
                    break
            else:
                print(first)
                count_of_prime+=1
                total+=first
    average=total/count_of_prime
    print("******************************************")
    print(f"Prime numbers printed below {highest_value} are",count_of_prime)
    print(" ")
    print("The sum of the prime numbers printed is",total)
    print(" ")
    print("The average of the prime numbers is",average)
    
prime_num()
    
        
    
                
        
                
                
