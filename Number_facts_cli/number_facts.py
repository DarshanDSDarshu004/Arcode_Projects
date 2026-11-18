
import math

def count_digits(n):
    count=0
    while n!=0:
        count+=1
        n//=10
    return count


def digit_sum(n):
    sum=0
    while n!=0:
        sum+=n%10
        n//=10
    return sum


def print_divisors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res

def is_prime(n):
    if(n<=2):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


def main():
    n=int(input("Enter a number"))

    print(count_digits(n))
    print(digit_sum(n))
    ans=print_divisors(n)
    for i in range(len(ans)):
        print(ans[i],end=" ")
    print("")
       
        
    
    print(is_prime(n))
   
if __name__=="__main__":
    main()
     
    

    