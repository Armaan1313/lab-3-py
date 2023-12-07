a={}
print("menu\n 1. Add a product to the cart.\n 2. Search for a product.  \n 3. Delete a product from the cart. \n 4. Display the contents of the cart. \n 5. Purchase items.\n 6. Quit")
x=int(input("what dou want to add? : "))
while(x!=6):
    if x==1:
        p=input("add a product which you want to add in shopping cart")
     
    elif x==2:
        f=input("search a product name")
        if f in a:
            print("data found")
        else:
            print("display not found")
    
    elif x==3:
        f=input("delete a product")
    
    elif x==4:
        f=input("display the contents of the cart")
        
    elif x==5:
        f=input("Complete purchase (Y/N)?")
        if f=="Y":
            print("thank you for business")
        else:
            print("please continue shopping")
    print("menu\n 1. Add a product to the cart.\n 2. Search for a product.  \n 3. Delete a product from the cart. \n 4. Display the contents of the cart. \n 5. Purchase items.\n 6. Quit")
    x=int(input("what dou want to add? : "))
    
 
