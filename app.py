#  參考文件
#  https://learn.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python-previous
import os
import pathlib
from dotenv import load_dotenv
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# 如果.env存在，讀取.env檔案
env_path = pathlib.Path(".env")
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# 取得環境變數
KEY = os.getenv('KEY')
ENDPOINT = os.getenv('ENDPOINT')

client = ComputerVisionClient(
    endpoint=ENDPOINT,
    credentials=CognitiveServicesCredentials(KEY)
)

IMAGE = 'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg' # 影像
LANG = 'en' # 描述語言
MAX = 1 # 產生的最大描述數量

analysis = client.describe_image(url=IMAGE, max_descriptions=MAX, language=LANG)

for caption in analysis.captions:
    print(caption.text)
    print(caption.confidence)
