from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

def fetch_employees(month, department, event_type):
    employees = []
    with open('database.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Department'].lower() != department.lower():
                continue
            date_field = 'Birthday' if event_type == 'birthdays' else 'Hiring Date'
            date = datetime.strptime(row[date_field], '%Y-%m-%d')
            if date.strftime('%B').lower() == month.lower():
                employees.append({"id": row['Name'], "name": row['Name'], "date": date.strftime('%b %d')})
    return employees

@app.route('/birthdays', methods=['GET'])
def birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    employees = fetch_employees(month, department, 'birthdays')
    return jsonify({"total": len(employees), "employees": employees})

@app.route('/anniversaries', methods=['GET'])
def anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    employees = fetch_employees(month, department, 'anniversaries')
    return jsonify({"total": len(employees), "employees": employees})

if __name__ == '__main__':
    app.run(debug=True)