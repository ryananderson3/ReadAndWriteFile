import csv

def main():

    outfile = open('customer_country.csv', 'w')
    infile = open('customers.csv', 'r')
    csvFile = csv.reader(infile, delimiter=',')

    outfile.write('Full Name,Country\n')
    infile.readline()

    for customer in csvFile:
        outfile.write(customer[1] + ' ' + customer[2] + ',' + customer[4] + '\n')
    
    outfile.close()

main()

