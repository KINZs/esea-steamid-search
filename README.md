# esea-steamid-search

This script allows one to submit pasted output of the 'status' console command in CS:GO to see if any of the players in your game are also ESEA members. Positive search results include the player(s) name and a link to their ESEA profile.

The script uses the simple form from [index.htm](https://github.com/dephekt/esea-steamid-search/blob/master/index.htm) to take pastes of SteamIDs. The form then submits the pasted input to [searchunique.py](https://github.com/dephekt/esea-steamid-search/blob/master/searchunique.py) for processing.

After using a regular expression to parse out individual SteamIDs from the input, the script relies on [cfscrape](https://github.com/Anorov/cloudflare-scrape) to defeat Cloudflare's DDoS protection on the ESEA website. Once a session has been established through Cloudflare, which takes about five seconds, the script reuses this valid session to send HTTP GET requests for each SteamID to ESEAs website. Any players found are shown on a new page, including their profile name on ESEA and a link to their profile.

### Dependencies
Running the script on a web server requires the following dependencies be installed:
* [cloudflare-scrape](https://github.com/Anorov/cloudflare-scrape)
* [Nodejs](https://nodejs.org/en/) (required for cloudflare-scrape)
* [requests](http://docs.python-requests.org/en/master/) python 2.7 module (required for cloudflare-scrape)
* [Lxml](http://lxml.de/installation.html) python bindings to libxml2 & libxslt
* [Python CGI](https://docs.python.org/2/library/cgi.html) module
* [re](https://docs.python.org/2/library/re.html) the python regular expression module
* A web server of your choice. This was tested with Apache2 on Ubuntu 16.04 LTS.
