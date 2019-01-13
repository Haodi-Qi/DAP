import csv
from appendID import appendTalkID
from appendTitleType import appendTitleType
from modifyDates import modifyDates
from modifyURL import modifyURL
from splitRatings import splitRatings
from modifyQuotationMarks import modifyQuotationMarks
from appendTagNum import appendTagNum

with open('../ted_main.csv', 'r', encoding='utf8') as csvfile:
    lines = csv.DictReader(csvfile)
    all_data = list(lines)

    appendTalkID(all_data)
    appendTitleType(all_data)
    appendTagNum(all_data)
    modifyQuotationMarks(all_data)
    modifyDates(all_data)
    modifyURL(all_data)
    splitRatings(all_data)

with open('../processed_data.csv', 'w') as updatedFile:
    write_header = False
    for row in all_data:
        if not write_header:
            header = ",".join(row.keys()) + "\n"
            updatedFile.write(header)
            write_header = True

        data = ""
        for value in row.values():
            data += str(value) + ','
        data = data[:-1] + "\n"
        updatedFile.write(data)
