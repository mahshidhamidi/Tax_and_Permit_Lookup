import csv
import sqlite3


def insert_tax_csv_data():
    sql_insert="""
    INSERT INTO companies (bid, name, revenue, tax_paid) VALUES (?,?,?,?)
    """

    db = sqlite3.connect('database.db')
    cur = db.cursor()

    with open('tax.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        
        for row in reader:
            cur.execute(sql_insert,(row[1],row[2], row[4], row[5],))

    db.commit()
    db.close()

def insert_permits_csv_data():
    sql_insert="""
    INSERT INTO permits (address, city, bid) VALUES (?,?,?)
    """

    db = sqlite3.connect('database.db')
    cur = db.cursor()

    with open('permits.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        
        for row in reader:
            cur.execute(sql_insert,(row[1],row[3], row[7],))

    db.commit()
    db.close()

def lookup_permit_address(address, city):
    sql="""
    SELECT name, revenue FROM companies WHERE 
    bid=(SELECT bid FROM permits WHERE address=? 
    AND city=?);
    """
    db = sqlite3.connect('database.db')
    cur = db.cursor()

    #tmp = cur.execute(sql, (address,city,))
    #result = cur.fetchone()
    #return result

    result = cur.execute(sql, (address,city,)).fetchone()

    return f"Company: {result[0]}, Revenue: {result[1]}€"

def lookup_permits_by_company(company_name=None, bid=None):
    sql="""
    SELECT address, city FROM permits where bid=(SELECT bid from companies WHERE name=?);
    """
    sql2="""
    SELECT address, city FROM permits where bid=?;
    """

    db = sqlite3.connect('database.db')
    cur = db.cursor()

    #tmp = cur.execute(sql, (address,city,))
    #result = cur.fetchone()
    #return result
    if company_name:
        result = cur.execute(sql, (company_name,)).fetchall()
        return result
    elif bid:
        result = cur.execute(sql2, (bid,)).fetchall()
        return result
    else:
        return None

print(lookup_permit_address('Asemakatu 10', 'Ylivieska'))

locations = lookup_permits_by_company(bid="0187614-3")

for location in locations:
    print(f"Address: {location[0]}, City: {location[1]}")