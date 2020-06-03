ad=open('a.txt')

for line in ad:
    if line.startswith("ETL"):
        print(line)