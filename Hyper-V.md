# Hyper-V 網路設定

1. 在Hyper-V管理員的**虛擬交換器管理員**中，新增一個外部(External)網路虛擬交換器，並選擇相對應的網卡(外網網卡)
2. 本機網卡處會新增一個vEthernet
3. 在VM內設定外網IP
4. 在外網網卡處，點選**內容** -> **共用** -> **設定**，打開共用的port

# Hyper-V防火牆設定 @ubuntu
0. 看防火牆是否開啟
`sudo ufw status`

1. 打開防火牆
`sudo ufw enable`

2. 打開需要的port
`sudo ufw allow ssh` 或是 `sudo ufw allow 3939` 之類的
