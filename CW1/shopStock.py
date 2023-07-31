class Stockitem:

    #set initial varibles
    def __init__(self, quantity, price, code, brand):
        self.quantity = quantity
        self.priceV = price
        self.price = format((price/1.175),".2f")
        self.code = code
        self.brand = brand
        self.category = None
        self.name = "Unknown Stock Name"
        self.desc = "Unknown Stock Description"
        print("\nCreating a stock item there are "+str(quantity) +" item(s), costing "
        +str(price) +" per item, with the item code: "+code+". The brand for this product is: "+brand+"\n")

    #default setters and getter functions
    def getBrandName(self):
        print("Item name: " + self.brand+"\n")

    def setBrandName(self, brand):
        print("Changing name of brand "+self.code+" to "+brand+"\n")
        self.brand = brand

    def getCategory(self):
        print("Item name: " + self.category+"\n")

    def setCategory(self, category):
        print("Changing category "+self.code+" to "+category+"\n")
        self.category = category

    def getStockName(self):
        print("Item name: " + self.name+"\n")

    def setStockName(self, name):
        print("Changing name of item "+self.code+" to "+name+"\n")
        self.name = name

    def getStockDesc(self):
        print("Description: " + self.desc+"\n")

    def setStockDesc(self, desc):
        print("Changing description of item "+self.code+"to "+desc+"\n")
        self.desc = desc

    def getStockQuantity(self):
        print("Quantity of stock: "+str(self.quantity)+"\n")

    def increaseStock(self, increase):
        if ((self.quantity + increase) > 100):
            print("\nERROR: Stock quantity out of range")
            print("Current stock count: " + str(self.quantity)+"\n")
        else:
            print("Increasing quantity of item "+self.code+"\n")
            self.quantity = self.quantity + increase

    def sellStock(self, decrease):
        if ((self.quantity - decrease) < 0):
            print("ERROR: Stock quantity out of range")
            print("Current stock count: " + str(self.quantity)+"\n")
        else:
            print("Removing stock from item "+self.code+"\n")
            self.quantity = self.quantity - decrease

    def getStockPrice(self):
        print("Price of stock before VAT: "+str(self.price)+"")
        print("Price of stock after VAT: "+str(self.priceV)+"\n")

    def setPrice(self, price):
        if price >= 0:
            self.price = format((price/1.175),".2f")
            self.priceV = price
            print("Price with VAT is now: "+str(self.priceV))
        else:
            print("\nERROR: Stock price out of range")
            print("Current price: " + str(self.price)+"\n")
    
    #return stock info
    def __str__(self):
        return ("\nCategory: "+self.category+
        "\nBrand: "+self.brand+
        "\nStock code: "+self.code+
        "\nStock name: " +self.name+
        "\nDescription: "+self.desc+
        "\nQuantity: "+str(self.quantity)+
        "\nPrice before VAT: "+str(self.price)+
        "\nPrice after VAT: "+str(self.priceV))
        
#sub-class for navsat item
class NavSat(Stockitem, object):
    def __init__(self, quantity, price, code, brand, size):
        #super init class with NavSat varibles
        super(NavSat, self).__init__(quantity, price, code, brand)
        #define public class varibles
        self.name = "Navigation"
        self.desc = "GeoVision"
        self.category = "Car Accessories"
        #define private varible
        self.__screensize = size
        #setters and getters classes
    def getScreenSize(self):
        print("Screen Size: "+str(self.__screensize))
    def setScreenSize(self, size):
        print("Changing screen size of item "+self.code+"\n")
        self.__screensize = size
    def __str__(self):
        #super __str__ with added private varibles
        return (super(NavSat, self).__str__()+"\nScreen Size: "+str(self.__screensize))

#repeated for the other 3 subclasses
class DashCam(Stockitem, object):
    def __init__(self, quantity, price, code, brand, views):
        super(DashCam, self).__init__(quantity, price, code, brand)
        self.name = "Dash Cam"
        self.desc = "Saftey"
        self.category = "Car Accessories"
        self.__views = views
    def getViews(self):
        print("Item views: "+self.__views)
    def setViews(self, views):
        print("Changing views of item "+self.code+"\n")
        self.__views = views
    def __str__(self):
        return (super(DashCam, self).__str__()+"\nCamera Views: "+self.__views)

class WiperBlades(Stockitem, object):
    def __init__(self, quantity, price, code, brand, length):
        super(WiperBlades, self).__init__(quantity, price, code, brand)
        self.name = "Wipers"
        self.desc = "Screen Care"
        self.category = "Motoring Essentials"
        self.__length = length
    def getLength(self):
        print("Item Length: "+str(self.__length))
    def getLength(self, length):
        print("Changing length of item "+self.code+"\n")
        self.__length = length
    def __str__(self):
        return (super(WiperBlades, self).__str__()+"\nWiper Blade Length: "+str(self.__length))

