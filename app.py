#  參考文件
#  https://learn.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python-previous
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# 以下資訊可以從 Azure 電腦視覺服務取得(正式上線時不要直接把金鑰跟服務端點寫在程式碼裡)
KEY = '[填入金鑰]' # 金鑰
ENDPOINT = '[填入服務端點]' # 服務端點

client = ComputerVisionClient(
    endpoint=ENDPOINT,
    credentials=CognitiveServicesCredentials(KEY)
)

IMAGE = "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg" # 影像
LANG = "en" # 描述語言
MAX = 1 # 產生的最大描述數量

analysis = client.describe_image(url=IMAGE, max_descriptions=MAX, language=LANG)

for caption in analysis.captions:
    print(caption.text)
    print(caption.confidence)
