try:
    age=int(input("Enter an age:"))
    if(age<18):
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")
    if age%2==0:
        print("odd number")
    elif age%2==1:
        print("odd number")