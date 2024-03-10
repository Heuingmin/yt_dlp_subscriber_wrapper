import mysql.connector

header = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
'Connection': 'keep-alive',
#'Cookie': 'nicosid=1654832700.386030167; _ts_yjad=1654832699020; _tdim=2967df10-e8a1-4315-ad61-684630526bc0; _im_id.1004550=65e6521f4ea10255.1654832709.; optimizelyEndUserId=oeu1654946006156r0.12031542107543336; optimizelySegments=%7B%223176911475%22%3A%22direct%22%2C%223188621092%22%3A%22gc%22%2C%223192211201%22%3A%22false%22%2C%223217420529%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; user_session=user_session_42190146_47b619e7b4b373cbda4a70609b71a1f83b3fc753b42366144f8c92097b182f45; user_session_secure=NDIxOTAxNDY6STlnVlFCdFpndmc1Y09IR3pFQVNiQ2xGMFFXS0xHZlJTcHBNRlhhcGI4Vg; col=1; _gcl_au=1.1.1196972546.1662871780; _ss_pp_id=a9e8dc77c5a522295281663273402826; _td=9bd5c48f-4ccc-48db-a965-c5e0dda2cde2; cto_bundle=d10BlV9OVlF3aCUyQjZCUWI5VTVhNERrbXV6OXpaOHFnQnQwR0NLaTJuN0tmWDNTeU1XQTZxUVJqJTJGN3MlMkJIWk9KQUFpTCUyQjk4V0htME9BcmVRdDljOEY1TGJWUHpac2lZMFRUJTJCNDZhWTVJM1gxZXlHUm9nN2d2dFpYNDF5WVo2MWdvbjVsd21kTFl6TFRia1RpYmlRNzFmRWJPa3d3JTNEJTNE; _gid=GA1.2.1960299906.1665194052; __aaxsc=1; __gads=ID=56889b7a5f5c58b6:T=1665280173:S=ALNI_MaoGZKEWQ-3UwoWFoeAcU8vdmOL-w; __gpi=UID=00000a2451911d07:T=1665280173:RT=1665280173:S=ALNI_MbGa4aTUQxofLgBcgBlGrPJCmsGEQ; common-header-oshirase-open-date=2022-10-09T06:05:38.116Z; aasd=1%7C1665538768580; common-header-oshirasebox-newest=2022-10-11T19:56:34.075+09:00; _im_ses.1004550=1; nico_gc=srch_s%3Dv%26srch_o%3Dd%26tg_o%3Dd%26tg_s%3DlikeCount; _ga_5LM4HED1NJ=GS1.1.1665578063.120.1.1665578251.58.0.0; _ga=GA1.1.1240634898.1654832702; _gat_NicoGoogleTagManager=1',
'Cookie': '_ga=GA1.1.63072463.1692687998; lastPath=/%E4%B8%93%E6%A0%8F/%E9%AB%98%E5%B9%B6%E5%8F%91%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A140%E9%97%AE; _ga_NPSEEVD756=GS1.1.1692687997.1.1.1692688824.57.0.0',#'Host': 'www.nicovideo.jp',
    "Referer": 'https://learn.lianglianglee.com/',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"'
}
def filter_long_video(info,*,incomplete):
    duration = info.get('duration')
    if duration and duration > 1800:
        return 'The video is too long'
