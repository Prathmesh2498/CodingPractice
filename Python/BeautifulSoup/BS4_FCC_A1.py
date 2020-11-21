# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:28:26 2020

@author: PD

FCC - Beautiful Soup
"""

from bs4 import BeautifulSoup as bs


with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = bs(content, 'lxml')
    #Print file in a readable way
    #print(soup.prettify())
    
    #Get specific tags
    tags = soup.find_all('h5')
    #print(tags)
    
    #Get all text in the tags
    l = []
    for s in tags:
        l.append(s.text)
    print(l)
    
    #Find all prices
    #'_' after class because class is keyword in python
    course_cards = soup.find_all('div', class_ = 'card')
    print(course_cards)
    
    d = {}
    for c in course_cards:
        d[c.h5.text] = c.a.text.split()[-1]#Split at space and get last element 
    
    for i in d.keys():
        print('{} -> {}'.format(i,d[i]))
        