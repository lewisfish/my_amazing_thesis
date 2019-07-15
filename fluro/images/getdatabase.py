import re
import urllib.request

print('Beginning file download with urllib2...')

regex = r"[a-z]{1,18}_eem\.txt#[A-Z]{1,20}\(?-?[A-Z]{1,20}\)?[a-z]{1,20}\ ?[a-z]{1,20}\ \[\d\]"

f = open("database.html", "r")
lines = f.readlines()
lines = lines[-2]

matches = re.finditer(regex, lines, re.MULTILINE | re.IGNORECASE)
string = "http://eemdb.uhnres.utoronto.ca/cgi-bin//WebObjects/WebFluor.woa/WebServerResources/"

for matchNum, match in enumerate(matches, start=1):
    string = "http://eemdb.uhnres.utoronto.ca/WebObjects/WebFluor.woa/WebServerResources/"
    string += match.group()
    url = string
    name, mid, tail = url.partition("#")
    print(url)
    url = string
    urllib.request.urlretrieve(url, name[75:])
