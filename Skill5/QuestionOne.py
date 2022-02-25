import csv
from operator import itemgetter
fields = ['EMPID','Name','DOB','Department','Designation','Experience',	'No of leaves','Salary']
rows = [['1',   'Mounika',  '02-05-2001',   'E-104',    'HR',       '1',    '20',   '30000'],
        ['2',   'Vishal',   '11-06-1984',	'E-105',    'Admin',    '5',    '15',   '25000'],
        ['3',   'Amitabh',  '20-02-2000',   'E-106',    'HR',       '10',   '30',   '15000'],
        ['4',	'Vivek',	'18-05-1986',	'E-107',	'Account',	'3',	'20',	'25000'],
        ['5',	'Niharika',	'05-12-1996',	'E-108',	'Account',	'18',	'20',	'15000'],
        ['6',	'Vipul'	,   '16-12-1992',	'E-109',	'Account',	'14',	'15',	'15000'],
        ['7',	'Satish',	'21-07-1990',	'E-110',	'Admin',	'2',	'17',	'40000'],
        ['8',	'Harsha',	'07-02-1999',	'E-111',	'Admin',	'6',	'18',	'20000'],
        ['9',	'Akash',	'21-04-1993',	'E-112',	'HR',	    '12',	'6',	'50000'],
        ['10',	'Pavan',	'07-03-1997',	'E-113',	'Admin',	'5',	'9',	'47000'],
        ['11',	'Gowtham',	'19-09-2000',	'E-114',	'Account',	'10',	'15',	'83000'],
        ['12',	'Sushmitha',	'04-11-1989',	'E-115',	'HR',	'4',	'5',	'60000'],
        ['13',	'Keshanand',	'03-06-1999',	'E-116',	'HR',	'3',	'6',	'55000'],
        ['14',	'Charan',	    '15-12-1998',	'E-117',	'Admin',	'0',	'9',	'48000'],
        ['15',	'Tejaswini',	'25-05-2000',	'E-118',	'Account',	'1',	'21',	'10000']]
print('*-*-* Working with CSV files in python *-*-*')
print('1. Insert into CSV File')
print('2. Read from CSV File')
print('3. Salary Less than 20000')
print('4. No of Leaves more than 2 days')
print('5. Experience greater than 10 years')
print('6. Access specific Employee using EMPID and Name')
choice=int(input('Enter Your choice : '))
if choice==1:
    filename = "Employees.csv"
    with open(filename, 'w') as csvfile:
        try:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
            print('Inserted into the CSV file')
        except Exception as e:
            print(e)
elif choice==2:
    with open("Employees.csv", mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)
elif choice==3:
    with open("Employees.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        # csv_reader = csv.reader(csv_file)
        for lines in csv_reader:
            if(int(lines['Salary'])<int(20000)):
                print(lines)
elif choice==4:
    with open("Employees.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        # csv_reader = csv.reader(csv_file)
        for lines in csv_reader:
            if(int(lines['No of leaves'])>int(2)):
                print(lines)
elif choice==5:
    with open("Employees.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for lines in csv_reader:
            if(int(lines['Experience'])>int(10)):
                print(lines)
elif choice==6:
    with open("Employees.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for lines in csv_reader:
            print("Name : ",lines["Name"])
            print("EMPID : ",lines["EMPID"])
else:
    print('*-*-*   **   *-*-*')
    print('Improper Selection')
    print('*-*-*   **   *-*-*')
    exit()