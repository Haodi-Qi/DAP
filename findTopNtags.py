import ast
import csv


def DistinctTagsNum(all_data):
    distTags = set()
    for row in all_data:
        tags = ast.literal_eval(row['tags'])
        for tag in tags:
            distTags.add(tag)
    return len(distTags)
# total number of dist tags = 416

def topNTags(all_data, n):
    '''
    this function first creates a dictionary of tag:number of talks with the tag
    then convert the dict to a list of tuples of (tag,talk number)
    return the top n tags with the most number of talks
    '''
    tag_talk_dict = {}
    for row in all_data:
        tags = ast.literal_eval(row['tags'])
        for tag in tags:
            if tag in tag_talk_dict:
                tag_talk_dict[tag] += 1
            else:
                tag_talk_dict[tag] = 1
    # a list of tuples (tag,no of talks with the tag)
    tag_talk_list = list(tag_talk_dict.items())
    tag_talk_list.sort(key=lambda x: x[1], reverse=True)
    return tag_talk_list[:n]


with open('data_test.csv', 'r', encoding='utf-8') as csvfile:
    all_data = list(csv.DictReader(csvfile))
#     print(DistinctTagsNum(all_data))
    print(topNTags(all_data, 10))
