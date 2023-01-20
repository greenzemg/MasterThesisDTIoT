import csv
from sys import argv
import pprint
from RISparser import readris

def compare_ris_files2(file1, file2):
    filtered = []

    # Read data from the first file
    with open(file1, 'r', encoding='utf-8') as bibliography_file1:
        entries1 = list(readris(bibliography_file1))

    # Read data from the second file 
    with open(file2, 'r', encoding='utf-8') as bibliography_file:
        entries2 = list(readris(bibliography_file))

    count = 0
    for entry1 in entries1:
        for entry2 in entries2:
            if 'doi' in entry1 and 'doi' in entry2:
                e1 = entry1['doi'].strip().replace(" ", "")
                e2 = entry2['doi'].strip().replace(" ", "")
                if e1 == e2 and e1 != "":
                    count = count + 1
                    print(count)
                    filtered.append(entry2)

    return filtered

def compare_ris_files(file1, file2):
    # Create empty sets to store the data from each file
    data1 = set()
    data2 = set()

    # Read the data from each file and add it to the corresponding set
    with open(file1, newline='', encoding='utf-8') as f1:
        reader1 = csv.DictReader(f1, delimiter='\t')
        i = 0
        for row in reader1:
            i = i + 1
            print(row)
            if i == 2: 
                break
            # data1.add(frozenset(row.items()))

    # with open(file2, newline='', encoding='utf-8') as f2:
    #     reader2 = csv.DictReader(f2, delimiter='\t')
    #     for row in reader2:
    #         data2.add(frozenset(row.items()))

    # # Find the duplicate entries by comparing the sets
    # duplicates = data1.intersection(data2)

    # # Print the duplicate entries
    # for duplicate in duplicates:
    #     print(dict(duplicate))

def list2ris(flist):
    pass



file1 = argv[1]
file2 = argv[2]


filout = compare_ris_files2(file1, file2)

result = list2ris(filout)