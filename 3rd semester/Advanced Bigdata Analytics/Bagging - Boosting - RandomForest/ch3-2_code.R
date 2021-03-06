rm(list=ls());gc()

#chap3-1 code 참고
cutoff_res = function(beta_hat = NULL, newx, response, cutoff, pred_prob = NULL){
  if (!is.null(beta_hat)) {
    X = cbind(1,as.matrix(newx))
    pred_prob = 1/(1+exp(-X%*%beta_hat))}
  pred = ifelse(pred_prob> cutoff, 1, 0)
  error_rate = mean(response != pred)
  sensitivity = sum(response == 1 & pred == 1)/sum(response == 1)
  specificity = sum(response == 0 & pred == 0)/sum(response == 0)
  precision = sum(response == 1 & pred == 1)/sum(pred == 1)
  recall = sensitivity
  if (sum(response == 1 & pred == 1) == 0) {f1 = 0}
  else {f1 = 2*(precision*recall)/(precision+recall)}
  cross_table = table(response, pred)
  return(list(res = c(cutoff, round(error_rate,4), 
                      round(sensitivity,4), round(specificity,4), round(f1, 4)),
              cross_table = cross_table))
} # res: 절단값, 오차율, 민감도, 특이도, f1값 그리고 교차표 출력

 
# chap3-1 code 참고. 각 모형에 대해 예측값 구해서 AUC 계산
auc_res = function(beta = NULL, newx, newy, pred_prob = NULL){ 
  if (!is.null(beta)){
    X = cbind(1,as.matrix(newx))
    pred_prob = 1/(1+exp(-X%*%beta))    }
  AUC = performance(prediction(pred_prob , newy) , "auc")
  return(AUC@y.values[[1]])
}


#--- 자료 전처리

## buytest data
#setwd("D:/Dropbox/조교자료/고용노동부_추천_201809/실습/ch3-2_lab")
buytest = read.table("C:/Users/renz/Desktop/고급 빅데이터 분석/ch3-2_lab/buytest.txt", header = T)
dim(buytest)
summary(buytest)

buytest[buytest$SEX == "", 'SEX'] = NA
levels(buytest$SEX)[1] = NA
buytest[buytest$ORGSRC == "", 'ORGSRC'] = NA
levels(buytest$ORGSRC)[1] = NA
buydata = buytest[,-c(1, 10, 19:26)] # 사용되지 않는 변수 제거
buydata = buydata[complete.cases(buydata),] # 결측치 제거
buydata = model.matrix(~., buydata)[,-1] # 가변수 생성

# 자료 분할(train, test set)
set.seed(1)
train_ind = sample(1:nrow(buydata), size = floor(nrow(buydata)*0.7), 
                   replace = F)
train = as.data.frame(buydata[train_ind,])
test = as.data.frame(buydata[-train_ind,])
X_train = buydata[train_ind, -1]
y_train = buydata[train_ind, 1]
X_test = buydata[-train_ind, -1]
y_test = buydata[-train_ind, 1]

dim(X_train)
dim(X_test)


#--- 3-2. 앙상블
## (1) 의사결정나무
library(rpart)
tree.buydata = rpart(as.factor(RESPOND)~., data = train)
tree.buydata
 
# rpart.control : minsplit, minbucket, cp, xval, etc.
tree.buydata = rpart(as.factor(RESPOND)~., data = train, control = rpart.control(cp = 0.005))
# cp 속성 값을 높이면 가지 수가 적어지고, 낮추면 가지 수가 많아진다.


tree.buydata
    
plot(tree.buydata)
text(tree.buydata, cex = 0.8)

plot(tree.buydata, margin = 0.1)  
text(tree.buydata, cex = 0.7, use.n =T) 

?text

# complexity parameter
tree.buydata = rpart(as.factor(RESPOND)~., data = train, control = rpart.control(cp = 0.001))
printcp(tree.buydata)

# 가지치기(prunning)
prune.buydata = prune(tree.buydata, cp = 0.005)
prune.buydata

plot(prune.buydata)
text(prune.buydata, cex = 0.7, use.n =T)


