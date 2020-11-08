import csv
from datetime import datetime
from datetime import timedelta
from datetime import date
import sys

#import file that sends texts
sys.path.append(r"C:\Users\jzhao\OneDrive\Desktop\Web\SMS")
import sendText as sT

def isBirthday(birthday):
    now = datetime.now()
    if now == birthday:
        return True
    else:
        return False

def main():
    year = datetime.now().year

    with open ("people.csv", "r" ) as people:
        reader = csv.reader(people, delimiter ="\t")
        next(reader)
        for row in reader:
            birthday = date(int(year), int(row[1]) , int(row[2]))
            
            if isBirthday(birthday):
                sT.sendText(f"Today is {row[0]}'s birthday!")
                print(f"Today is {row[0]}'s birthday")
            else:
                print(f"Today is not {row[0]}'s birthday")
            

    people.close()

main()