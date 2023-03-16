from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from urllib.request import urlopen as url_opan
import numpy as np
import logging
import os
import re
import csv




query = 'PW-Foundation'
headers ={"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
respose = requests.get(f'https://www.youtube.com/@{query}/videos', headers=headers)
res=respose.text
# print(res)
filename = 'web_text.txt'
videoids = re.findall('"videoRenderer":{"videoId":".*?"', res)
# print(videoids)
# for videoid in videoids:
#     print(videoid.split('"'))
# thumbnail
thumbnails = re.findall('"thumbnail":{"thumbnails":\[{"url":".*?"', res)
# Title
titles = re.findall('"title":{"runs":\[{"text":".*?"', res)
# for title in titles:
#     print(title.split('"'))
# Views
views = re.findall('"shortViewCountText":{"accessibility":{"accessibilityData":{"label":".*?"', res)
# Published Time
published_times = re.findall('"publishedTimeText":{"simpleText":".*?"', res)


report_list = [
    ['S No', 'Video url', 'Thumbnail', 'Title', 'Views', 'Published Time']
 ]
for i in range(1):
    temp = []
    temp.append(i+1)
    temp.append('https://www.youtube.com/watch?v=' + videoids[i].split('"')[-2])
    temp.append(thumbnails[i].split('"')[-2])
    temp.append(titles[i].split('"')[-2])
    temp.append(views[i].split('"')[-2])
    temp.append(published_times[i].split('"')[-2])
    report_list.append(temp)
    print(temp)



# file_name = os.path.join(BASE_DIR, query+'.csv')
# with open(file_name, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     for row in report_list:
#         csvwriter.writerow(row)

# with open(filename, 'w',  encoding="utf-8") as txtfile:
#     data = txtfile.write(res)
# # print(data)
#     txtfile.close()





for i in range(1):
    temp2 = []
    temp2.append(i+1)
    temp2.append('https://www.youtube.com/watch?v=' + videoids[i].split('"')[-2])
    temp2.append(thumbnails[i].split('"')[-2])
    temp2.append(titles[i].split('"')[-2])
    temp2.append(views[i].split('"')[-2])
    temp2.append(published_times[i].split('"')[-2])
    report_list.append(temp2)
    print('temp2', temp2)