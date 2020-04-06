# 🛍️ OpenImages Tool
A tool to make OpenImages data Tensorflow-friendly

## ⚠️ Required File Organization
```
Dataset
|___ validation
|    |___ <object_name>
|          |___ Label
|          |    |___ <validation_label_file_name>.txt
|          |    |___ ....
|          |___ <validation_image_file_name>.jpg
|          |___ ....
|
|___ test
|    |___ <object_name>
|          |___ Label
|          |    |___ <validation_label_file_name>.txt
|          |    |___ ....
|          |___ <validation_image_file_name>.jpg
|          |___ ....
|
|___ train
     |___ <object_name>
           |___ Label
           |    |___ <validation_label_file_name>.txt
           |    |___ ....
           |___ <validation_image_file_name>.jpg
           |___ ....

```
> 📢 validation, test, train and Label are required keywords

## 🎉 Result File Organization
```
images
|___ test
|    |___ <object_name_1>_test.xml
|    |___ <object_name_1>_test.jpg
|    |___ ....
|
|___ train
     |___ <object_name_1>_train.xml
     |___ <object_name_1>_train.jpg
     |___ ....

```