# CV 이용하여 적절한 가지치기 찾기
set.seed(1)    
K = 10
sample.ind = sample(1:K, size = nrow(train), replace = T)  
cp = seq(from = 0.001, to = 0.01, length = 30)
error = matrix(0, nrow = length(cp), K)
for (i in 1:length(cp)){
  for (j in 1:K){
    tmp = rpart(as.factor(RESPOND)~., data = train[sample.ind != j , ] ,  cp = cp[i]) 
    error[i,j] = sum(predict(tmp, train[sample.ind == j,], type = "class")
                     != train[sample.ind == j,]$RESPOND)/sum(sample.ind == j)
  } 
} 
rowMeans(error)
cp[which.min(rowMeans(error))]  
 

##(2) 배깅 및 랜덤포레스트
 
library(randomForest)
set.seed(1)
p = dim(as.matrix(train))[2] - 1
bag.fit = randomForest(x= X_train, y = as.factor(y_train), 
                       mtry = p, ntree = 500, importance = T)
bag.fit
mean(y_test != predict(bag.fit, X_test))
varImpPlot(bag.fit)
importance(bag.fit)

set.seed(1)
rf.fit = randomForest(x= X_train, y = as.factor(y_train), 
                      mtry = floor(sqrt(p)), ntree = 500, importance = T)
rf.fit
mean(y_test != predict(rf.fit, X_test))


varImpPlot(rf.fit)
importance(rf.fit)


##(3) 부스팅

# training
install.packages('xgboost')
library(xgboost)
boost.fit = xgboost(data = X_train, label = y_train, max.depth = 2, 
                    eta = 0.1, nround = 2, objective = "binary:logistic")

                                                
# testing              
pred = predict(boost.fit, X_test)
mean(y_test != round(pred))
?xgboost
# nround 에 따른 validataion set error
set.seed(123)
val.ind = sample(1:nrow(X_train), size = floor(nrow(X_train)*0.3))
val.err = c()
candidates = seq(from = 50, to = 250, by = 20)
for (i in candidates){
  boost.val = xgboost(data = X_train[-val.ind,], label = y_train[-val.ind], max.depth = 2, 
                      eta = 0.1, nround = i, objective = "binary:logistic", verbose = 0)
  pred.val = predict(boost.val, X_train[val.ind,])
  val.err = c(val.err, mean(y_train[val.ind] != round(pred.val)))
}
val.err
which.min(val.err)


boost.fit = xgboost(data = X_train, label = y_train, max.depth = 2, 
                    eta = 0.1, nround = candidates[which.min(val.err)], objective = "binary:logistic", verbose = 0)
pred = predict(boost.fit, X_test)
mean(y_test != round(pred))

# relative influence
import_mat = xgb.importance(colnames(X_train), model = boost.fit)
print(import_mat)


library(Ckmeans.1d.dp)
xgb.plot.importance(importance_matrix = import_mat)

# 모형별 ROC curve 및 AUC 값 비교
library(ROCR)
roc.plot = function(pred_prob, y, model_name = NULL){          
  AUC = performance(prediction(pred_prob , y) , "auc")
  ROC = performance(prediction(pred_prob ,y) , "tpr","fpr")
  plot(ROC , main = paste(model_name,"\n AUC:", 
                          round(as.numeric(AUC@y.values),4)), 
       col = "blue", lwd = 2.5)
  abline(c(0,0), c(1,1), lty = 2, lwd = 2)
}

# 6개의 모형에 대한 ROC, AUC값 비교(강의노트)  
 #pred_probs_test = sapply(1:4, function(i) 1/(1+exp(-cbind(1, X_test)%*%beta_hat[,i])))
 #pred_probs_test = cbind(pred_probs_test, predict(rf.fit, X_test, type = 'prob')[,2], 
 #                       predict(boost.fit, X_test))
 #model_names = c('Logistic','Logistic+AIC', 'Ridge', 'LASSO',
 #               'RandomForest', 'Boosting')

# 3개의 모형에 대한 ROC, AUC값 비교(배깅,랜덤포레스트,부스팅)
pred_probs_test = cbind(predict(bag.fit, X_test, type = 'prob')[,2],
                        predict(rf.fit, X_test, type = 'prob')[,2], 
                        predict(boost.fit, X_test))
model_names = c('Bagging','RandomForest', 'Boosting') 


par(mfrow = c(1,3))
for (i in 1:3){
  roc.plot(pred_probs_test[,i], y_test, model_names[i])
}


