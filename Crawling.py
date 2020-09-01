import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time
import os
import pandas as pd
import sys
import re
import atexit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from ckonlpy.tag import Twitter

class Crawling:
    def __init__(self):
        self.PROJECT_DIR = ''
        print(self.PROJECT_DIR)
        self.DOWNLOAD_DIR = os.path.join(self.PROJECT_DIR, 'download')
        #self.driver_path = os.path.join(self.PROJECT_DIR, 'lib/webDriver')

        # GUI 창 설정 (True = GUI 안함, False = GUI)
        self.headless = True

        # OS 확인
        self.platform = sys.platform
        if self.platform == 'darwin':
            print('System platform : Darwin')
            self.driver_path = './static/lib/webDriver/chromedriver_mac'

        elif self.platform == 'linux':
            print('System platform : Linux')
            self.driver_path = './static/lib/webDriver/chromedriver_linux'

        elif self.platform == 'win32':
            print('System platform : Window')
            #self.driver_path = os.path.join(self.driver_path, 'chromedriver_win.exe')
            self.driver_path = './static/lib/webDriver/chromedriver_win.exe'
            print(self.driver_path)

        else:
            print(f'[{sys.platform}] 지원하지 않는 운영체제입니다. 확인 바랍니다.')
            raise Exception()

        # 저장을 원하는 경로 설정 / 현재 경로
        self.img_save_path = os.getcwd()

        # 변경금지
        self.output_path = os.path.join(self.img_save_path, 'static')
        self.img_path = os.path.join(self.output_path, 'crawl_img')
        self.text_path = os.path.join(self.output_path, 'crawl_text')

        if os.path.isdir(self.output_path):
            pass
        else:
            os.mkdir(self.output_path)



    def text(self,scan_name):
        # 트위터 검색어
        self.scan_name = scan_name


    # 단어사전을 추가해야함. / 워드클라우드 사용시 사용됩니다.
    def sajun(self):
        sajun = ['트와이스', 'kf94', 'KF94', 'Kf94', 'kF94', '타임라인', '확진자', '예방수칙', '코로나19', 'corona19', 'Corona19',
                 '개소리', '판매', '제품', '쿠팡', 'kf94마스크', 'KF94마스크', 'Kf94마스크', 'kF94마스크',
                 '우한폐렴', '신종코로나', '신종코로나바이러스', 'coronavirus', 'Coronavirus', '사재기',
                 '복지부장관', '바이러스', '피해복구', '이만희', '문재인', '이재갑', '한림대',
                 '감염내과', '교수님', '정치인', '입국금지', '대변인', '청와대', '문대통령', '황기자', '신천지', '근로장려금',
                 '까페', '배달', '페미', '항체', '에휴', '미래통합당', '자유한국당', '민주통합당', '3사',
                 '이동통신', '갤럭시', '갤럭시S20', '감염병', '난리', '순방', '신천지', '신천지사이트', '쿠팡',
                 '쿠팡플렉스', 'coupang flex', '배급제', '1인2매', '마스크', '이덴트', '수출길', '마스크5부제',
                 '신천지연예인명단', '신천지연예인', '세계여성의날', '식약처', '양금희', '시진핑', '주석',
                 '보건당국', '구로콜센터', '실거래', '공적마스크', 'WHO', '사무총장', '큐넷', '팬데믹', '펜대믹', '팬대믹',
                 'pandemic', 'Pandemic', '1800선', '코스피', '코스피하락', '최악', '급락', '트럼프', 'cospi', 'cosdac', '사이드카',
                 '망했다', '10년전', 'IMF', '거품', '금융버블', '금융위기', '붕괴', '순매수', '순매도', '공매도', '공매도금지법',
                 '금융위원회', '한국거래소', '주지훈', '하이에나', '은혜의강교회', '사이비종교', '집단감염', '신도', '카톡', '카톡에러',
                 '개학연기', '신형아반떼', '현대자동차', '아반떼', 'Avante', '1500선붕괴', '1400선', 'n번방', 'n번방사건', '텔레그램',
                 '소신발언', '벗방', '그것이알고싶다', '카르텔', '사이버성폭력', '강력처벌', 'BJ', '그알', '셀트리온', '코로나항체', '항체개발',
                 '7월내', '조주빈', 'N번방박사', '한타바이러스', '중국바이러스', '설치류', '중국', '초중고', 'EBS특강', 'EBS', '온라인강의',
                 '포털서비스', '네이버', '카카오', '라이브특강', '라이브특강', '접속자폭주', '피파온라인4', '상반기', '로스터업데이트',
                 '넥슨', '후베이성', '우한폭동', '봉쇄풀린', '두달만에', '손석희', 'JTBC', '삼성', '긴급재난지원금', '복지로',
                 '중산층', '소득분위', '70%', '150%', '중위소득', '재난지원금']
        return sajun

    def cleanText(self,readData):
        # 텍스트에 포함되어 있는 특수 문자 제거
        text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》\n_·李永钦▶]', '', readData)
        return text

    def twitter(self):
        cr_name = 'twitter'
        # 이미지파일 저장 장소 확인
        save_path = os.path.join(self.img_path, cr_name)
        if os.path.isdir(save_path):
            print(cr_name + ' 이미지 경로 확인 완료')
        elif os.path.isdir(self.img_path):
            os.mkdir(save_path)
        else:
            os.mkdir(self.img_path)
            os.mkdir(save_path)

        text_save_path = os.path.join(self.text_path, cr_name)
        if os.path.isdir(text_save_path):
            print(cr_name + ' 텍스트 경로 확인 완료')
        elif os.path.isdir(self.text_path):
            os.mkdir(text_save_path)
        else:
            os.mkdir(self.text_path)
            os.mkdir(text_save_path)

        import time
        import nltk
        keyword = self.scan_name

        # 웹 셋팅
        chrome = self.generate_chrome(
            driver_path=self.driver_path,
            headless=self.headless,
            download_path=self.DOWNLOAD_DIR)

        # 웹접속 - 네이버 이미지 접속
        print("Twitter 접속중")
        # driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        # driver.implicitly_wait(30)

        url = 'https://twitter.com/search?q={}&src=typed_query'.format(keyword)
        chrome.get(url)
        time.sleep(3)

        body = chrome.find_element_by_css_selector('body')
        text2 = chrome.find_elements_by_css_selector(
            '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div')
        result = []

        for i in range(10):
            for q in range(3):
                body.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
            for ttt in tqdm(text2):
                result.append(re.sub('\n', '', ttt.text))

        t = Twitter()
        t.add_dictionary(self.sajun(), 'Noun')

        tokens_ko = []

        for i in range(len(result)):
            tokens_ko.append(t.nouns(result[i]))
        final = []
        for _, q in enumerate(tokens_ko):
            for i in range(len(q)):
                final.insert(-1, q[i])

        ko = nltk.Text(final, name="첫번째")
        data = ko.vocab().most_common(1000)
        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        date2 = time.strftime('%Y%m%d_%H%M', time.localtime(time.time()))

        # 텍스트파일에 댓글 저장하기
        file = open(text_save_path + '/twitter{}.txt'.format(date), 'w', encoding='utf-8')

        for review in result:
            file.write(review + '\n')

        file.close()

        tmp_data = dict(data)

        wordcloud = WordCloud(font_path='/Library/Fonts/NanumMyeongjo.ttf',
                              background_color='white', max_words=230).generate_from_frequencies(tmp_data)
        plt.figure(figsize=(10, 8))
        plt.imshow(wordcloud)
        plt.axis('off'), plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
        plt.savefig(save_path + "/twitter_{}.png".format(date), bbox_inces='tight', dpi=400, pad_inches=0)

    def Naver(self):
        cr_name = 'naver'
        # 이미지파일 저장 장소 확인
        save_path = os.path.join(self.img_path, cr_name)
        if os.path.isdir(save_path):
            print(cr_name + ' 이미지 경로 확인 완료')
        elif os.path.isdir(self.img_path):
            os.mkdir(save_path)
        else:
            os.mkdir(self.img_path)
            os.mkdir(save_path)

        text_save_path = os.path.join(self.text_path, cr_name)
        if os.path.isdir(text_save_path):
            print(cr_name + ' 텍스트 경로 확인 완료')
        elif os.path.isdir(self.text_path):
            os.mkdir(text_save_path)
        else:
            os.mkdir(self.text_path)
            os.mkdir(text_save_path)

        # 네이버 헤드라인 가져오는소스
        import time
        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        date2 = time.strftime('%Y%m%d_%H%M', time.localtime(time.time()))

        result = []
        res = []

        # 웹 셋팅
        chrome = self.generate_chrome(
            driver_path=self.driver_path,
            headless=self.headless,
            download_path=self.DOWNLOAD_DIR)

        # options = webdriver.ChromeOptions()
        #
        # options.add_argument('headless')
        # options.add_argument('--disable-gpu')
        # options.add_experimental_option('prefs', {
        #     'download.default_directory': self.DOWNLOAD_DIR,
        #     'download.prompt_for_download': False,
        # })

        # chrome = webdriver.Chrome(executable_path='./chromedriver_win.exe', options=options)

        # 웹접속 - 네이버 이미지 접속
        print("Naver 접속중")
        # driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        # driver.implicitly_wait(30)

        url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&date={}'.format(date)
        chrome.get(url)
        time.sleep(2)

        # scroll(3)
        for sun in range(4, 10):
            pr = chrome.find_elements_by_xpath('//*[@id="wrap"]/table/tbody/tr/td[2]/div/div[{}]'.format(sun))
            for p in pr:
                result.append(p.find_elements_by_tag_name('a'))
            # print(result)

            for i, q in enumerate(result):
                for e in q:
                    res.append(e.get_attribute('href'))
        http = list(set(res))
        len(http)
        https = []

        for idx in range(len(http)):
            if http[idx].find('popularDay') >= 0:
                continue
            else:
                https.append(http[idx])

        files = pd.DataFrame()

        for i in range(len(https)):
            res = requests.get(https[i])
            soup = BeautifulSoup(res.content, 'html.parser')
            body = soup.select('._article_body_contents')
            files = files.append(pd.DataFrame({
                'Title': soup.find('div', attrs={'class': 'article_info'}).h3.text,
                'Contents': re.sub('   ', '', re.sub('    ', '', re.sub('\t', '', self.cleanText(body[0].text)[
                                                                                  (self.cleanText(body[0].text)).find(
                                                                                      '{}') + 2:]))),
                'link': https[i]},
                index=[i]))

        text2 = files.Contents
        # 텍스트파일에 저장 csv
        files.to_csv(text_save_path + '/네이버종합뉴스_{}.csv'.format(date), index=False, encoding='utf-8')

        # -------------------------------------

        # 사전만들기
        from ckonlpy.tag import Twitter
        t = Twitter()
        t.add_dictionary(self.sajun(), 'Noun')

        import nltk
        tokens_ko = []

        for i in range(len(text2)):
            tokens_ko.append(t.nouns(text2[i]))

        final = []
        for _, q in enumerate(tokens_ko):
            for i in range(len(q)):
                final.insert(-1, q[i])

        ko = nltk.Text(final, name="첫번째")
        data = ko.vocab().most_common(1000)

        data_1 = []
        for i in range(len(data)):
            for q in range(0, 1, 1):
                if len(data[i][0]) >= 2:
                    data_1.append(data[i])

        from wordcloud import WordCloud
        import matplotlib.pyplot as plt

        import time
        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        date2 = time.strftime('%Y%m%d_%H%M', time.localtime(time.time()))

        tmp_data = dict(data_1)

        wordcloud = WordCloud(font_path='/Library/Fonts/NanumMyeongjo.ttf',
                              background_color='white', max_words=230).generate_from_frequencies(tmp_data)
        plt.figure(figsize=(10, 8))
        plt.imshow(wordcloud)
        plt.axis('off'), plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
        plt.savefig(save_path + "/naver_{}.png".format(date), bbox_inces='tight', dpi=400, pad_inches=0)

    def Daum(self):
        cr_name = 'daum'
        # 이미지파일 저장 장소 확인
        save_path = os.path.join(self.img_path, cr_name)
        if os.path.isdir(save_path):
            print(cr_name + ' 이미지 경로 확인 완료')
        elif os.path.isdir(self.img_path):
            os.mkdir(save_path)
        else:
            os.mkdir(self.img_path)
            os.mkdir(save_path)

        text_save_path = os.path.join(self.text_path, cr_name)
        if os.path.isdir(text_save_path):
            print(cr_name + ' 텍스트 경로 확인 완료')
        elif os.path.isdir(self.text_path):
            os.mkdir(text_save_path)
        else:
            os.mkdir(self.text_path)
            os.mkdir(text_save_path)


        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        date2 = time.strftime('%Y%m%d_%H%M', time.localtime(time.time()))
        # 다음뉴스 헤드라인 긁어오기
        http=[]
        print('Daum 접속 중')
        httz = 'https://media.daum.net/ranking/popular/?regDate={}'.format(date)
        res = requests.get(httz)
        soup = BeautifulSoup(res.content, 'html.parser')
        body = soup.select('#mArticle > div.rank_news > ul.list_news2')
        body = body[0].find_all('a')


        for i in range(len(body)):
            t = body[i].get('href')
            http.append(t)

        # 중복제거
        http = list(set(http))

        files = pd.DataFrame()
        for i in range(len(http)):
            res = requests.get(http[i])
            soup = BeautifulSoup(res.content, 'html.parser')
            body = soup.select('.article_view')[0]

            files = files.append(pd.DataFrame({
                'Title': soup.find('div', attrs={'class': 'head_view'}).h3.text,
                'Contents': " ".join(p.get_text() for p in body.find_all('p')),
                'link': http[i]
            }, index=[i]))
        text2 = files.Contents

        # 텍스트파일에 댓글 저장하기
        files.to_csv(text_save_path+'/다음뉴스종합_{}.csv'.format(date),index=False,encoding='utf-8')



        from ckonlpy.tag import Twitter

        t = Twitter()
        t.add_dictionary(self.sajun(), 'Noun')

        import nltk
        tokens_ko = []

        for i in range(len(text2)):
            tokens_ko.append(t.nouns(text2[i]))

        final = []
        for _,q in enumerate(tokens_ko):
            for i in range(len(q)):
                final.insert(-1,q[i])

        ko = nltk.Text(final, name="첫번째")
        data = ko.vocab().most_common(1000)


        # 다음뉴스는 50페이지 긁어오는거라서 1글자는 삭제했음. 필요한건 바로바로 보고서 사전에 추가해서 태깅 다시해야함.
        data_1 = []
        for i in range(len(data)):
            for q in range(0,1,1):
                if len(data[i][0]) >= 2 :
                    data_1.append(data[i])


        tmp_data = dict(data_1)

        wordcloud = WordCloud(font_path='/Library/Fonts/NanumMyeongjo.ttf',
                              background_color='white', max_words=230).generate_from_frequencies(tmp_data)
        plt.figure(figsize=(10, 8))
        plt.imshow(wordcloud)
        plt.axis('off'), plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
        plt.savefig(save_path+"/daum_{}.png".format(date), bbox_inces='tight', dpi=400, pad_inches=0)

    def _enable_download_in_headless_chrome(self,driver: webdriver, download_dir: str):
        """
        :param driver: 크롬 드라이버 인스턴스
        :param download_dir: 파일 다운로드 경로
        """
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

        params = {
            'cmd': 'Page.setDownloadBehavior',
            'params': {
                'behavior': 'allow',
                'downloadPath': download_dir
            }
        }
        driver.execute("send_command", params)

    def _close_chrome(self,chrome: webdriver):
        """
        크롬 종료

        :param chrome: 크롬 드라이버 인스턴스
        """

        def close():
            chrome.close()

        return close

    def generate_chrome(self,
            driver_path: str,
            download_path: str,
            headless: bool = False
    ) -> webdriver:
        """
        크롭 웹드라이버 인스턴스 생성

        :param driver_path: 드라이버 경로
        :param download_path: 파일 다운로드 경로
        :param headless: headless 옵션 설정 플래그

        :return webdriver: 크롬 드라이버 인스턴스
        """

        self.options = webdriver.ChromeOptions()
        if headless:
            self.options.add_argument('headless')
            self.options.add_argument('--disable-gpu')
        self.options.add_experimental_option('prefs', {
            'download.default_directory': download_path,
            'download.prompt_for_download': False,
        })

        chrome = webdriver.Chrome(executable_path=driver_path, options=self.options)

        if headless:
            self._enable_download_in_headless_chrome(chrome, download_path)

        atexit.register(self._close_chrome(chrome))  # 스크립트 종료전 무조건 크롬 종료

        return chrome