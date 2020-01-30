import pandas as pd
import json
import sys,io
import os
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

path_to_ted_aws_dataset = "./aws_ted_dataset/"

path_to_ted_video = "./videos/"

if not os.path.isdir(path_to_ted_video):
    os.mkdir(path_to_ted_video)

all_ted_talks = os.listdir(path_to_ted_aws_dataset)

for ted_talk in all_ted_talks:
    if ted_talk.endswith(".json"):
        ted_name = ted_talk.split(".")[0]
        ted_talk_full_path = os.path.join(path_to_ted_aws_dataset,ted_talk)
        with open(ted_talk_full_path,"r") as f:
            ted_meta = json.load(f)
        video_allJson = json.loads(ted_meta["alldata_JSON"])
        video_download_links = video_allJson["talks"][0]["downloads"]["nativeDownloads"]
        if not video_download_links == None:
            # print(video_download_links)
            res = video_download_links.keys()
            if "high" in res:
                video_download_link = video_download_links["high"]
            elif "medium" in res:
                video_download_link = video_download_links["medium"]
            elif "low" in res:
                video_download_link = video_download_links["low"]
            video_path = os.path.join(path_to_ted_video,ted_name+".mp4")
            if not video_download_link==None:
                print("downloading: {}".format(ted_name))
                urllib.request.urlretrieve(video_download_link, filename = video_path)
            exit()

