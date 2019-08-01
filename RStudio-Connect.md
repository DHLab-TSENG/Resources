# 安裝與設定RStudio Connect說明
環境: Ubuntu 18.04.2 LTS

## 安裝R
1. 先更新
`sudo apt-get update`

2. 安裝R
`sudo apt-get install r-base`

## 安裝RStudio Connect

1. 安裝deb軟體包
`sudo apt-get install gdebi-core`

2. 下載RStudio Connect
`wget https://s3.amazonaws.com/rstudio-connect/rstudio-connect_1.7.4.1-7_amd64.deb`

3. 安裝RStudio Connect
`sudo gdebi rstudio-connect_1.7.4.1-7_amd64.deb`

4. 安裝必要套件
`sudo apt-get install build-essential libcurl4-gnutls-dev openjdk-7-* libxml2-dev libssl-dev texlive-full`

## 設定RStudio Connect
1. 打開設定檔
`sudo vim /etc/rstudio-connect/rstudio-connect.gcfg`

2. 參考說明文件設定網址
https://docs.rstudio.com/connect/admin/getting-started.html#initial-configuration


## 換證號
`sudo /opt/rstudio-connect/bin/license-manager deactivate`
