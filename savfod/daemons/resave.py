import argparse
import csv
import traceback

DESCRIPTION="""
No discription for this prog. Guess? 
Guess??? Who is here?
"""

def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-f', '--file', required=True, help='filename that should be resaved')
    return parser.parse_args()

def read_wrong_csv(filename):
    with open(filename, 'r') as in_file:
        table = list(csv.reader(in_file, delimiter=','))
    return table

def test_table(table):
    assert(19 <= len(table) <= 21)
    assert(10 <= len(table[0]))
    for row in table:
        assert(len(row) == len(table[0]))

def write_good_csv(filename, table):
    with open(filename, 'w') as out_file:
        writer = csv.writer(out_file, delimiter='\t')
        for row in table:
            writer.writerow(row)


def resave(filename):
    table = read_wrong_csv(filename)
    try:
        test_table(table)
        write_good_csv(filename, table)
        print("File " + filename + " successfully resaved")
    except:
        print(traceback.format_exc())
        print("Bad format for resaving. Nothing changed in file " + filename)

if __name__ == "__main__":
    parser = parse_args()
    resave(parser.file)