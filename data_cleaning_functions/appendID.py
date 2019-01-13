def appendTalkID(all_data):
    '''
    add a new field of talk_id 
    '''
    count = 1
    for row in all_data:
        row['talk_id'] = str(count)
        row.move_to_end('talk_id', last=False)  # move talk_id to the first col
        count += 1
