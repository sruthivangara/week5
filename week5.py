#1. Created an single list that consists of all the data

my_list1 = [1121, "Jackie Grainger", 22.22,
1122, "Jignesh Thrakkar", 25.25,
1127, "Dion Green", 28.75, False,
24.32, 1132, "Jacob Gerber",
"Sarah Sanderson", 23.45, 1137, True,
"Brandon Heck", 1138, 25.84, True,
1152, "David Toma", 22.65,
23.75, 1157, "Charles King", False,
"Jackie Grainger", 1121, 22.22, False,
22.65, 1152, "David Toma"]

#created an empty dictonary
my_dict = {}
#created an empty list
list1=[]

totalhourly_wages = []  #created an empty list named totalhourly_wage
underpaid_salaries=[]      #created an empty list named unpaid_salaries
comapny_raises=[]       #created an empty list named company_raises

#removing duplicates
for i in my_list1:
    if i not in list1:
        list1.append(i)
       
#Each dictionary must be in a database-like format.
        
for i in list1:
    if type(i) is int:
        my_dict["employee_information"]=i
    if type(i) is str:
        my_dict["employee_name"]=i   
    # adding 1.3 to the wage salary for hour
    if type(i) is float:
        my_dict["hourly_wage"]=i
        my_dict["totalhourly_wage"]=i*1.3  #multiplying the current hourly wage value by 1.3
        totalhourly_wages.append(my_dict["totalhourly_wage"]) #adding totalhourly_wage to the dictionary named my_dict
        print(my_dict)
        # print()        
        for i,hourly_wage in my_dict.items():
            if type(hourly_wage)==float:

                #to find out the underpaid salaries

                if hourly_wage>=28.15 and hourly_wage<30.65:                   
                   underpaid_salaries.append(my_dict["employee_name"])

#If the hourly rate (not the total hourly rate) is between 22 and 24 dollars per hour, apply a 5% raise to the current rate. 
# If the hourly rate is between 24 and 26 dollars per hour, apply a 4% raise to the current rate. If the hourly rate is between 26 and 28 dollars per hour, apply a 3% raise to the current rate. 
# All other salary ranges should get a standard 2% raise to the current rate.

                if hourly_wage>=22 and hourly_wage<=24:
                    hourly_wage*=0.05                    
                elif hourly_wage>=24 and hourly_wage<=26:
                    hourly_wage*=0.04
                elif hourly_wage>=26 and hourly_wage<=28:
                    hourly_wage*=0.03
                else:
                    hourly_wage*=0.02
        comapny_raises.append(my_dict["employee_name"])
        comapny_raises.append(my_dict["hourly_wage"])


#printing all three lists created (totalhourly_wages,underpaid_salaries,company_raises)
print()
print(totalhourly_wages)  #this will print totalhourly_wages list
print()
print(underpaid_salaries) #this will print underpaid_salaries list
print()
print(comapny_raises)     #this will print company_raises list

#GitHub Link https://github.com/
#Repository Name: week5