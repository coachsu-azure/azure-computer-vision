# azure-computer-vision
Azure AI服務：電腦視覺測試範例

# 測試環境設定
 1. [建議] 先建立虛擬環境
 2. 安裝需要的套件

    `pip install -r requirements.txt`
 
# 修改環境變數
將 Azure AI 電腦視覺的金鑰與服務端點寫入環境變數檔案(`.env`)

 # 測試單機執行程式(app.py)
1. 依據需要修改app.py (例如，影像來源、描述語言)
2. 執行 app.py

   `python app.py`

# 測試 flask API 服務(api.py)
1. 執行 api.py

    `python api.py`
2. 開啟瀏覽器並前往 http://127.0.0.1:8080?language=en&image=https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg

# 測試網頁頁用程式(web.py)
1. 執行 web.py

   `python web.py`
2. 開啟瀏覽器並前往 http://127.0.0.1:8080

# 練習
1. 將 web.py 部署到 Azure Virtual Machine。
2. 將 web.py 部署到 Azure Contrainer Instance。
3. 將 api.py 部署到 Azure Function。