ydl_opts = {
    # 'format': 'bestaudio/worstvideo',
    # 'format_sort_force': '+abr,size',
    'cookiefile': 'C:\\Users\\19125\Downloads\\nicovideo.jp_cookies.txt',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
    }],
    'proxy': 'socks5://127.0.0.1:7890/',
    'download_archive': "D:\\Media\\Music\\Archieve",
    'break_on_existing': False,
    'downloader':'aria2c',
    # 'max_filesize': '200M',
    'concurrent-fragments':8,
    'quiet':True,
    'ignoreerrors':True,
    "add_header":"Accept-Language:ja",
    'match_filter':filter_long_video
}
#目前先以常量字面值的形式存储，之后看看有没有必要上数据库
#另外考虑1.rss 2.引入date，记录最近一次爬取日期（这个可能得和数据库绑着使用，存文件里不太现实）
#目前的考虑：列表+日期/投稿数目，定时监控，放mysql里，定期执行并且更新（RSS配nico似乎欠稳定）
#今晚把这个爬虫和PJSK的其他爬虫整了
users = [
    ('x髥莏','https://www.nicovideo.jp/user/88252248'),
    ('環崎にょちお','https://www.nicovideo.jp/user/26877910'),
    # ('Arimuri',),
    # ('油性',''),
    ('リギル','https://www.nicovideo.jp/user/2427360'),
    ('daraku','https://www.nicovideo.jp/user/118137370'),
    ('blues','https://www.nicovideo.jp/user/116821094'),
    ('アタリ','https://www.nicovideo.jp/user/50698413'),
    ('吉田夜世','https://www.nicovideo.jp/user/23662320'),
    ('Mikade','https://www.nicovideo.jp/user/30683338'),
    ('GONNZ','https://www.nicovideo.jp/user/123981861'),
    ('ムラタシユウ','https://www.nicovideo.jp/user/70152889'),
    ('GOAT','https://www.youtube.com/c/Goat_20XX'),
    ('西憂花','https://www.nicovideo.jp/user/121341941'),
    ('イマニシ','https://www.nicovideo.jp/user/117299724'),
    ('亜店','https://www.nicovideo.jp/user/93318590'),
    ('ゆうら','https://www.nicovideo.jp/user/92589104'),
    ('かんてゐく','https://www.nicovideo.jp/user/116947634'),
    ('ミヤサカアキラ','https://www.nicovideo.jp/user/51118252'),
    ('ごーぶす','https://www.nicovideo.jp/user/46749040'),
    ('靴紐','https://www.youtube.com/@user-nx3tl4be1l'),
    ('Peg','https://www.nicovideo.jp/user/78627783'),
    ('白風珈琲','https://www.nicovideo.jp/user/92893091'),
    ('春浅葱','https://www.nicovideo.jp/user/123814103'),
    ('エイハブ','https://www.nicovideo.jp/user/95812305/mylist/68647788'),
    ('なちぴ','https://www.youtube.com/@nachi-p3013/videos'),
    ('EO','https://www.nicovideo.jp/user/116064862'),
    ('A4。','https://www.nicovideo.jp/user/115965100'),
    # ('シキドール',''),
    ('jon-YAKITORY','https://www.nicovideo.jp/mylist/37411638'),
    ('Project Lumina','https://www.nicovideo.jp/user/123688006'),
    ('由末 イリ','https://www.nicovideo.jp/user/77252050'),
    ('リョウ','https://www.nicovideo.jp/user/62311318'),
    ('limit34','https://www.youtube.com/channel/UCm4Qbe8dudHQWfO-tn2MwMQ'),
    ('SIG','https://www.nicovideo.jp/user/116312118'),
    ('Ç¢Çª','https://www.nicovideo.jp/user/125155973/mylist/73501346'),
    ('橘しとら','https://www.nicovideo.jp/user/125508936'),
    ('nenene','https://www.nicovideo.jp/user/129511558'),
    ('GESO','https://www.nicovideo.jp/user/118282262/mylist/70725956'),
    ('rinri','https://www.nicovideo.jp/user/125363498'),
    ('itsuka','https://www.nicovideo.jp/user/122501596'),
    ('NexDart','https://www.nicovideo.jp/user/15712334'),
    # ('nana','https://www.nicovideo.jp/user/26877910'),
    ('中瀬ミル','https://www.youtube.com/@mirunakase'),
    ('caffeine','https://www.youtube.com/@caffeine-mcl'),
    ('Ramune','https://www.youtube.com/@ramune8447'),
    ('マツシタレオ','https://www.youtube.com/@Leo_Matsushita'),
    ('アメリカ民謡研究会','https://www.youtube.com/watch?v=q4NeJLhAGso'),
    ('いえぬ','https://www.youtube.com/@ienu0ienu'),
    ('君嶋リョウ','https://www.youtube.com/channel/UCoVBCf62dif6N3skpQq3xfQ'),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
]
class sortBench:
    popularity = 'h'
    published_date = 'f'
    recommended = 'p'
    views = 'v'
    mylists_num = 'm'
    comment_num = 'r'
    comment_time = 'n'
    length = 'l'
    likeCount = 'likeCount'

    desc = 'd'
    asc = 'a' 

def get_option(url,path):
    option = ydl_opts.copy()
    if url.find('nico')!=-1:
        option['format'] = 'worst'
        option['format_sort'] = ['+abr','size']
    else:
        option['format'] = 'bestaudio'
        option['postprocessors'] = []
        # option[]
    option['paths'] = path
    return option

def get_infos_from_db():
    try:
        # 连接到 MySQL 数据库
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="music"
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            # 创建游标对象
            cursor = connection.cursor()

            # 执行查询
            cursor.execute("SELECT * FROM authors")

            # 获取所有结果
            authors_data = cursor.fetchall()

            # 关闭游标和连接
            cursor.close()
            connection.close()

            # 返回作者数据
            return authors_data

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    return None
