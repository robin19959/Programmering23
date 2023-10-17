volym = int(input ("Enter a volume in liters:  "))
print("\n\n")


print("Do you want to convert the volume to:\n 1. Milliliters \n 2. Centiliters \n 3. Deciliters \n 4. Cubic decimeters \n 5. Cubic meters \n ")

enhet = int(input("Svar: "))

if enhet == 1:
    print (volym*1000)
if enhet == 2:
    print (volym*100)
if enhet == 3:
    print (volym*10)
if enhet == 4:
    print (volym*10*10)
if enhet == 5:
    print (volym*0.1*0.1)
    
if enhet != 1:
    print("Plz choose between 1-5")
    
if enhet != 2:
    print("Plz choose between 1-5")
    
if enhet != 3:
    print("Plz choose between 1-5")
    
if enhet != 4:
    print("Plz choose between 1-5")
    
if enhet != 5:
    print("Plz choose between 1-5")


    # test