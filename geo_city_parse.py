#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import requests
import xml.etree.ElementTree as ET

txt = open('input.txt', 'r').read().split('\n')
i = 0;

for line in txt:
    i += 1
    lp, region, district, municipality, city, lat, lon = line.split('\t')
    baseUrl = 'http://nominatim.openstreetmap.org/search/pl/'+region+'/'+district+'/'+municipality+'/'+city+'/?format=xml'
    resp = requests.get(baseUrl)
    msg = resp.content
    tree = ET.fromstring(msg)
    for place in tree.findall('place'):
        location = '{:5f}\t{:5f}'.format(
            float(place.get('lat')),
            float(place.get('lon')))

    f = open('result.txt', 'a')
    f.write(location+'\t'+region+'\t'+district+'\t'+municipality+'\t'+city+'\n')
    f.close()

g = open('stats.txt', 'a')
g.write(('value of "i" is: ')+str(i))
g.close()
