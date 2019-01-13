def modifyURL(all_data):
    '''
    this function removes the \n at the end of the url
    '''
    for row in all_data:
        row['url'] = row['url'][:-1]
