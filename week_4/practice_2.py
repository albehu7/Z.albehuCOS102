def changeme( mylist):
    #This changes a passed list
    mylist.append([1,2,3,4])
    print("Print values inside the funtion:", mylist)
    return
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function:", mylist)
