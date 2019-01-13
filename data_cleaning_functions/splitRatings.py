import csv
import ast


def find_all_rating_attr(all_data):
    '''
    find all the rating attributes 
    => it is found that all talks have the same rating attr
    this function thus serves for future checking if needed
    '''
    all_rating_attr = []
    for row in all_data:
        talk_ratings = ast.literal_eval(row['ratings'])
        for indiv_rating in talk_ratings:
            if indiv_rating['name'] not in all_rating_attr:
                all_rating_attr.append(indiv_rating['name'])
    return all_rating_attr


def splitRatings(all_data):

    all_rating_attr = []
    for row in all_data:
        talk_ratings = ast.literal_eval(row['ratings'])
        for indiv_rating in talk_ratings:
            row[indiv_rating['name']] = indiv_rating['count']
        del row['ratings']
