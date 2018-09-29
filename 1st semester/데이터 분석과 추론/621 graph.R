
?iris
data(iris) 
str(iris)
summary(iris)

#R PLOT 그리기
plot(iris$Sepal.Length) #첫번쨰 부터 마지막 인덱스까지
plot(iris$Petal.Length)

# x,y 값 설정 #?plot
plot(x = iris$Sepal.Length ,y=iris$Petal.Length)
plot(iris$Sepal.Length, iris$Petal.Length)
plot(iris$Sepal.Length,iris$Petal.Length, xlim =c(2,10), ylim=c(0,8)) 
# x축 y축 범위 조절

# x축 이름 y축이름
plot(x = iris$Sepal.Length ,y=iris$Petal.Length, xlab='sepal Length',ylab='Petal Length')
#그래프 제목 
plot(x = iris$Sepal.Length ,y=iris$Petal.Length, xlab='sepal Length',ylab='Petal Length',
     main ='Iris sepal-petal Length')

#그래프 점  # cex 기준 1 점 크기 조젏
plot(iris$Sepal.Length ,cex = 0.5) 
plot(iris$Sepal.Length ,cex = 2)
# 그래프 점 모양 # rplot pch (구글에)
plot(iris$Sepal.Length, cex=1.5 , pch =16 )
plot(iris$Sepal.Length, cex=1.5 , pch =18 )

#그래프 점 색깔
plot(iris$Sepal.Length ,cex=1 ,pch= 16 , col=2) 
#그래프 타입 
plot(iris$Sepal.Length, cex=1, pch=16, type='l') # 1이 아니라 L 

#그래프 창 설정  
oldpar =par() # -> 그래프 창 설정 
par(mfrow =c(2,2)) #-> 한 창에 여러개 띄움  mfrow  mfcol  -> 차이: 창 순서 바꿈
plot(iris$Petal.Width, ylab="", main ='petal Length')
plot(iris$sepal.Length , type='l',ylab="",main ="petal Length")
plot(iris$sepal.Length ,col=2, type='l', lty=2 ,ylab="", main ="petal Length") #lty line type
plot(iris$Petal.Width, lwd =3 , type='l')   #lwd-> line width (선의 굵기)

#같이 그리기 
par(mfrow=c(1,1)) #  원래 값으로 돌리기 그래프 그리는 창 
plot(x= iris$Sepal.Length,y=iris$Sepal.Width, cex=1.5 , pch =16 )
points(iris$Petal.Length, iris$Petal.Width,col=2)
lines(iris$petal.Length, iris$Petal.Width, )
#범례 표시
legend('bottomright', legend=c('sepal','petal'), pch=c(16,1), col=1:2  ) # 순서 맞춰서

#히스토그램
hist(iris$Sepal.Length)
hist(iris$Sepal.Length, breaks = 20, freq=FALSE)  #막대 너비의 합이 1
?hist
#막대그래프
iris.mean =tapply(iris$Sepal.Length,iris$Species, mean) #각 종별 평균을 구하라
barplot(iris.mean)

save.image('graph')


