# 학습자료에서 오분류율 최소화하는 절단값을 이용하여 예측자료 성능 비교
cut_sel = matrix(0, nrow = 3, ncol = 3)
#pred_probs_train = sapply(1:4, function(i) 1/(1+exp(-cbind(1, X_train)%*%beta_hat[,i])))
pred_probs_train = cbind(predict(bag.fit, X_train, type = 'prob')[,2], predict(rf.fit, X_train, type = 'prob')[,2], 
                         predict(boost.fit, X_train))               
                                                                   
cutoff_can = seq(0.01, 0.99, by = 0.01)

for (i in 1:3){
  cutoff_out =  t(sapply(1:length(cutoff_can),
                         function(j) cutoff_res(newx = X_train, response = y_train, 
                                                cutoff = cutoff_can[j], pred_prob = pred_probs_train[,i])[[1]]))
  cut_sel[i, 1] = cutoff_out[which.min(cutoff_out[,2]), 1]                     
  cut_sel[i, 2] = cutoff_out[tail(which(cutoff_out[,3] >= 0.5), n = 1), 1]
  cut_sel[i, 3] = cutoff_out[which.max(cutoff_out[,5]), 1]
}


# 각 절단값에 따라 test set 의 결과 출력

# 오분류율 최소화
matrix(t(sapply(1:3, function(i) cutoff_res(newx = X_test, response = y_test, 
                                            cutoff = cut_sel[i, 1], pred_prob = pred_probs_test[,i])[[1]])),
       nrow = 3,
       dimnames =list(model_names, c("cutoff","error rate","sensitivity",
                                     "specificity","f1 score")))

# 민감도 0.5이상
matrix(t(sapply(1:3, function(i) cutoff_res(newx = X_test, response = y_test, 
                                            cutoff = cut_sel[i, 2], pred_prob = pred_probs_test[,i])[[1]])), 
       nrow = 3,
       dimnames =list(model_names, c("cutoff","error rate","sensitivity","specificity","f1 score")))


# f1값 최대화
matrix(t(sapply(1:3, function(i) cutoff_res(newx = X_test, response = y_test, 
                                            cutoff = cut_sel[i, 3], pred_prob = pred_probs_test[,i])[[1]])), 
       nrow = 3,
       dimnames =list(model_names, c("cutoff","error rate","sensitivity","specificity","f1 score")))



#--- 4. Case-control sampling
# 과소 추정  y_train == 0 을 y_train == 1 의 2배수준으로 줄임
# y==0 인 자료를 y==1인 자료의 2배만큼 추출.
n1 = sum(y_train == 1)
set.seed(6)
cc_ind = sample(1:sum(y_train == 0),
                size = 2*n1, replace = F)
cc_data = rbind(train[y_train == 1,],
                train[y_train == 0,][cc_ind,])

cc_data = cc_data[sample(1:nrow(cc_data), nrow(cc_data), replace = F),]
table(cc_data$RESPOND)
dim(cc_data)

# 반복횟수는 50번
tol_iter = 50
beta_list = list()
set.seed(6)
for (iter in 1:tol_iter){
  cc_ind = sample(1:sum(y_train == 0),
                  size = 2*n1, replace = F)
  cc_data = rbind(train[y_train == 1,],
                  train[y_train == 0,][cc_ind,])
  beta_list[[iter]] = coef(glm(RESPOND~., data = cc_data, family = 'binomial'))
}

# 반복을 통해 만들어진 여러 모형을 합쳐서 최종 앙상블 모형 생성
train_pred_probs = sapply(1:tol_iter, 
                          function(iter) 1/(1+exp(-cbind(1, X_train)%*%
                                                    beta_list[[iter]])))
train_pred_prob = rowMeans(train_pred_probs)
test_pred_probs = sapply(1:tol_iter, 
                         function(iter) 1/(1+exp(-cbind(1, X_test)%*%
                                                   beta_list[[iter]])))
test_pred_prob = rowMeans(test_pred_probs)


# 앙상블 모형의 AUC 결과      
auc_res(newx = X_train, newy = y_train, pred_prob = train_pred_prob)
auc_res(newx = X_test, newy = y_test, pred_prob = test_pred_prob)

# 해보기 : 위의 과소 추출법을 전진선택법 (AIC), Ridge, LASSO, RandomForest, Boosting에 대해 실행, 
# AUC 비교, 여러 절단값 선택 방법들을 시행하여 예측성능 비교.