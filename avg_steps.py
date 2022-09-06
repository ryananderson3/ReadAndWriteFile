import csv

def main():
    months = ['January', 'Febuary', 'March', 'April','May','June','July','August','September', 'October','November','December']
    
    outfile = open('avg_steps.csv', 'w')

    month = 1
    while month < 13:
        infile = open('steps.csv', 'r')
        csvFile = csv.reader(infile, delimiter=',')
        infile.readline()
        steps = 0
        count = 0
        for record in csvFile:
            if int(record[0]) == month:
                steps += int(record[1])
                count+=1
        
        avgSteps = steps/count
        outfile.write(months[month-1] + ',' + str(format(avgSteps, '.2f')+'\n'))
        month+=1

    outfile.close()

main()