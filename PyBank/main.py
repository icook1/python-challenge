#Import OS and CSV 
import os
import csv
#Previous trouble with PC correctly identifying the directory. Identify current working directory and utilize absolute path to ensure correct file consistenly.
print("Current Working Directory:", os.getcwd())
os.chdir("C:\\Users\\ormis\\Desktop\\python-challenge\\PyBank\\Resources")
budget_csv = os.path.join("..", "Resources", "budget_data.csv")
absolute_csvpath = os.path.abspath(budget_csv)
print("Absolute Path:", absolute_csvpath)

#Open the CSV file in reader format with a comma delimiter.
with open(budget_csv, encoding="utf-8") as csv_file:
    budget_csv = csv.reader(csv_file, delimiter=",")
#Identify and move on from the CSV header if one is in the file.
    csv_header = next(csv_file)
#Establish baselines for variables to be utilized in the code.    
    total_months = 0
    money_previous = 0
    month_change = []
    total_money = 0
    money_change_list = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 99999999999999999999]
#Loop through the rows of the CSV to provide the Total Months, Total Revenue, Average Change, Greatest Increase and Decrease in Profits for a single month.
    for row in budget_csv:
        total_months = total_months + 1
        total_money = total_money + int(row[1])
        
        money_average = int(row[1]) - money_previous
        money_previous = int(row[1])
        money_change_list = money_change_list + [money_average]
        month_change = month_change +[row[1]]

        if (money_average > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = money_average

        if (money_average < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = money_average

money_average = sum(money_change_list) / len(money_change_list)


#Establish and print the final analysis of the CSV file.
final = (
    f" Financial Analysis \n"
    f"---------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_money}\n"
    f"Average Change: ${money_average}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(final)
#Write the results to the text file for final analysis.
with open("C:\\Users\\ormis\\Desktop\\python-challenge\\PyBank\\Analysis\\PyBank Analysis.txt", "w") as txt_file:
    txt_file.write(final)

    


