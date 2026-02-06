try:
    p = float(input("Enter the Principle amount "))
    n = float(input("Enter the No of month "))
    r = float(input("Enter the rate of interest"))
    if(p<0 or n<0 or r<0):
        print("negative input")
    else:
        si = (p*n*r)/100
        print("The simplle interest for",n,"month is",si)
        ta = si+p
        print("The Total amount is",ta)
except:
    print("Invalid Input")
