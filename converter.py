from osupyparser import OsuFile
import configparser
import json

class Note():
    def __init__(self, input_type, note_modifier,  timestamp:float):
        self.input_type = input_type
        self.note_modifier = note_modifier
        self. timestamp = timestamp
        
    def returnType(self):
        return self.input_type
    def returnTime(self):
        return self.timestamp


if __name__ == "__main__":
    data = OsuFile("osuFile.osu").parse_file()
    prevTimeStamp = -1
    listOfNotes = [] 
    for elem in data.hit_objects: #read osu content and parse hitObjects/timestamps to BB format
        if(elem.start_time == prevTimeStamp): #ignore notes appearing on the same time
            continue
        
        typeN = None
        if elem.pos.x  == 64:
            typeN = 0
        elif elem.pos.x == 192:
            typeN = 1
        elif elem.pos.x == 320:
            typeN = 2
        elif elem.pos.x == 448:
            typeN = 3
        
        prevTimeStamp = elem.start_time
        listOfNotes.append(Note(input_type=typeN,note_modifier=0, timestamp=float(elem.start_time)/1000))
        
    #create notes.cfg and write to it
    structure = {
        'charts':[{
            "name": "Normal",
            "notes": [ob.__dict__ for ob in listOfNotes],
            "rating": 1
        }]
    }
    dataFinal = json.dumps(structure)
    config = configparser.ConfigParser()
    config["main"] = {"data":dataFinal}
    with open('notes.cfg', 'w') as configfile:
        config.write(configfile)
    print("Converted!")