class Battery(Stockitem, object):
    def __init__(self, quantity, price, code, brand, volt):
        super(Battery, self).__init__(quantity, price, code, brand)
        self.name = "Battery"
        self.desc = "Conventional"
        self.category = "Motoring Essentials"
        self.__voltage = volt
    def getVoltage(self):
        print("Item voltage: "+str(self.__voltage))
    def setVoltage(self, volt):
        print("Changing voltage of item "+self.code+"\n")
        self.__voltage = volt
    def __str__(self):
        return (super(Battery, self).__str__()+"\nBattery Voltage: "+str(self.__voltage)+"V")

#create stocks
navsys = NavSat(10, 10.99, 'NS101', 'TomTom', 5)
cam = DashCam(10, 162.99, 'SC920', 'NextBase', "Front and Rear")
wiper = WiperBlades(10, 17.99, 'LR210', 'BOSCH', 18)
battery = Battery(10, 100.99, 'BB606', 'Yuasa', 12)

#while varible
sys = True

#arrays for quick amending
#list of items for counting and function calling eg items[2].name
items = navsys, wiper, battery, cam
#additional information and varibles for ui output
addi = "Size", "Length", "Volt", "Views"

funName = "Name", "Description", "Quantity", "Brand", "Price"

while sys == True:
    #list all stock info
    print("PRINTING INITIAL STOCK INFO")
    for stock in (items):
        print(stock)

    #list avalible stocks
    print("\nWhich stock would you like to amend")
    count = 0
    for stock in (items):
        count=count+1
        print(str(count)+") "+stock.code+" - "+stock.name)
    
    #options to change infomation
    itemSel = int(input("\nENTER CORRESPONDING NUMBER: "))
    itemSel=itemSel-1
    print("\nHow would you like to amend "+items[itemSel].code+"?")

    #how to change that information
    count=0
    for i in funName:
        count=count+1
        print(str(count)+") "+funName[count-1])
    print(str(count+1)+") "+addi[itemSel])

    select = int(input("\nENTER CORRESPONDING NUMBER: "))

    #change product name
    if select == 1:
        (items[itemSel]).getStockName()
        data = input("Do you want to change this name (Y/N): ")
        if (data == "Y" or data == "y"):
            change = input("Enter desired name: ")
            items[itemSel].setStockName(change)

    #change product description
    if select == 2:
        (items[itemSel]).getStockDesc()
        data = input("Do you want to change this description (Y/N): ")
        if (data == "Y" or data == "y"):
            change = input("Enter desired description: ")
            items[itemSel].setStockDesc(change)

    #change product quantity
    if select == 3:
        (items[itemSel]).getStockQuantity()
        data = input("Do you want to change this value (Y/N): ")
        if (data == "Y" or data == "y"):
            try:
                change = input("Increase or decrease (+/-): ")
                value = int(input("Enter value of change: "))
                if change == "+":
                        items[itemSel].increaseStock(value)
                elif change == "-":
                        items[itemSel].sellStock(value)
                else:
                    print("TETYTTTTTTTTTTTTTTT")
            except:
                print("\nERROR: Incorrect value entered - Value has not been changed - Please try again")

    #change brand name
    if select == 4:
        (items[itemSel]).getBrandName()
        data = input("Do you want to change this brand (Y/N): ")
        if (data == "Y" or data == "y"):
            change = input("Enter desired brand: ")
            items[itemSel].setBrandName(change)
        
    #change price
    if select == 5:
        (items[itemSel]).getStockPrice()
        data = input("Do you want to change this value (Y/N): ")
        if (data == "Y" or data == "y"):
            try:
                change = float(input("Enter new price of this item (after VAT): "))
                items[itemSel].setPrice(change)
            except:
                print("\nERROR: Incorrect value entered - Value has not been changed - Please try again")

    #change additional info
    if select == 6:

        if itemSel == 0:
            items[itemSel].getScreenSize()
            data = input("Do you want to change this value (Y/N): ")
            if (data == "Y" or data == "y"):
                try:
                    change = int(input("Enter new screen size: "))
                    items[itemSel].setScreenSize(change)
                except:
                    print("\nERROR: Incorrect value entered - Value has not been changed - Please try again")

        if itemSel == 1:
            items[itemSel].getLength()
            data = input("Do you want to change this value (Y/N): ")
            if (data == "Y" or data == "y"):
                change = int(input("Enter new length: "))
                items[itemSel].setLength(change)

        if itemSel == 2:
            items[itemSel].getVoltage()
            data = input("Do you want to change this value (Y/N): ")
            if (data == "Y" or data == "y"):
                change = int(input("Enter new voltage: "))
                items[itemSel].setVoltage(change)

        if itemSel == 3:
            items[itemSel].getViews()
            data = input("Do you want to change this value (Y/N): ")
            if (data == "Y" or data == "y"):
                change = input("Enter views: ")
                items[itemSel].setViews(change)

    #quit system prompt
    data = input("\nWould you like to leave the system (Y/N): ")
    if ( data == "Y" or data == "y"):
            sys = False