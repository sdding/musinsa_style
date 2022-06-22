from flask import Flask, render_template, request
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from PIL import Image
import io

app = Flask(__name__)

model = load_model('./ResNet_model.h5')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        
        return render_template('index.html')

    if request.method == 'POST':
        img = request.files["file"].read()
        img = Image.open(io.BytesIO(img))
        img = img.resize((256, 256))
        img = img_to_array(img)
        img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
        
        pred = model.predict(img)
        label = pred.argmax()
        style = ['걸리시', '댄디', '로맨틱', '스트릿', '스포츠', '시크', '캐주얼', '포멀']
        return render_template("result.html", img = img, label=style[label])