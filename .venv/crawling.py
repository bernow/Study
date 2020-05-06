from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=5&bidNm=&searchDtType=1&fromBidDt=2020/04/27&toBidDt=2020/04/27&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1")
