def delete_cd(filename):
    import os
    file = 'static/customer_img'
    os.remove(file+'/{}'.format(filename))

def facescore(name):
    import cv2
    from matplotlib import pyplot as plt
    import numpy as np

    from keras.models import load_model

    import glob
    plt.style.use('dark_background')

    model = load_model('model/facemodel.h5')
    img_test_list = glob.glob('static/customer_img/{}'.format(name))

    imgs_test_resized = []

    img = cv2.imread(img_test_list[0])
    img_resized = cv2.resize(img, (350, 350))


    img_resized = img_resized.astype(np.float32) / 255.
    imgs_test_resized.append(img_resized)

    imgs_test_resized = np.array(imgs_test_resized, dtype=np.float32)


    preds = model.predict(imgs_test_resized)
    plt.figure(figsize=(7,5))

    plt.title('%.2f score / 4.5 Max score' % (preds[0]),fontsize=35)
    img = cv2.cvtColor(imgs_test_resized[0], cv2.COLOR_BGR2RGB)
    plt.imshow(img.squeeze())

    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.savefig("static/face/{}".format(name), bbox_inces='tight', dpi=400, pad_inches=0)
    delete_cd(name)

    if preds[0] <= 3.0:
        jum = '점수는 숫자에 불과합니다.'
    elif preds[0] >= 3.0 or preds[0] <= 3.99:
        jum = '좋은 인상을 가지셨네요!'
    elif preds[0] >= 4.0:
        jum = '정말 퍼펙트한 인상입니다.'
    return jum