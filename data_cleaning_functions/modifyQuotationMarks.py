import ast


def modifyQuotationMarks(all_data):
    '''
    this function modifies the format of description, related_talks and tags so that the values can be written
    in the csv file in one single cell
    '''
    for row in all_data:
        row['description'] = "\"" + row['description'] + "\""

        related_talks = str(ast.literal_eval(
            row['related_talks'])).replace("\"", "\'")
        row['related_talks'] = "\"" + related_talks + "\""

        tags = str(ast.literal_eval(
            row['tags'])).replace("\"", "\'")
        row['tags'] = "\"" + tags + "\""
