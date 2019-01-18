import csv
import time
import data_cleaning_functions as f
from data_cleaning_functions.appendID import appendTalkID
from data_cleaning_functions.appendTitleType import appendTitleType
from data_cleaning_functions.modifyDates import modifyDates
from data_cleaning_functions.modifyURL import modifyURL
from data_cleaning_functions.splitRatings import splitRatings
from data_cleaning_functions.modifyQuotationMarks import modifyQuotationMarks
from data_cleaning_functions.appendTagNum import appendTagNum
from data_cleaning_functions.appendRelatedTalksNum import appendRelatedTalksNum


with open('data_test.csv', 'r', encoding='utf-8') as csvfile:
    lines = csv.DictReader(csvfile)
    all_data = list(lines)

    appendRelatedTalksNum(all_data)
    appendTagNum(all_data)
    modifyQuotationMarks(all_data)
    appendTalkID(all_data)
    appendTitleType(all_data)
    modifyDates(all_data)
    modifyURL(all_data)
    splitRatings(all_data)


with open('processed_data.csv', 'w', encoding='utf-8') as updatedFile:
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

# #convert csv to xlsx workbook
#from openpyxl import Workbook
# wb =Workbook()
# ws = wb.active
# with open('processed_data.csv', 'r',encoding='utf-8') as f:
#     for row in csv.reader(f):
#         ws.append(row)
# wb.save('processed_data.xlsx')