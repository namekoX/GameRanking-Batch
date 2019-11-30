import requests
from bs4 import BeautifulSoup
from db_util import DbUtil, Entry

class GetRank(object):
    def getDmm18(self):
        html_doc = requests.get("http://games.dmm.co.jp/ranking/").text
        soup = BeautifulSoup(html_doc, 'html.parser')

        commentlist = []
        comments = soup.find_all('span', {'class': 'tx-comment'})
        for comment in comments:
            commentlist.append(comment.get_text(strip=True))

        thumblist = []
        titlelist = []
        thumbs = soup.find_all('span', {'class': 'thumb'})
        for thumb in thumbs:
            img = thumb.find('img')['src']
            thumblist.append(img)
            title = thumb.find('img')['alt']
            titlelist.append(title)

        linkslist = []
        rankings = soup.find_all('div', {'class': 'ranking'})
        for ranking in rankings:
            links = ranking.find_all('a')
            for link in links:
                if not 'ranking?' in link['href']:
                    linkslist.append(link['href'])

        dbUtil = DbUtil()
        for i in range(len(titlelist)):
            entry = Entry('dmmR18',titlelist[i], i + 1, commentlist[i], linkslist[i], thumblist[i])
            dbUtil.insert_entry(entry)

        dbUtil.conClose()
        return 0

    def getDmm(self):
        html_doc = requests.get("http://games.dmm.com/ranking/").text
        soup = BeautifulSoup(html_doc, 'html.parser')

        commentlist = []
        comments = soup.find_all('span', {'class': 'tx-comment'})
        for comment in comments:
            commentlist.append(comment.get_text(strip=True))

        thumblist = []
        titlelist = []
        thumbs = soup.find_all('span', {'class': 'thumb'})
        for thumb in thumbs:
            img = thumb.find('img')['src']
            thumblist.append(img)
            title = thumb.find('img')['alt']
            titlelist.append(title)

        linkslist = []
        rankings = soup.find_all('div', {'class': 'ranking'})
        for ranking in rankings:
            links = ranking.find_all('a')
            for link in links:
                if not 'ranking?' in link['href']:
                    linkslist.append(link['href'])

        dbUtil = DbUtil()
        for i in range(len(titlelist)):
            entry = Entry('dmm',titlelist[i], i + 1, commentlist[i], linkslist[i], thumblist[i])
            dbUtil.insert_entry(entry)

        dbUtil.conClose()
        return 0

    def getNijiyome(self):
        html_doc = requests.get("https://www.nijiyome.com/app/list?st=1").text
        soup = BeautifulSoup(html_doc, 'html.parser')

        titlelist = []
        names = soup.find_all('p', {'class': 'name'})
        for name in names:
            titles = name.find_all('a')
            for title in titles:
                titlelist.append(title.get_text(strip=True))

        commentlist = []
        details = soup.find_all('div', {'class': 'detail'})
        for detail in details:
            comments = detail.find_all('p')
            for comment in comments:
                commentlist.append(comment.get_text(strip=True))

        linkslist = []
        thumblist = []
        figures = soup.find_all('figure', {'class': 'image'})
        for figure in figures:
            links = figure.find_all('a')
            for link in links:
                linkslist.append(link['href'])
            thumbs = figure.find_all('img')
            for thumb in thumbs:
                thumblist.append('https:' + thumb['src'])

        dbUtil = DbUtil()
        for i in range(len(titlelist)):
            entry = Entry('nijiyome',titlelist[i], i + 1, commentlist[i], linkslist[i], thumblist[i])
            dbUtil.insert_entry(entry)

        dbUtil.conClose()
        return 0

    def getGooglePlay(self):
        html_doc = requests.get("https://play.google.com/store/apps/collection/cluster?clp=0g4YChYKEHRvcGdyb3NzaW5nX0dBTUUQBxgD:S:ANO1ljLhYwQ&gsr=ChvSDhgKFgoQdG9wZ3Jvc3NpbmdfR0FNRRAHGAM%3D:S:ANO1ljIKta8&hl=ja&gl=jp").text
        soup = BeautifulSoup(html_doc, 'html.parser')

        titlelist = []
        titles = soup.find_all('div', {'class': 'WsMG1c'})
        for title in titles:
            titlelist.append(title['title'])

        commentlist = []
        linkslist = []
        thumblist = []
        figures = soup.find_all('div', {'class': 'b8cIId'})
        for figure in figures:
            links = figure.find_all('a')
            for link in links:
                linkslist.append(link['href'])
                commentlist.append('https://play.google.com' + link.get_text(strip=True))

        dbUtil = DbUtil()
        for i in range(len(titlelist)):
            entry = Entry('GooglePlay',titlelist[i], i + 1, commentlist[3 * i + 2], linkslist[3 * i + 2], "")
            dbUtil.insert_entry(entry)

        dbUtil.conClose()
        return 0

    def getYahoo(self):
        html_doc = requests.get("https://games.yahoo.co.jp/title/list?sort=rank").text
        soup = BeautifulSoup(html_doc, 'html.parser')

        titlelist = []
        titles = soup.find_all('div', {'class': 'item__name'})
        for title in titles:
            titlelist.append(title.get_text(strip=True))

        dbUtil = DbUtil()
        for i in range(len(titlelist)):
            entry = Entry('Yahoo',titlelist[i], i + 1, "", "", "")
            dbUtil.insert_entry(entry)

        dbUtil.conClose()
        return 0