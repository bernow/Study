library(httr)
library(XML)
library(rvest)

df <- data.frame(matrix(nrow=0, ncol=8))
pageNo <- 1
check <- TRUE

while(1){
  url <- paste0("http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?area=&bidNm=&bidSearchType=1&currentPageNo=",pageNo,"&fromBidDt=2020%2F05%2F13&fromOpenBidDt=&instNm=&maxPageViewNoByWshan=44&radOrgan=1&regYn=Y&searchDtType=1&searchType=1&taskClCds=5&toBidDt=2020%2F05%2F13&toOpenBidDt=&")
  nara <- read_html(url, encoding="CP949")
  for(i in 1:10){
    nodes <- html_nodes(nara, xpath = paste0('//*[@id="resultForm"]/div[2]/table/tbody/tr[',i,']/td'))
    if(length(nodes)==0){
      check <- FALSE
      break
    }
    if(html_text(nodes[1])=="검색된 데이터가 없습니다."){
      check <- FALSE
      break
    }
    vec <- c()
    for(j in 1:8){
      temp <- html_text(nodes[j])
      vec <- c(vec, temp)
    }
    df <- rbind(df,vec)
  }
  if(check==FALSE){
    break
  }
  pageNo <- pageNo+1
}

names(df) <- c("업무", "공고번호-차수", "분류", "공고명", "공고기관", "수요기관", "계약방법", "입력일시(입찰마감일시)")

df[length(df[,1]),1:8]
df
write.csv(df, "0513.csv", row.names = F)
