
import requests_constants as CONSTANTS
import requests
import nicoSpider as NS
from win11toast import toast
from parsel import Selector
from io import StringIO
import yt_dlp
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from io import StringIO
import contextlib
path = "D:\\Media\\Music\\"

class producer_data:
    producer_name  = ""
    date = None
    url = None


def initialize():
    if not NS.judge_if_premier_only(path):
        toast("NICONICO当前时段会员专属，请换一个时段看看！")
        return

    producer_list = get_producer_list()
    # with Pool(6) as exece:
    with ThreadPoolExecutor(1) as executor:
        executor.map(download,producer_list)
        executor.shutdown(wait=True)
        # exece.join()
        # exece.close()

def download(producer_info):
    try:
        p_path = {'home': path + producer_info[0]}
        url = producer_info[1]
        options = CONSTANTS.get_option(url,p_path)
        # yt_dlp.YoutubeDL(options).download(url)
        # stdout_buffer = StringIO()
        # with contextlib.redirect_stdout(stdout_buffer):
            # 在上下文中执行下载，控制台输出将被捕获到缓冲区

        # infos = yt_dlp.YoutubeDL(options).extract_info(url,download=False);
        # yt_dlp.YoutubeDL(options).
        yt_dlp.YoutubeDL(options).download([url])

    except  Exception as e:
        print(f"在下载{producer_info[0]}的作品时发生异常：{e.args}")
    # options['paths'] = producer_path
    # yt_dlp.YoutubeDL(options).download(url)


    #
    # for item in producer_list:
    #     producer_path = path + item[0]
    #     url = list(item[1])
    #     options = CONSTANTS.ydl_opts.copy()
    #     options['paths'] = {'home' : producer_path}
    #     pool.apply(yt_dlp.YoutubeDL(options).download,url)
    #

def get_producer_list():
    result = CONSTANTS.users.copy()
    for item in result:
        if item[0] == '':
            result.remove(item)
    return result

if __name__ == '__main__':
    initialize()

# 此处存放的是YoutubeDL中的修改逻辑，用以更智能的避免下载。
# 使用时放在1812行 / self.add_default_extra_info(ie_result, ie, url)后面
#
# entries = resolved_entries = list(entries)
# try:
#     temp_entries = []
#     find_str = ''.join(os.listdir(self.params.get('paths').get('home')))
#     for i in resolved_entries:
#         id_index = max(i[0]['url'].rfind("v="), i[0]['url'].rfind("/")) + 2
#         id = i[0]['url'][id_index:]
#         if find_str.find(id) == -1:
#             temp_entries.append(i)
#     self.to_screen(f"我根据文件存在与否过滤掉了很多下载地址，原有{len(entries)}条，现在有{len(temp_entries)}条")
#     entries = resolved_entries = temp_entries
# except:
#     None