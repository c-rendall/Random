import sqlite3
import random 
from datetime import datetime, timedelta 

# Generate synthetic data 
def generate_synthetic_data(num_records): 
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

    icd_10_codes = []
    for _ in range(num_records):
        category = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        subcategory = random.randint(0, 99)
        subcategory_str = str(subcategory).zfill(2)
        extension = random.choice(['.', '-', '/', ''])
        extension_str = random.choice(['', '0', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09'])
        icd_10_code = category + subcategory_str + extension + extension_str
        icd_10_codes.append(icd_10_code)

    cpt_codes = []
    for _ in range(num_records):
        section = random.choice(['1', '2', '3', '4', '5', '6'])
        subsection = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        category = random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'])
        code = section + subsection + category
        cpt_codes.append(code)

    in_scope_choices = [0, 1]

    data = []
    for _ in range(num_records):
        member_id = random.randint(1000, 9999)
        date_of_service = datetime.now() - timedelta(days=random.randint(1, 365))
        state = random.choice(states)
        icd10_code = random.choice(icd_10_codes)
        cpt_code = random.choice(cpt_codes)
        net_pay = round(random.uniform(50.0, 500.0), 2)
        in_scope = random.choice(in_scope_choices)
        data.append((member_id, date_of_service, state, icd10_code, cpt_code, net_pay, in_scope))
    return data

# Create SQLite database and table
def create_database_and_table():
    conn = sqlite3.connect('medical_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS medical_data (
                        member_id INTEGER,
                        date_of_service TEXT,
                        state TEXT,
                        icd10_code TEXT,
                        cpt_code TEXT,
                        net_pay REAL,
                        in_scope INTEGER
                        )''')
    conn.commit()
    conn.close()

# Insert data into SQLite database
def insert_data_into_database(data):
    conn = sqlite3.connect('medical_data.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO medical_data VALUES (?, ?, ?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()

# Execute SQL queries on SQLite database
def execute_sql_queries():
    conn = sqlite3.connect('medical_data.db')
    cursor = conn.cursor()
    
    # Example SQL queries
    cursor.execute('SELECT COUNT(*) FROM medical_data WHERE in_scope = 1')
    print("Number of in-scope members:", cursor.fetchone()[0])
    
    cursor.execute('SELECT state, AVG(net_pay) FROM medical_data GROUP BY state')
    avg_net_pay_by_state = cursor.fetchall()
    print("Average net pay by state:")
    for row in avg_net_pay_by_state:
        print(row)
    
    conn.close()

def main():
    num_records = 100000
    synthetic_data = generate_synthetic_data(num_records)
    
    create_database_and_table()
    insert_data_into_database(synthetic_data)
    
    execute_sql_queries()

if __name__ == "__main__":
    main()
    

