


def sysend():
    import sys
    import time
    time.sleep(1)
    sys.stdout.flush()

def fare_(Fare):
    if Fare <= 7.91:
        Fare = 0

    elif Fare >= 7.92 and Fare <= 14.454:
        Fare = 1

    elif Fare >= 14.455 and Fare <= 31:
        Fare = 2

    elif Fare >= 32:
        Fare = 3
    return Fare


def age_(age):
    if age <= 16:
        age = 0

    elif age >= 17 and age <= 32:
        age = 1

    elif age >= 33 and age <= 48:
        age = 2

    elif age >= 49 and age <= 64:
        age = 3

    elif age >= 65:
        age = 4
    return age


def titanic_m(pclass, sex, age, Fare, embarked, name, isalone):
    import pandas as pd
    from sklearn.externals import joblib
    titanic = joblib.load('model/titanic.pkl')
    pclass = int(pclass)
    sex = int(sex)
    age = int(age)
    Fare = int(Fare)
    embarked = int(embarked)
    name = int(name)
    isalone = int(isalone)


    age_(age)
    fare_(Fare)
    a = [pclass, sex, age, Fare, embarked, name, isalone]
    a = list(map(int, a))
    a.append(a[0] * a[2])
    column = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Title', 'IsAlone', 'Age*Class']
    qq = pd.DataFrame(a, index=column).T


    pred = titanic.predict(qq)
    if pred[0] == 1:
        pa = '생존입니다.'
    else:
        pa = '사망입니다.'

    return pa
