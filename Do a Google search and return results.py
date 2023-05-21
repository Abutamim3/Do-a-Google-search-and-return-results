'''Do a Google search and return results'''
# you may need to first "pip install google"
#https://github.com/Abutamim3
#Developed by Abdul Rahman Al-Harbi


import webbrowser
from googlesearch import search

QUERY = " اغنية تفائل بالخير"

#change tld to "co.uk" or whatever,num=results to get
for RESULTS in search(QUERY, tld="co.uk", num=10, stop=4, pause=4):
    print(RESULTS)
webbrowser.open(RESULTS)

print("Developed by Abdul Rahman Al-Harbi")