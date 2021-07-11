#Author: Dylan Hansen
#Date: 07/11/21
#This is a fun script to learn about APIs

#Import all needed libraries
import csv
import JSON
import requests
#URL-based API Call
api_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId="+(ChannelId)+"&key=<placeholderforyourAPIkey>"
api_response = requests.get(api_url)
videos = json.loads(api_response.text)


#Open the URL and read the API response
with open("youtube_videos.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_wrtier.writerow(["publishedAt",
                            "Title",
                            "description",
                            "thumbnailurl"])
#Identify each data point in your JSON and print it to a spreadsheet
    if videos.get("items") is not None:
        for video in videos.get("items"):
            video_data_row = [
                        video["snippet"]["publishedAt"],
                        video["snippet"]["title"],
                        video["snippet"]["description"],
                        video["snippet"]["thumbnails"]["default"]["url"]
                        ]
                csv_writer.writerow(video_data_row)
