# PM2設定筆記

## pm2 安裝 @Ubuntu
https://www.rplumber.io/docs/hosting.html#pm2

```
sudo apt-get update
sudo apt-get install nodejs npm
sudo npm install -g pm2
```

## 新增包括API指令的R程式碼檔案
以`firstAPI.R`為例，先進到未來要放API的R程式碼資料夾(以`~/API`為例)，如果沒有此資料夾，可在ubuntu新增資料夾

```
mkdir ~/API
```

新增完後在ubuntu輸入

```
sudo vim ~/API/firstAPI.R
```

開啟vim編輯器後，將**API程式碼**貼入並:wq存檔

## 新增呼叫並啟用`firstAPI.R`的R程式碼
以`test.R為例`，在ubuntu輸入
```
sudo vim ~/API/test.R
```
並將下列程式碼貼上
```
#!/usr/bin/env Rscript

library(plumber)
pr <- plumb('~/API/firstAPI.R')
pr$run(port=4000)
```

## 確定Ubuntu上有R以及會用到的套件
如果沒有R，要裝，可直接在ubuntu上輸入
```
R
```
看能不能進入R程式就知道了

下一步要確認有安裝要用到的R套件，如`plumber`或`dplyr`等，如果沒有，可直接安裝。
安裝方法有很多種，可先用sudo權限進入R
```
sudo R
```
再輸入以下R指令

```
install.packages(c("plumber","dplyr"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
```

最後輸入`q()`跳出


## 使用pm2啟用API
```
sudo pm2 start --interpreter="Rscript" test.R
```

## 檢查是否有正常啟用
```
sudo pm2 show test
```
