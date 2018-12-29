# Server Setup
Last update: 2018/12/29

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

- 舊機轉移
  - https://www.phpini.com/linux/linux-server-migrate-user-accounts
  - http://jack197247.pixnet.net/blog/post/21988637-linux%E5%B8%B3%E8%99%9F%E5%8F%8A%E5%AE%B6%E7%9B%AE%E9%8C%84%E9%83%B5%E4%BB%B6%E7%A7%BB%E8%BD%89%E8%87%B3%E6%96%B0%E6%A9%9F
  
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

- 安裝套件所需元件

https://stackoverflow.com/questions/15248815/rgdal-package-installation
https://github.com/datacarpentry/r-raster-vector-geospatial/issues/138
```
sudo apt install apt-file
apt-file purge
sudo apt-file update 
apt-cache search libgdal
sudo apt-get install libgdal1-dev proj-data proj-bin 
sudo apt-get install libxml2-dev
sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
sudo apt-get update
sudo apt-get install libudunits2-dev libgdal-dev libgeos-dev libproj-dev
sudo apt-get install default-jre
sudo apt-get install default-jdk
sudo R CMD javareconf
sudo apt-get install r-cran-rjava
sudo apt-get install libcairo2-dev
sudo apt-get install libxt-dev
export LD_LIBRARY_PATH=/usr/local/cuda-9.2/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda-9.2/bin:$PATH
sudo ldconfig /usr/local/cuda-9.2/lib64
```

- 套件安裝，必須在終端機畫面，用sudo R進入R程式 (需root權限)，輸入以下語法

```{r}

install.packages(c("scales"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
install.packages(c("bitops","curl","RCurl","Rcpp","readr","dplyr","data.table","bit64","ggplot2","stringr","tidyr","rvest","lubridate","readxl","jiebaR","devtools","icd","rJava","RODBC","cronR","shiny","miniUI","shinyFiles"), lib="/usr/local/lib/R/site-library")


install.packages(c("Cairo"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
install.packages(c("crosstalk","htmlwidgets","DT"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
install.packages(c("R.cache","R.methodsS3", "R.oo", "R.utils","R.devices"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends", "Suggests"))
install.packages(c("brew", "commonmark","roxygen2"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
install.packages(c("rex","covr"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
install.packages(c("tinytex","rmarkdown","tufte"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
install.packages(c(), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))

install.packages(c("jsonlite","foreign","openxlsx","elastic","sas7bdat"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends", "Suggests"))
withr::with_libpaths(new = "/usr/lib/R/site-library/", devtools::install_github('imanuelcostigan/RSQLServer'))

install.packages(c("repr","snakecase","caTools","","questionr","ROCR","caret"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends","Suggests"))

install.packages(c("sf"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
install.packages(c("rgdal"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
install.packages(c("tigris"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
install.packages(c("choroplethr","choroplethrMaps"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends", "Suggests"))
install.packages(c( "uroot"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))

install.packages(c("quantmod","quadprog","tseries","fracdiff","urca","forecast"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))

install.packages(c("config", "tfruns","tensorflow"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))
install.packages(c("zeallot","keras"), lib="/usr/local/lib/R/site-library", dependencies = c("Depends"))

update.packages(lib.loc = "/usr/local/lib/R/site-library",check.built=TRUE,ask=FALSE)

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


