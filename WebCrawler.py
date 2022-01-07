import requests
from bs4 import BeautifulSoup

towson_url = 'https://www.towson.edu/fcsm/departments/computerinfosci/facultystaff/'

#creates the soup from the HTML
def soup_chef(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    new_soup = BeautifulSoup(plain_text, features='html.parser')
    return new_soup


info_soup = soup_chef(towson_url) # call to soup chef
info_list = []# list for all info
names = []# list for just the names
prev = ''#holds the previous string; used to destinguish names from ancillary data


# loads info_list from info_soup and prints each element
for info in info_soup.findAll('td'):
    info = str(info.text)
    info_list += info.split('\n')
    print(info)


# loads the first name into names
names += info_list[1].split('\n')

# every name that belongs to a professor is preceded by a room number from the previous entry
# Other staff are not preceded by room numbers so only professors' names are loaded into the array
for i in info_list:
    if i == '':
        del i
        continue
    elif 'YR-' in prev:
        names += i.split('\n')
    prev = i
names = names[:-1]


for name in names:
    # modify this 'S' to the first letter of your last name
    # the list includes more than just professors, so not all names get tested against your name
    if name[0] == 'S':
        print(f'{name} has the same first letter of my last name! {name[0]}!')



