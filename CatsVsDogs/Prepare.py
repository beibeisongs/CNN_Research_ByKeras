# encoding=utf-8
# Date: 2018-09-27
# Author: MJUZY


import os
import shutil


original_dataset_dir = "D:/Learning_Process_Keras/kaggle/train"

base_dir = "D:\Learning_Process_Keras\cats_and_dogs_small"
if not os.path.exists(base_dir):
    os.mkdir(base_dir)

train_dir = os.path.join(base_dir, "train")
if not os.path.exists(train_dir):
    os.mkdir(train_dir)

validation_dir = os.path.join(base_dir, "validation")
if not os.path.exists(validation_dir):
    os.mkdir(validation_dir)

test_dir = os.path.join(base_dir, "test")
if not os.path.exists(test_dir):
    os.mkdir(test_dir)

train_cats_dir = os.path.join(train_dir, "cats")
if not os.path.exists(train_cats_dir):
    os.mkdir(train_cats_dir)

train_dogs_dir = os.path.join(train_dir, "dogs")
if not os.path.exists(train_dogs_dir):
    os.mkdir(train_dogs_dir)

validation_cats_dir = os.path.join(validation_dir, "cats")
if not os.path.exists(validation_cats_dir):
    os.mkdir(validation_cats_dir)

validation_dogs_dir = os.path.join(validation_dir, "dogs")
if not os.path.exists(validation_dogs_dir):
    os.mkdir(validation_dogs_dir)

test_cats_dir = os.path.join(test_dir, "cats")
if not os.path.exists(test_cats_dir):
    os.mkdir(test_cats_dir)

test_dogs_dir = os.path.join(test_dir, "dogs")
if not os.path.exists(test_dogs_dir):
    os.mkdir(test_dogs_dir)

if len(os.listdir(train_cats_dir)) == 0:

    line_i = 0
    fnames = ["cat.{}.jpg".format(i) for i in range(1000)]
    for fname in fnames:
        line_i += 1
        print(line_i)
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(train_cats_dir, fname)
        shutil.copyfile(src, dst)
else:
    print("total training cat images : ", len(os.listdir(train_cats_dir)))

if len(os.listdir(validation_cats_dir)) == 0:

    line_i = 0
    fnames = ["cat.{}.jpg".format(i) for i in range(1000, 1500)]
    for fname in fnames:
        line_i += 1
        print(line_i)
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(validation_cats_dir, fname)
        shutil.copyfile(src, dst)
else:
    print("total validation cat images : ", len(os.listdir(validation_cats_dir)))

if len(os.listdir(test_cats_dir)) == 0:

    line_i = 0
    fnames = ["cat.{}.jpg".format(i) for i in range(1500, 2000)]
    for fname in fnames:
        line_i += 1
        print(line_i)
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(test_cats_dir, fname)
        shutil.copyfile(src, dst)
else:
    print("total test cat images : ", len(os.listdir(test_cats_dir)))

if len(os.listdir(train_dogs_dir)) == 0:

    line_i = 0
    fnames = ["dog.{}.jpg".format(i) for i in range(1000)]
    for fname in fnames:
        line_i += 1
        print(line_i)
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(train_dogs_dir, fname)
        shutil.copyfile(src, dst)
else:
    print("total train dogs images : ", len(os.listdir(train_dogs_dir)))

if len(os.listdir(validation_dogs_dir)) == 0:

    line_i = 0
    fnames = ["dog.{}.jpg".format(i) for i in range(1000, 1500)]
    for fname in fnames:
        line_i += 1
        print(line_i)
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(validation_dogs_dir, fname)
        shutil.copyfile(src, dst)
else:
    print("total validation dogs images : ", len(os.listdir(validation_dogs_dir)))

if len(os.listdir(test_dogs_dir)) == 0:

    line_i = 0
    fnames = ["dog.{}.jpg".format(i) for i in range(1500, 2000)]
    for fname in fnames:
        line_i += 1
        print(line_i)
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(test_dogs_dir, fname)
        shutil.copyfile(src, dst)
else:
    print("total test dogs images : ", len(os.listdir(test_dogs_dir)))
