import csv
import ast


def appendTalkID(all_data):
    '''
    add a new field of talk_id
    '''
    count = 1
    for row in all_data:
        row['talk_id'] = str(count)
        row.move_to_end('talk_id', last=False)  # move talk_id to the first col
        count += 1


def findMedianNum(num_list):
    length = len(num_list)
    if length % 2 == 1:
        return num_list[length // 2]
    else:
        median = (num_list[length//2] + num_list[length//2-1])//2
        return median


def calAdjustedAvg(num_list):
    '''
    adjusted avg is the average after removal of the largest and smallest value
    '''
    adjusted_list = num_list.copy()
    adjusted_list.sort()
    length = len(num_list)
    if length >= 3:
        adjusted_list = adjusted_list[1:-1]
        length -= 2
    return round(sum(adjusted_list)/length, 3)


def createTagDict(all_data):
    '''
    the function first creates a dictionary, tag_dict {"tag":(view_list,talk_list)}
    '''
    tag_dict = {}

    for row in all_data:
        tags = ast.literal_eval(row['tags'])
        for tag in tags:
            if tag in tag_dict:
                tag_dict[tag][0].append(row['talk_id'])
                tag_dict[tag][1].append(int(row['views']))
            else:
                tag_dict[tag] = ([row['talk_id']], [
                    int(row['views'])])
    return tag_dict


with open('data_test.csv', 'r', encoding='utf-8') as csvfile:
    all_data = list(csv.DictReader(csvfile))
    appendTalkID(all_data)
    tag_dict = createTagDict(all_data)

with open('tag_file.csv', 'w', encoding='utf-8') as file:
    '''
    the csv file is with the following heading:
    tag | talk num | avg view | adjusted avg view | median view | talk list |
    '''
    header = "tag,talk_num,avg_view,adj_avg,median_view,talk_list\n"
    file.write(header)

    for tag in tag_dict:
        lists = tag_dict[tag]
        length = len(lists[0])
        view_sum = sum(lists[1])
        data = tag + "," + str(length) + "," + \
            str(round(view_sum/length, 3)) + "," + \
            str(calAdjustedAvg(lists[1])) + "," + \
            str(findMedianNum(lists[1])) + \
            ",\"[" + ",".join(lists[0]) + "]\"\n"
        file.write(data)
