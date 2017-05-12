# Server Setup
Last update: 2017/05/12

## Linux Server

### 安裝ubuntu

- 安裝Ubuntu 16.04 伺服器版本
  - 從光碟安裝
  - 安裝說明 https://www.ubuntu.com/download/server/install-ubuntu-server
  - 中文step by step 安裝說明 https://magiclen.org/ubuntu-server-14-04/
  - 中文網站 https://www.ubuntu-tw.org/
- ubuntu管理設定
  - 網路設定與固定IP設定方式 https://www.cyut.edu.tw/~ckhung/b/gnu/network.php
  - 防火牆設定 http://download.ithome.com.tw/article/index/id/974
    - 設定規則請見 https://github.com/DHLab-CGU/Resources-Private
  - 桌面工具安裝方式 http://www.arthurtoday.com/2012/11/ubuntu-server-install-unity-gui.html

### 安裝R相關工具
- 安裝R
  - https://cran.rstudio.com/bin/linux/ubuntu/README.html
  - 按照指令執行

- 安裝RStudio Server Pro
  - http://docs.rstudio.com/ide/server-pro/index.html#debian-8-ubuntu-12.04
  - 按照指令執行

- 輸入RStudio Server Pro product key 
  - http://docs.rstudio.com/ide/server-pro/index.html#activation
  - product key 找 PI要

- RStudio Server Pro管理設定
  - Port設定 
    - http://docs.rstudio.com/ide/server-pro/access-and-security.html#network-port-and-address
  - 可連接ip設定
    - http://docs.rstudio.com/ide/server-pro/access-and-security.html#ip-access-rules

- RStudio Server to SQL Server
  - ODBC driver https://blogs.msdn.microsoft.com/sqlnativeclient/2016/10/20/odbc-driver-13-0-for-linux-released/
  - 安裝RODBC package for all user `sudo apt-get install r-cran-rodbc`
  - 連接方法 https://support.rstudio.com/hc/en-us/articles/214510788-Setting-up-R-to-connect-to-SQL-Server-

- 套件安裝

以下為已安裝之共用套件
```{r}
install.packages(c("curl","RCurl","Rcpp","readr","dplyr","data.table","bit64",
                   "ggplot2","stringr","tidyr","rvest","lubridate","readxl",
                   "jiebaR","devtools","icd"), lib="/usr/local/lib/R/site-library")
install.packages(c("caret"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends", "Suggests"))                      
```

## Windows Server資料機

- 安裝Windows Server 2016
  - 從光碟安裝
  - 序號找PI索取

- Windows Server 2016管理設定
  - https://www.youtube.com/watch?v=jt9mTMvDxqg&index=9&list=PLtQwQZqIvJLdsZczfIQImksQQM9WEXK5K

- 安裝SQL Server 2016
  - 從光碟安裝

- SQL Server 2016管理設定
  - SQL與Windows驗證
  - 開防火牆1433Port
  
- Elasticsearch
  - http://stackoverflow.com/questions/40540123/elasticsearch-windows-service-not-work-on-nano-server
  - https://www.elastic.co/webinars/getting-started-elasticsearch
  
  
## Windows Server開發機

- 安裝Windows Server 2016
  - 從光碟安裝

- Windows Server 2016管理設定
  - https://www.youtube.com/watch?v=jt9mTMvDxqg&index=9&list=PLtQwQZqIvJLdsZczfIQImksQQM9WEXK5K

- React Native 相關安裝
  - https://github.com/DHLab-CGU/Resources/blob/master/ReactNativeWinServerSetup.md


## OS X Server開發機

- 安裝Xcode
  - 從App Store下載

- 安裝OS X Server
  - 從App Store下載
    - http://www.apple.com/tw/osx/server/
    - 帳密找 PI要

- OS X Server管理設定
  - TBD
  - 可遠端用個人帳密登入

- React Native 相關安裝
  - https://github.com/DHLab-CGU/Resources/blob/master/ReactNativeiOSSetup.md


