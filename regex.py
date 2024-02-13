import re

names = ["Finn Bindemballe",
         "Geir Andres Berge",
         "HappyCordingRobot",
         "Ron Cromberge",
         "Sohil"]

#Find people with first name and last mname only

regex ='^\w+\s+\w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(result)