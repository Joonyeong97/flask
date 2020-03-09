
def delete_cd(filename):
    import os
    file = 'static/customer_img'
    os.remove(file+'/{}'.format(filename))

def panbyul(name):
    if name == '강아지':
        name = 'dog.jpg'
    if name == '고양이':
        name = 'cat.jpg'
    return name

def cat_dog(filename):
    from PIL import Image
    import glob
    import numpy as np
    from keras.models import load_model

    caltech_dir = "static/customer_img/"
    image_w = 100
    image_h = 100

    X = []
    filenames = []
    files = glob.glob(caltech_dir + filename)
    # files = glob.glob(caltech_dir+"/*.*")
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)
        filenames.append(f)
        X.append(data)

    X = np.array(X)
    X = X.reshape(X.shape[0], 100, 100, 1)
    model = load_model('model/multi_img_classification.model')

    prediction = model.predict(X)
    cnt = 0

    # 이 비교는 그냥 파일들이 있으면 해당 파일과 비교. 카테고리와 함께 비교해서 진행하는 것은 _4 파일.
    for i in prediction:
        pre_ans = i.argmax()  # 예측 레이블
        pre_ans_str = ''
        if pre_ans == 1:
            pre_ans_str = "강아지"
        else:
            pre_ans_str = "고양이"
        if i[0] == 1:
            dap = pre_ans_str
        if i[1] == 1:
            dap = pre_ans_str
        cnt += 1
    delete_cd(filename)
    return dap