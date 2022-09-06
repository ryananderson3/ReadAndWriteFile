import csv

def main():
    
    infile = open('EmployeePay.csv', 'r')
    csvFile = csv.reader(infile, delimiter=',')
    infile.readline()

    for record in csvFile:
        totalPay = int(record[3]) + (int(record[3]) * float(record[4]))

        print('Employee ID:', record[0])
        print('First Name:', record[1])
        print('Last Name:', record [2])
        print('Salary:', record[3])
        print('Bonus:', record[4], 'of salary')
        print('Total pay:', totalPay)

        input()

main()
