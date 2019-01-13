import ast


def appendRelatedTalksNum(all_data):
    '''
    add a new field of related_talks_num
    '''
    for row in all_data:
        related_talks = ast.literal_eval(row['related_talks'])
        row['related_talks_num'] = len(related_talks)
