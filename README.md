# Tax and Permit Lookup

This Python program imports data from two CSV files and inserts it into two tables in an SQLite database. 
The program also provides two lookup functions to query the database for information.

## Getting Started

### Prerequisites

- Python 3.x
- sqlite3 module
- csv module

### Installation

1. Clone the repository: `git clone https://github.com/mahshidhamidi/Tax_and_Permit_Lookup.git`
2. Navigate to the project directory: `cd Tax_and_Permit_Lookup`

### Usage

1. Make sure the CSV files (`tax.csv` and `permits.csv`) are in the project directory.
2. Run the program: `python app.py`
3. The program will insert the data from the CSV files into two tables in an SQLite database named `database.db`.
4. The program will then execute two lookup functions:
   - `lookup_permit_address(address, city)`: This function takes an address and city as input parameters and returns the company name and revenue associated with the corresponding business ID (bid) from the `companies` table.
   - `lookup_permits_by_company(company_name=None, bid=None)`: This function takes either a company name or a bid as an input parameter and returns all the addresses and cities associated with that company from the `permits` table.
