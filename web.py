from flask import Flask, request
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# 以下資訊可以從 Azure 電腦視覺服務取得(正式上線時不要直接把金鑰跟服務端點寫在程式碼裡)
KEY = '' # 填入金鑰
ENDPOINT = '' # 填入端點

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def object_detection():
    IMAGE = request.args.get('image')
    LANG = request.args.get('language')

    client = ComputerVisionClient(
        endpoint=ENDPOINT,
        credentials=CognitiveServicesCredentials(KEY)
    )
    
    analysis = client.describe_image(url=IMAGE, max_descriptions=1, language=LANG)
    result = analysis.captions[0]
    return "{} [{}]".format(result.text, result.confidence)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
