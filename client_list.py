
def main():

    infile = open('clients.txt', 'r')
    # loop through client list
    count = 1

    for line in infile:
        print(count, ". ", line.strip(),sep='')
        count+=1

main()
