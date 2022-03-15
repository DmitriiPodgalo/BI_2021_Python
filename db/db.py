import pandas as pd
import sqlite3

genstudio = pd.read_csv('genstudio.csv', index_col=0, low_memory=False)
metadata = pd.read_csv('metadata.csv', index_col=0)

connection = sqlite3.connect('dna.db')

genstudio.head()

metadata.head()

# Position (dtype == object) --> Position (dtype == int)

genstudio = genstudio[genstudio['Position'].str.contains('-') == False]
genstudio['Position'] = pd.to_numeric(genstudio['Position'])

query1 = '''CREATE TABLE IF NOT EXISTS dna_snps(
                                id INTEGER PRIMARY KEY,
                                dna_id TEXT,
                                SNP TEXT,
                                SNP_name TEXT,
                                Position INTEGER,
                                GC_score INTEGER
                                )'''

query2 = '''CREATE TABLE IF NOT EXISTS dna_char(
                                id INTEGER PRIMARY KEY,
                                dna_id TEXT,
                                breed TEXT,
                                sex TEXT
                                )'''

connection.execute(query1)
connection.execute(query2)

insertion_query1 = f'''INSERT INTO
                      dna_snps(dna_id, SNP, SNP_name, Position, GC_score)
                      VALUES (?, ?, ?, ?, ?)'''

insertion_query2 = f'''INSERT INTO
                      dna_char(dna_id, breed, sex)
                      VALUES (?, ?, ?)'''

info1 = genstudio[['Sample ID', 'SNP', 'SNP Name', 'Position', 'GC Score']].values.tolist()
connection.executemany(insertion_query1, info1)

info2 = metadata[['dna_chip_id', 'breed', 'sex']].values.tolist()
connection.executemany(insertion_query2, info2)

connection.commit()

select_query = '''
                SELECT dna_id, SNP
                FROM dna_snps'''
result = connection.execute(select_query).fetchall()

for dna in result[:10]:
    print(*dna)

select_query = '''
                SELECT dna_id, sex
                FROM dna_char'''
result = connection.execute(select_query).fetchall()

for dna in result[:10]:
    print(*dna)

cursor = connection.cursor()
query_join = '''
                SELECT * FROM dna_snps
                JOIN dna_char USING(dna_id)'''
cursor.execute(query_join)

result = cursor.fetchall()
for row in result[:10]:
    print(*row)
