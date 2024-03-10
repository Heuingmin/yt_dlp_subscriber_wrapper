import json
import math
import multiprocessing
import time
import win11toast
import requests_constants as CONSTANTS
import requests

from win11toast import toast
from parsel import Selector
from io import StringIO
import yt_dlp
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
base_url = "https://www.nicovideo.jp/watch/"
# path = "D:\\Media\\Music\\术COLLE\\"

#todo:下载器配置；url字串下载导入；基于列表自裂解实现的多进程；研究一下多线程的可行性；统计信息和下载行为分离避免爬取低质量视频以及重复爬取
# （最好实现物理上的分离，也即避免线性运行互相阻塞）
#todo
def search_result_resolve(type, content, sort, order , path):
    if not judge_if_premier_only(path):
        toast("当前时段会员专属，请换一个时间段")
        return
    url = fr"https://www.nicovideo.jp/{type}/{content}?sort={sort}&order={order}"
    first_response = requests.get(url, headers=CONSTANTS.header)
    first_response_selector = Selector(first_response.text)
    num_item = first_response_selector.xpath('//*[@class="num"]')
    item_nums_str = num_item.xpath('.//text()').get()
    item_nums = int(item_nums_str.replace(',', ''))

    pages_num = math.ceil(item_nums / 32) + 1

    video_address_list = []

    # todo:将具体元素获取整理成多进程提高速度
    # for i in range(1, 2):
    #     if i != 1:
    #         url = fr"https://www.nicovideo.jp/{type}/{content}?page={i}&sort={sort}&order={order}"
    #     response = requests.get(url, headers=CONSTANTS.header)
    #     response_selector = Selector(response.text)
    #     video_items_list = response_selector.xpath('//@data-video-id')
    #     # for video_item in video_items_list:
    #     #     video_address_list.append(base_url+video_item.get())
    #     video_address_list.extend(video_items_list.getall())
    #     time.sleep(0.4)
    # video_address_list = list(map(lambda x: base_url + x, video_address_list))#这里应该可以直接append，对每个列表做map，实现按页爬取
    # # print(video_address_list)
    # audio_download_for_multiprocessing(video_address_list, path)
    for i in range(1, pages_num):
        if i != 1:
            url = fr"https://www.nicovideo.jp/{type}/{content}?page={i}&sort={sort}&order={order}"
        response = requests.get(url, headers=CONSTANTS.header)
        response_selector = Selector(response.text)
        video_items_list = response_selector.xpath('//@data-video-id')
        for video_item in video_items_list:
            video_address_list.append(base_url+video_item.get())
        # video_address_list.append(list(map(lambda x: base_url + x,video_items_list.getall())))
        time.sleep(0.4)
    # video_address_list = list(map(lambda x: base_url + x, video_address_list))#这里应该可以直接append，对每个列表做map，实现按页爬取
    # print(video_address_list)
    # video_address_list = tuple(video_address_list)
    # audio_download_for_multiprocessing(video_address_list, path)
    audio_download(video_address_list,path)

def download_from_url_list(str,path):
    list_to_download = []

def audio_download(video_address_list,path):

    with yt_dlp.YoutubeDL(CONSTANTS.ydl_opts) as ydl:
        with Pool(8) as executor:
            executor.map(ydl.download, video_address_list)
        # ydl.download(video_address_list)

#todo 研究一下池化
#初步估计多进程的核心问题在于cookie的文件锁
def audio_download_for_multiprocessing(video_address_list,path):
    pool = multiprocessing.Pool(8)
    for video_address_page in video_address_list:
        # with Pool(8) as executor:
        #     ydl = yt_dlp.YoutubeDL(CONSTANTS.ydl_opts)
        #     executor.apply(ydl.download,video_address_page)
        # ydl.download(video_address_list)
        pool.apply(yt_dlp.YoutubeDL(CONSTANTS.ydl_opts).download,video_address_page)

def judge_if_premier_only(path):
    path_dict = {'home':path}
    CONSTANTS.ydl_opts['paths'] = path_dict
    judge_url = 'https://www.nicovideo.jp/watch/sm35979548' # 夜驱
    info = None
    with yt_dlp.YoutubeDL(CONSTANTS.ydl_opts) as ydl:
        info = ydl.extract_info(judge_url,download=False,process=False)
        # ydl.__exit__()
        ydl.__exit__()
        return info['_api_data']['media']['delivery']['movie']['audios'][0]['isAvailable']

if __name__ == '__main__':
    type = 'tag'
    # type = [tag | search | ]
    # content = 'ボカコレ2022秋TOP100参加作品'
    content = 'ボカランED曲'
    # sort = 'likeCount'
    sort = CONSTANTS.sortBench.published_date
    order = 'd'
    path = "D:\\Media\\Music\\周刊ED\\"
    search_result_resolve(type, content, sort, order, path)
