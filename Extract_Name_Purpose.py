# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from requests_html import HTMLSession
import pandas as pd

def Extract_Company_Name_Purpose(url, times):
    table = []
    session = HTMLSession()
    for j in range(times):  
        r = session.get(url)
        total_result = []
        for i in range(1,10):
            sel = 'body > ol > li:nth-child(' + str(i) +')'
            results = r.html.find(sel)
            if results == []:
                break;
            else:
                if 'Name' in results[0].text:
                    total_result.append((results[0].text)[6:])
                if 'Purpose' in results[0].text:
                    total_result.append((results[0].text)[9:])
        table.append(total_result)

    return(table)                

                    
df = pd.DataFrame(Extract_Company_Name_Purpose('http://3.95.249.159:8000/random_company', 50),
                  columns = ['Name','Purpose'])
print(df)
df.to_csv('A2_result.csv')