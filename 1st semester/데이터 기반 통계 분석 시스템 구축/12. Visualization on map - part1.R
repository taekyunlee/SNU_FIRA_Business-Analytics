rm(list = ls()); gc(reset = T)

# -----------------------------
if(!require(maps)){install.packages("maps") ;library(maps)}
if(!require(mapdata)){install.packages("mapdata") ;library(mapdata)}

# -----------------------------
par(mfrow = c(1,1))
map(database = "usa")
map(database = "county") ## county map을 이용, 자세한 USA map을 그릴 수 있음

# -----------------------------
map(database = 'world', region = 'South Korea') # 닫힌 다각형 10개로 구성 region
# world2Hires에서 보다 높은 자세한 map을 그릴 수 있음
map('world2Hires', 'South Korea') 
map('world2Hires')

# -----------------------------
data(us.cities)
head(us.cities)

# -----------------------------
map('world', fill = TRUE, col = rainbow(30))

# -----------------------------
map('world', fill = TRUE, col = rainbow(30))

# -----------------------------
data(unemp) # unemployed rate data
data(county.fips) # county fips data
head(unemp,3)
head(county.fips,3)

# -----------------------------
unemp$colorBuckets <- as.numeric(cut(unemp$unemp, 
                                     c(0, 2, 4, 6, 8, 10, 100))) 
colorsmatched <- unemp$colorBuckets[match(county.fips$fips, unemp$fips)]

# -----------------------------
colors = c("#F1EEF6","#D4B9DA","#C994C7","#DF65B0","#DD1C77","#980043")
       # 칼라 파레트 만듦        
if(!require(mapproj)){install.packages("mapproj") ;library(mapproj)}
map("county", col = colors[colorsmatched], fill = TRUE,
    resolution = 0, lty = 0, projection = "polyconic")

# -----------------------------
colors = c("#F1EEF6","#D4B9DA","#C994C7","#DF65B0","#DD1C77","#980043")
map("county", col = colors[colorsmatched], fill = TRUE,
    resolution = 0, lty = 0, projection = "polyconic")

# -----------------------------
map("county", col = colors[colorsmatched], fill = TRUE,
    resolution = 0, lty = 0, projection = "polyconic")
map("state", col = "white", fill = FALSE, add = TRUE, lty = 1,
    lwd = 0.2,projection = "polyconic")
title("unemployment by county, 2009")

# -----------------------------
colors = c("#F1EEF6","#D4B9DA","#C994C7","#DF65B0","#DD1C77","#980043")
colorsmatched <- unemp$colorBuckets[match(county.fips$fips, unemp$fips)]
map("county", col = colors[colorsmatched], fill = TRUE,
    resolution = 0, lty = 0, projection = "polyconic")
map("state", col = "white", fill = FALSE, add = TRUE, lty = 1,
    lwd = 0.2,projection = "polyconic")
title("unemployment by county, 2009")

# -----------------------------
if(!require(dplyr)){install.packages("dplyr") ;library(dplyr)}
if(!require(ggplot2)){install.packages("ggplot2") ;library(ggplot2)}

wm <- ggplot2::map_data('world')
head(wm , n=30)
wm[400:500,]
wm %>% dplyr::select(region) %>% unique()%>%head()
# 맵이 그리는 단위는 나라가 아니라 폴리곤이다. 색깔벡터 열 따라 
# -----------------------------
ur <- wm %>% dplyr::select(region)%>%unique()
grep( "Korea", ur$region )  # 한국이 어디에 있는지 나옴 ,위치 
ur$region[c(125,185)]
nrow(ur)
# -----------------------------
map("world", ur$region[c(125,185)],fill = T,
    col = "blue")
wmr <- wm %>% filter(wm$region == 'South Korea' | wm$region == 'North Korea')
wmr <- wm %>% filter(wm$region == 'North Korea')
unique(wmr$group) # 북한 2개의 폴리곤 남한은 11개의 폴리곤 
wmr

wmr <- wm %>% filter(wm$region == 'South Korea')
map("world", ur$region[c(125,185)],fill = T,
    col = c(rep("darkblue",11), rep('pink',2)))


# -----------------------------
if(!require(mapplots)){install.packages("mapplots") ;library(mapplots)}
if(!require(ggmap)){install.packages("ggmap") ;library(ggmap)}
if(!require(mapdata)){install.packages("mapdata") ;library(mapdata)}
   
map('worldHires', 'South Korea')
seoul_loc = geocode('seoul')
busan_loc = geocode('Busan')
add.pie(z=1:2,labels = c('a','b'), 
        x = seoul_loc$lon, y = seoul_loc$lat, radius = 0.5)
add.pie(z=4:3,labels = c('a','b'),
        x = busan_loc$lon, y = busan_loc$lat, radius = 0.5)

















