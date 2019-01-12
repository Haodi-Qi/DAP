import datetime
with open("ted_edit.csv","r",encoding="utf8") as data:
    with open("clean_data.csv","w") as newdata: 
            newdata.write("ID,Film_Date,Published_Date,Tags_Count\n")
            counter = 0
            data.readline()
            for i in data:
                newi = i.split(",")
                newi2 = i.split("[")
                # print(newi[3],counter)
                film_date = int(newi[3])
                published_date = int(newi[8])
                tags = newi2[1].split("]")[0]
                counter += 1
                newfdate = str(datetime.datetime.fromtimestamp(film_date).strftime('%d-%m-%Y'))
                newpdate = str(datetime.datetime.fromtimestamp(published_date).strftime('%d-%m-%Y'))
                numtag = str(tags.count(",")+1)
                tags = "["+tags+"]"
                output = str(counter)+","+newfdate+',' + newpdate+','+numtag + "\n"
                newdata.write(output)
    

