import csv
from sys import argv

# Input 
inputfile = argv[1]
outputfile = argv[2]


with open(inputfile, 'r', encoding='utf-8') as csvfile:
    # reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    reader = csv.DictReader(csvfile)

    # Open the RIS file for writing
    with open(outputfile, 'w', encoding='utf-8') as risfile:
        for row in reader:
            # Write the data to the RIS file
            print(row)
            risfile.write("TY  - JOUR\n")
            risfile.write("TI  - " + row['title'] + "\n")
            risfile.write("AU  - " + row['author'] + "\n")
            risfile.write("JO  - " + row['journal'] + "\n")
            risfile.write("AB  - " + row['abstract'].replace("\n", "")+ "\n")
            risfile.write("PY  - " + row['year'] + "\n")
            risfile.write("DO  - " + row['doi'] + "\n")
            risfile.write("VL  - " + row['volume'] + "\n")
            risfile.write("LA  - " + row['language'] + "\n")
            risfile.write("SN  - " + row['issn'] + "\n")
            risfile.write("AN  - " + row['year'] + "\n")
            risfile.write("N1  - " + row['note'] + "\n")
            risfile.write("KW  - " + row['keywords'] + "\n")
            risfile.write("PB  - " + row['publisher'] + "\n")
            risfile.write("DB  - " + row['source'] + "\n")
            risfile.write("UR  - " + row['url'] + "\n")
            risfile.write("ER  - \n")
            risfile.write("\t\n")

