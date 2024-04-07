import csv
import argparse
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(description='Generate a report for birthdays and anniversaries.')
    parser.add_argument('filename', help='Database CSV file name')
    parser.add_argument('month', help='Month to generate report for')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose report including names')
    return parser.parse_args()

def generate_report(filename, month, verbose):
    birthdays = {}
    anniversaries = {}
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            b_month = datetime.strptime(row['Birthday'], '%Y-%m-%d').strftime('%B').lower()
            a_month = datetime.strptime(row['Hiring Date'], '%Y-%m-%d').strftime('%B').lower()
            department = row['Department']
            
            if b_month == month.lower():
                if department not in birthdays:
                    birthdays[department] = []
                birthdays[department].append(row['Name'])
            
            if a_month == month.lower():
                if department not in anniversaries:
                    anniversaries[department] = []
                anniversaries[department].append(row['Name'])
    
    print(f"Report for {month.capitalize()} generated")
    print("--- Birthdays ---")
    total_birthdays = sum(len(names) for names in birthdays.values())
    print(f"Total: {total_birthdays}")
    for department, names in birthdays.items():
        print(f"- {department}: {len(names)}")
        if verbose:
            for name in names:
                print(f"  - {name}")
    
    print("--- Anniversaries ---")
    total_anniversaries = sum(len(names) for names in anniversaries.values())
    print(f"Total: {total_anniversaries}")
    for department, names in anniversaries.items():
        print(f"- {department}: {len(names)}")
        if verbose:
            for name in names:
                print(f"  - {name}")

if __name__ == "__main__":
    args = parse_args()
    generate_report(args.filename, args.month, args.verbose)
