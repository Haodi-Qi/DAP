import ast


def appendTagNum(all_data):
    '''
    add a new field of tag_num
    '''
    for row in all_data:
        tags = ast.literal_eval(row['tags'])
        row['tag_num'] = len(tags)
