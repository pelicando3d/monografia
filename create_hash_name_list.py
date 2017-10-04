import urllib2
import os
import re
import time
import csv

dir_home = "F:/Users/Victor/Documents/@DOCUMENTOS/ufmg/2017-2/Monografia/"
app_id = "730"
dir_data = dir_home + "data/"
dir_page = dir_data + app_id + "/"
page_id = "1"
file_name = "page" + page_id + ".txt"

DAT = dir_home + "listHashFormated.dat"
DAT2 = dir_home + "listHashNames.dat"
fw = open(DAT, "w")
fw.write("Name" + ";" + "ATR1" + ";" + "ATR2" +
         ";" + "ATR3" + ";" + "ATR4" + "\n")
fw2 = open(DAT2, "w")
fw2.write("Hash-name: " + "\n")

for page in range(1,940):
    page_file = "page" + str(page) + ".txt"
    FILE = dir_page + page_file
    a = open(FILE)
    arq = a.readlines()
    for line in arq:

        res = re.search(
            r'<a class="market_listing_row_link" href="http://steamcommunity.com/market/listings/730/(.+)" id', line)
        if (res != None):
            hash_name = res.group(1)
            fw2.write(str(hash_name)+ "\n")
            #print(hash_name)
            hashSplited = res.group(1).split('%')
            hashAux = hashSplited
            for field in hashSplited:
                if field == '7C':
                    hashAux.remove('7C')
            hashSplited = hashAux
            for field in hashSplited:
                if field == '29' :
                    hashAux.remove('29')
            hashSplited = hashAux
            for field in hashSplited:
                if field == '20' :
                    hashAux.remove('20')
            hashSplited = hashAux
            print hashSplited
            # year = res.group(3)
            # year_num = int(year)
            # ly.extend([year_num])
            if (len(hashSplited) == 3):
                 fw.write(str(hashSplited[0]) + ";" +
                          hashSplited[1] + ";" + hashSplited[2] +
                          "\n")

            if (len(hashSplited) == 4):
                 fw.write(str(hashSplited[0]) + ";" +
                          hashSplited[1] + ";" + hashSplited[2] + ";" +
                          hashSplited[3] + "\n")

            if (len(hashSplited) == 5):
                 fw.write(str(hashSplited[0]) + ";" +
                          hashSplited[1] + ";" + hashSplited[2] + ";" +
                          hashSplited[3] + ";" + hashSplited[4] + "\n")

            if (len(hashSplited) >= 6):
                 fw.write(str(hashSplited[0]) + ";" +
                          hashSplited[1] + ";" + hashSplited[2] + ";" +
                          hashSplited[3] + ";" + hashSplited[4] + ";" +
                          hashSplited[5] + "\n")
    a.close()
fw.close()
fw2.close()
# while(len(ly) > len(lp)):
#         lp.extend([""])

#     for i in range(0,len(lt)):
#         a = ly[i]
#     b = lt[i]
#     c = lp[i]

#     tupla.extend([(a,b,c)])

# fw = open(DAT, "w")
# fw.write("yr" + ";" + "win" + ";" + "mvp" + "\n")
# for reg in tupla:
#     fw.write(str(reg[0]) + ";" + reg[1] + ";" + reg[2] + "\n")
# fw.close()
# ------------------------------------------------------------------
