#!/usr/bin/env python
from lxml import html
import cfscrape
import re
import cgi
import sys

print "Content-Type: text/html\n\n"
form = cgi.FieldStorage()
if form.getvalue('statustext'):
    textContent = form.getvalue('statustext')
else:
    print 'no text submitted'
    sys.exit('No text submitted!')

p = re.compile('[0-5]:[01]:\d+')
steamids = p.findall(textContent)

scraper = cfscrape.CloudflareScraper()
for steamid in steamids:
    payload = {'s': 'search', 'query': steamid, 'source': 'users', 'fields[unique_ids]': '1'}
    r = scraper.get('https://play.esea.net/index.php', params=payload)

    tree = html.fromstring(r.content)
    results = tree.xpath('//a[@class="result"]')
    for result in results:
        userInfo = result.xpath('@href | text()')
        print 'SteamID: ' + steamid + '</br>'
        print 'Name: ' + userInfo[1] + '</br>'
        linkDomainStart = '"https://play.esea.net' + userInfo[0]
        linkDomainEnd = '">https://play.esea.net' + userInfo[0]
        print 'Profile: <a href=' + linkDomainStart + linkDomainEnd + '</a></br></br>'
