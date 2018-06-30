import numpy as np
import cv2
import os
import pandas as pd
import fnmatch
from six.moves import cPickle 

# For this problem the validation and test data provided by the concerned authority did not have labels, so the training data was split into train, test and validation sets
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
train_dir = os.path.join(__location__,'dataset_sample')

X_train = []
y_age = []
y_gender = []

df = pd.read_csv(os.path.join(train_dir,'dataset_sample_labels.csv'))
a = df.values
m = a.shape[0]

path = train_dir + '\\'
print('Loading data set...')
for i in os.listdir(path):
    if fnmatch.fnmatch(i, '*.png'):
        y_age.append(df.boneage[df.id == int(i[:-4])].tolist()[0])
        a = df.male[df.id == int(i[:-4])].tolist()[0]
        if a:
            y_gender.append(1)
        else:
            y_gender.append(0)
        img_path = path + i
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224, 224))
        x = np.asarray(img, dtype=np.uint8)
        X_train.append(x)

print('')
print('100% completed loading data')

print('')
print('Saving data...')
# Save data
train_pkl = open('data.pkl', 'wb')
cPickle.dump(X_train, train_pkl, protocol=cPickle.HIGHEST_PROTOCOL)
train_pkl.close()

train_age_pkl = open('data_age.pkl', 'wb')
cPickle.dump(y_age, train_age_pkl, protocol=cPickle.HIGHEST_PROTOCOL)
train_age_pkl.close()

train_gender_pkl = open('data_gender.pkl', 'wb')
cPickle.dump(y_gender, train_gender_pkl, protocol=cPickle.HIGHEST_PROTOCOL)
train_gender_pkl.close()
print('')
print('100% completed saved data')
