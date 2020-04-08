# 🌌 OpenImages Tool
A tool to convert OpenImages dataset format to TensorFlow-friendly format;
- ➰ Convert xml to VOC format
- 🚀 Make directory structure suitable to be used in TensorFlow custom object training
- 👩‍💻 Use presented [Code Snippets](./src/code_snippets.py) for other organizing operations
  - `string_replacer`
  - `xml_replacer`
  - `file_renamer` 

## 🏗️ Required Directory Structure
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
> 📢 validation, test, train and Label are required **fix** keywords

## 🎉 Result Directory Structure
```
images
|___ test
|    |___ <object_name>_test_<id>.xml
|    |___ <object_name>_test_<id>.jpg
|    |___ ....
|
|___ train
     |___ <object_name>_train_<id>.xml
     |___ <object_name>_train_<id>.jpg
     |___ ....

```

## 👩‍💻 Usage
1. Clone this repository
2. Organize your data to be like the required
3. Open [src](./src) folder in CMD
4. Run: 
```bash
 src> python script.py -i <INPUT_PATH> -o <OUTPUT_PATH>
```
👮‍♀️ This command will add validation set to training set folder, if you want to disable this behavior then run:

```bash
 src> python script.py -i <INPUT_PATH> -o <OUTPUT_PATH> -v
```
👀 To see running options, run: 
```bash
src> python script.py -h
```

## 📖 References
- [OIDv4_ToolKit](https://github.com/EscVM/OIDv4_ToolKit)
- [OIDv4_to_VOC](https://github.com/AtriSaxena/OIDv4_to_VOC/blob/master/OIDv4_to_VOC.py)


## 💼 Contact & Support
Find me on [LinkedIn](https://www.linkedin.com/in/asmaamirkhan/) and feel free to mail me, [Asmaa 🦋](mailto:asmaamirkhan.am@gmail.com)