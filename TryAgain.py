Total_Price = 0
while True:
    try:
        Product_Price = input("Product Price : ")
        if Product_Price == "exit":
            print(f"Total Price: {Total_Price}")
            break
        Product_Price = float(Product_Price)

        if Product_Price == 0:
            raise ZeroDivisionError
        elif Product_Price < 0:
            raise Exception
        else:
            Total_Price += Product_Price
    except ZeroDivisionError:
        print("ราคาสินค้าต้องมากกว่า 0")
    except ValueError:
        print("กรุณาใส่แค่ตัวเลขเท่านั้น ")
    except:
        print("ราคาสินค้าต้องไม่ติดลบ ")
