__author__ = 'jph'

with open('panini_data.txt') as f:
    data=f.readlines()

data=[x.split('\t') for x in data]
database={}

for player in data:
    database[int(player[1].replace("[","").replace("]",""))]={"country":player[2],"type":player[3],"value":player[4],
                                                              "rating":float(player[5].replace("(","").replace(")\n",""))}

try:
    with open('sticker.txt') as f:
        data=f.readlines()
except IOError:
    print "Error: No sticker.txt found in directory"
    exit()

output="\t".join(['Number','Country','Name','Value(max100)','Rating(max5)'])+"\n"

try:
    data.sort(key=lambda x:float(database[int(x.replace('\n',''))]['value']), reverse=True)
except KeyError:
    print "Incorrect number in data, could not sort..."

for number in data:
    try:
        output+="\t".join([number.replace("\n",""),database[int(number)]['country'],database[int(number)]['type'],
                           database[int(number)]['value'],str(database[int(number)]['rating'])])
        output+="\n"
    except KeyError:
        print "Number "+number+" not found"

try:
    with open('sticker_output.txt',"w") as f:
        f.write(output)
except IOError:
    print "Error: can't write to sticker_output.txt"
    exit()

print "done!"