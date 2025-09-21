import pandas as pd
import matplotlib.pyplot as plt

file = "owid-covid-data.csv"
data = pd.read_csv(file)
data = data
country_data = pd.read_csv(file)
country_data =  country_data.loc[country_data["continent"] == "Asia", "location"]
print("By Default Brazil is Selected")
print("Select 2 Countries Names From Below: ");
print("")
a = input("Press any key to see country lists: ");
print(country_data.drop_duplicates())
a = input("Enter 1st name from list: ")
b = input("Enter 2nd name from list: ")

print("Countries Selected: ",a," ", b)


c = "0";
while(c!="4"):
    print("Select below options: \n1-Death Evolution\n2-Number of cases\n3-Total Vaccinations\n4-Exit")
    c = input();
    cd = "Brazil"
    if c == "1":
        dcd =data.loc[data["location"] == cd,'new_deaths']
        print("******** COUTRY DEATHS ",cd," *********\n",dcd)
        da =data.loc[data["location"] == a,'new_deaths']
        print("******** COUTRY DEATHS ",a," *********\n",da)
        db =data.loc[data["location"] == b,"new_deaths"]
        print("******** COUTRY DEATHS ",b," *********\n",db)
        print("\n\nMean for Country: ",a,da.mean())
        print("\n\nMean for Country: ",b,db.mean())
        
        dcd.plot()
        da.plot()
        db.plot()
        
        plt.show()
    elif c =="2":
        ccd = data.loc[data["location"] == cd,"total_cases"]
        print("******** COUTRY CASES ",cd," *********\n",ccd)
        ca = data.loc[data["location"] == a,"total_cases"]
        cb = data.loc[data["location"] == b,"total_cases"]
        print("******** COUTRY CASES ",a," *********\n",ca)
        print("******** COUTRY CASES ",b," *********\n",cb)
        print("\n\nMean for Country: ",a,ca.mean())
        print("\n\nMean for Country: ",b,cb.mean())
        ccd.plot()
        ca.plot()
        cb.plot()
        plt.show()
    elif c == "3":
        vcd = data.loc[data["location"] == cd,"total_vaccinations"]
        print("******** COUTRY VACCINATIONS ",cd," *********\n",vcd)
        va = data.loc[data["location"] == a,"total_vaccinations"]
        vb = data.loc[data["location"] == b,"total_vaccinations"]
        print("******** COUTRY VACCINATIONS ",a," *********\n",va)
        print("******** COUTRY VACCIINATIONS ",b," *********\n",vb)
        print("\n\nMean for Country: ",a,va.mean())
        print("\n\nMean for Country: ",b,vb.mean())
        
        vcd.plot()
        va.plot()
        vb.plot()
        plt.show()
    elif c == "4":
        print("Program Exited")
    else:
        print("Error Select Correct Option")