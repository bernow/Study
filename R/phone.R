phone <- c()

for(i in 1:1000){
  a <- sprintf("%04d", sample(x=1:9999,size=1))
  b <- sprintf("%04d", sample(x=1:9999,size=1))
  phone <- c(phone,paste0("010-",a,"-",b))
}

phone

write.csv(phone,  "phone2.csv", row.names = F)