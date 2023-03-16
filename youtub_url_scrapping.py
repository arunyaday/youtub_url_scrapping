from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests
from urllib.request import urlopen as url_opan
import logging
import os
import re
import csv



base_dir=os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=os.path.join(base_dir,"scrapper.log"))


app=Flask(__name__)
print('----Scraping start----')
@app.route("/", methods = ['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")


@app.route("/review", methods=['GET','POST'])
@cross_origin()
def index():
    if request.method=='POST':
        try:
            query = request.form['content'].replace(" ","")
            headers ={"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
            respose = requests.get(f'https://www.youtube.com/@{query}/videos', headers=headers)
            res=respose.text
            # print(res)
            # fetch the search results page
            response = requests.get(f"https://www.youtube.com/@{query}/videos", headers=headers)
            res = response.text

            # Video
            videoids = re.findall('"videoRenderer":{"videoId":".*?"', res)
            # thumbnail
            thumbnails = re.findall('"thumbnail":{"thumbnails":\[{"url":".*?"', res)
            # Title
            titles = re.findall('"title":{"runs":\[{"text":".*?"', res)
            # Views
            views = re.findall('"shortViewCountText":{"accessibility":{"accessibilityData":{"label":".*?"', res)
            # Published Time
            published_time = re.findall('"publishedTimeText":{"simpleText":".*?"', res)


            info_list = [
                ['Sr_No','Video_url', 'Thumbnail', 'Title', 'Views', 'Published_Time' ]
            ]
            for i in range(6):
                temp_list=[]
                temp_list.append(i+1)
                temp_list.append('https://www.youtube.com/watch?v=' + videoids[i].split('"')[-2])
                temp_list.append(thumbnails[i].split('"')[-2])
                temp_list.append(titles[i].split('"')[-2])
                temp_list.append(views[i].split('"')[-2])
                temp_list.append(published_time[i].split('"')[-2])
                info_list.append(temp_list)
            file_name = os.path.join(base_dir, query+'.csv')
            with open(file_name, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                for row in info_list:
                    csvwriter.writerow(row)
            return render_template('result.html', report_list=info_list, channel=query)
        except Exception as e:
            logging.info(e)
            return "Something wrong"
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)