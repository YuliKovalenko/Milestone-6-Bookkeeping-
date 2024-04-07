import requests
import sys

def fetch_report(month, department):
    base_url = "http://127.0.0.1:5000"
    # Fetch birthdays
    response = requests.get(f"{base_url}/birthdays?month={month}&department={department}")
    birthdays = response.json()

    # Fetch anniversaries
    response = requests.get(f"{base_url}/anniversaries?month={month}&department={department}")
    anniversaries = response.json()

    print(f"Report for {department} department for {month.capitalize()} fetched.")
    print(f"Total Birthdays: {birthdays['total']}")
    if birthdays['total'] > 0:
        print("Birthdays:")
        for employee in birthdays['employees']:
            print(f"- {employee['date']}, {employee['name']}")

    print(f"Total Anniversaries: {anniversaries['total']}")
    if anniversaries['total'] > 0:
        print("Anniversaries:")
        for employee in anniversaries['employees']:
            print(f"- {employee['date']}, {employee['name']}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python fetch_report.py <month> <department>")
        sys.exit(1)
    month, department = sys.argv[1], sys.argv[2]
    fetch_report(month, department)