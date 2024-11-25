try:
    TotalPrice = float(input("Purchase amount : "))
    if TotalPrice == 0:
        raise ZeroDivisionError
    elif TotalPrice < 0:
        raise Exception 
    elif TotalPrice >= 5000:
        DS1 = TotalPrice * 0.2
        DS1_2 = TotalPrice - DS1
        print(f"20% Discount ={DS1} Total Price ={DS1_2} ")
    elif TotalPrice >= 2000:
        DS2 = TotalPrice * 0.1
        DS2_2 = TotalPrice - DS2
        print(f"10% Discount ={DS2} Total Price ={DS2_2} ")
    else:
        print("Purchase amount is not enough")
except ZeroDivisionError:
    print("Can't input 0 Value")
except ValueError:
    print("Only number is allow")
except:
    print("Negative Value is not Allow")
