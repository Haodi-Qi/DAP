import csv


def categorizeTitle(title):
    '''
    this function categorizes titles based on whether it is in the form of a question or statement
    titles in the form of questions start with 5W1H or Do/Does/Did/Have
    the function returns "question" or "statement" and the title in the standard format 
    (Captialize the first word and add ? for questions and . for statements)
    '''
    category = ""
    determinants = ['Who', 'What', 'When', 'Where',
                    'Why', 'How', 'Does', 'Do', 'Did', 'Have']
    title = title[1:-1].capitalize()

    if title.split()[0] in determinants:
        category = "question"
        if title[-1] != "?":
            title += "?"
    else:
        category = "statement"
        if title[-1] != ".":
            title += "."

    title = "\"" + title + "\""

    return category, title


def appendTitleType(all_data):
    '''
    use categorizeTitle function to format all titles
    and add a new field of title_type
    '''
    for row in all_data:
        category, talk_title = categorizeTitle(row['title'])
        row['title_type'] = category
        row['title'] = talk_title
