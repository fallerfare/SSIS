import csv

with open('Students.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('writeStudents.csv', 'w') as newStudents_file:
        fieldnames = ['id', 'firstname', 'lastname', 'yearlevel', 'gender', 'programcode']
    
        csv_writer = csv.DictWriter(newStudents_file, fieldnames = fieldnames, delimiter = ',')

        csv_writer.writeheader()
        
        for line in csv_reader:
            csv_writer.writerow(line)
            print(line['yearlevel'])

    # for line in csv_reader: 
    #     print(line['yearlevel'])



