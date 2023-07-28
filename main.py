from flask import Flask, request
from cv import *
from utils import *
from ocr import *
from llm import *

app = Flask(__name__)


@app.route('/', methods=['POST'])
def image_to_items():
    file = request.data

    jpg_as_np = np.frombuffer(file, dtype=np.uint8)
    image = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)

    print(image)

    image = image_normalize(image)
    angle, image = correct_skew(image)
    image = remove_noise(image)
    image = bw_scanner(image)

    extracted_text = image_to_string(image, lang='rus+eng')
    prompt = bild_prompt_for_gpt(extracted_text)
    posison = gpt_process(prompt)

    items = content_str_to_dict(posison)

    return items

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')