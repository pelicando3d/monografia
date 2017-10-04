
import urllib2, os, re, time, csv

from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
from bs4 import BeautifulSoup

def create_directory(dir_name):    
    if not os.path.isdir(dir_name):
        print "Creating directory:"
        print "\t" + dir_name
        
        os.mkdir(dir_name)        
        print "Directory created.\n"

def download_page(url):
    print "Downloading page:"
    print "\t" + url
    
    hdr = {'User-Agent': 'your bot 0.1',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'close'}
    
    request = urllib2.Request(url, headers=hdr)
    socket = urllib2.urlopen(request)
    data = socket.read()
    socket.close()
    
    print "Page downloaded.\n"
    return data

#verifica se o xml existe
def xml_exist(dir_name, filename):
    name = dir_name + filename
    return os.path.exists(name)

#grava o o arquivo baixado
def save_xml(data, dir_name, filename):
    file_name = dir_name + filename
    
    print "Saving XML file:"
    print "\t" + file_name
    
    f = open(file_name, "w")
    f.write(data)
    f.close()
    
    print "File saved.\n"

#Aqui estao as funcoes relacionadas ao parser do HTML
class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text
page = "1"
app_id = "730"
url_home = "http://steamcommunity.com/market/search?appid="
dir_home = "F:/Users/Victor/Documents/@DOCUMENTOS/ufmg/2017-2/Monografia/"
dir_data = dir_home + "data/"
dir_game = dir_data + app_id + "/"

create_directory(dir_data)
create_directory(dir_game)

#-------------------------------------------------------------------
# Baixar todas as paginas de itens
for p in range(788,940):
    page = str(p)
    url_game = url_home + app_id + "#p"+ page + "_popular_desc"
    file_name = "page" + page + ".txt"
    if not (xml_exist(dir_game, file_name)):
        data = download_page(url_game)
        save_xml(data, dir_game, file_name)

