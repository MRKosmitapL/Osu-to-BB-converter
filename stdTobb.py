from itertools import count
from osupyparser import OsuFile
import configparser
import json

class Note():
    def __init__(self, input_type, note_modifier,  timestamp:float):
        self.input_type = input_type
        self.note_modifier = note_modifier
        self.timestamp = timestamp
        
    def returnType(self):
        return self.input_type
    def returnTime(self):
        return self.timestamp


if __name__ == "__main__":
    data = OsuFile("osuFile.osu").parse_file()
    prevTimeStamp = -1
    listOfNotes = [] 
    info = data.__dict__
    userInput = input("Do you want to count edges of sliders: (y/n)")
    for elem in data.hit_objects: #read osu content and parse hitObjects/timestamps to BB format
        if elem.__class__.__name__ == "Slider":
            if userInput == "y" or userInput == "Y":
                elemDict = elem.__dict__
                edges = len(list(elemDict["edges"]))
                dur = int(elemDict["duration"])
                for i in range(0, edges):
                    listOfNotes.append(Note(input_type=0,note_modifier=0, timestamp=float(elem.start_time + dur*i)/1000))
            elif userInput == "n" or userInput == "N":
                listOfNotes.append(Note(input_type=0,note_modifier=0, timestamp=float(elem.start_time)/1000))
        elif elem.__class__.__name__ == "Circle":
            listOfNotes.append(Note(input_type=1,note_modifier=0, timestamp=float(elem.start_time)/1000))
        
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