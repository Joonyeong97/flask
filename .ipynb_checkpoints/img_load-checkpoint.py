
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

    for i in prediction:
        pre_ans_str = ''
        if i[0] >= 0.5:
            pre_ans_str = "강아지"
            dap = pre_ans_str
        if i[1] >= 0.5:
            pre_ans_str = "고양이"
            dap = pre_ans_str
    delete_cd(filename)
    return dap