import requests
from bs4 import BeautifulSoup
import re  #regular expressons pattern matching
#from urllib.request import urlretrieve #downloading mp4
import sys #for argument parsing

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("error: please enter the ted talk url")

r = requests.get(url)
print("download about to start")

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.findAll("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split('"')[0]

print("downloading video from url "+ mp4_url)
file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]
print("storing video in ...." + file_name)

r = requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(r.content)

print("download process finished")
