import ast


def modifyQuotationMarks(all_data):
    '''
    this function modifies the format of some fields so that the values can be written
    in the csv file in one single cell, by replacing all "" with ''
    '''
    for row in all_data:
        row['description'] = "\"" + \
            row['description'].replace("\"", "\'") + "\""

        related_talks = str(ast.literal_eval(
            row['related_talks'])).replace("\"", "\'")
        row['related_talks'] = "\"" + related_talks + "\""

        tags = str(ast.literal_eval(
            row['tags'])).replace("\"", "\'")
        row['tags'] = "\"" + tags + "\""

        row['name'] = "\"" + \
            row['name'].replace("\"", "\'") + "\""

        row['speaker_occupation'] = "\"" + \
            row['speaker_occupation'].replace("\"", "\'") + "\""

        row['title'] = "\"" + \
            row['title'].replace("\"", "\'") + "\""
