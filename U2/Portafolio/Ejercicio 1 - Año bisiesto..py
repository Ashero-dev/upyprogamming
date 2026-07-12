#año biciesto
year= int(input("Enter a year: "))
if (year % 4 == 0 and year %100 !=0) or (year %400 ==0):
    print(f"is a year biciest{year}")
else: 
    print(f"is not a year biciest{year}")