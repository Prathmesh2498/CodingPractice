# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:57:00 2020

@author: Admin
"""

from bs4 import BeautifulSoup as bs
import requests
import time

def check_page():
    #Get website info
    #.text is used to remove tags
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)
    
    soup = bs(html_text, 'lxml') 
    #print(soup.prettify)                        
    
    
    #It's a good idea to get only one element first when you are figuring out the structure.
    job = jobs = soup.find('li', class_='clearfix job-bx wht-shd-bx')
    
    #.replace to remove unecessary spaces
    company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ', '')
    print(company_name)
    
    skills = job.find('span', class_=('srp-skills')).text
    print(skills)
    
    #'.span.text' because of nested spans
    pub_date = job.find('span', class_='sim-posted').span.text
    print(pub_date)



def get_JobDetails():
    
    #Get website info
    #.text is used to remove tags
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)
    
    soup = bs(html_text, 'lxml') 
    #print(soup.prettify)   
    
    def printData(l):
        for i in l:
            print(f'Company name: {i[0]}')
            print(f'Skills: {i[1]}')
            print(f'Published: {i[2]}')
            print(f'Link: {i[3]}')
    
    #Now get all elements and repeat for each element.
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    print(jobs)
    l = []
    for job in jobs:
        #.replace to remove unecessary spaces
        company_name = job.find('h3', class_= 'joblist-comp-name').text.strip()
        
        #Get skills
        skills = job.find('span', class_=('srp-skills')).text.strip()
        
        #Get Link
        link  = job.header.h2.a['href']
        
        #'.span.text' because of nested spans
        pub_date = job.find('span', class_='sim-posted').span.text
        if 'few' in pub_date:
            l.append([company_name, skills, pub_date, link])
    
    print(l)
    print()

if __name__ == '__main__':
   while True:
       get_JobDetails()
       wait_time = 10
       time.sleep(10 * 60)
       print(f'Waiting 10 minutes....\n')

    
    
    