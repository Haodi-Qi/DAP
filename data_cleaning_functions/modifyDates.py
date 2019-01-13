from datetime import datetime, date


def modifyDates(all_data):
    '''
    convert unix timestamp for film_date and published_date into DD-MM-YYYY format
    add a new field of date_diff in days btw the two dates
    '''
    for row in all_data:
        unix_film_date = int(row['film_date'])
        unix_published_date = int(row['published_date'])
        converted_film_date = datetime.fromtimestamp(
            unix_film_date).strftime("%d-%m-%Y")
        converted_published_date = datetime.fromtimestamp(
            unix_published_date).strftime("%d-%m-%Y")

        row['film_date'] = converted_film_date
        row['published_date'] = converted_published_date

        diff = str((datetime.fromtimestamp(unix_published_date) -
                    datetime.fromtimestamp(unix_film_date)).days)
        row['date_diff'] = diff
