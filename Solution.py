import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
# Default to the assignment URL if left blank
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Afifah.html'

count = input('Enter count: ')
if len(count) < 1:
    count = 7
else:
    count = int(count)

position = input('Enter position: ')
if len(position) < 1:
    position = 18
else:
    position = int(position)

print('Retrieving:', url)

# Loop 'count' times
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')

    # Find the link at the specified position (1-based index)
    # We subtract 1 because Python lists are 0-based
    tag = tags[position - 1]

    url = tag.get('href', None)
    name = tag.contents[0]  # The text of the link is usually the name

    print('Retrieving:', url)

print(f'The answer to the assignment for this execution is "{name}"')