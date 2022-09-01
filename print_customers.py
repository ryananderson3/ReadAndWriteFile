import csv

def main():
    
    infile = open('customers.csv', 'r')
    csvFile = csv.reader(infile, delimiter=',')

    for record in csvFile:
        
        print('ID:', record[0])
        print('First Name:', record[1])
        print('Last Name:', record[2])
        print('City:', record[3])
        print('Country:', record[4])
        print('Phone #:', record[5])
        
        input()
        

main()
