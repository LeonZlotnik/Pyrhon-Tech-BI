import csv

#Date = input("introduce Date: ")
#DateFound = False

with open('budget_data.csv', 'r', newline='') as csvfile:
    BudgetList = list(csv.reader(csvfile, delimiter=','))
    
 #   for item in BuggetList:
 #       if Date in item:
  #          DateFound = True
   #         break
        
#if DateFound:
 #   print(f"on {item[0]} the profit was {title[1]} and loss {title[2]} ")
#else:
 #   print("Date")

#print (BudgetList)

for Month in BudgetList:

    for M in Month:
        print (M)

        Integer = int(M)
        print(M)

#Month_Counter = M.count(Sum)
#print(Month_Counter)