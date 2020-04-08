import argparse
import os
from xml_utils import construct_voc_xml
from shutil import copyfile

DATASETS_FOLDERS = ['validation', 'test', 'train']
LABEL_FOLDER_NAME = 'Label'
TF_FOLDER_NAME = 'images'


def get_img_ids(folder):
    ids = []
    for file in os.listdir(folder):
        if os.path.splitext(file)[1] == '.jpg':
            ids.append(os.path.splitext(file)[0])
    return ids


def get_obj_names(folder):
    objs = []
    if os.path.isdir(folder):
        objs = [f.name for f in os.scandir(folder) if f.is_dir()]
    return objs


def main(args):
    os.makedirs(os.path.join(args.output_dir, TF_FOLDER_NAME), exist_ok=True)

    for dataset in DATASETS_FOLDERS:
        if dataset == DATASETS_FOLDERS[0] and not args.ignore_val:
            continue
        
        if os.path.isdir(os.path.join(args.input_dir, dataset)):
            if dataset == DATASETS_FOLDERS[0] or dataset == DATASETS_FOLDERS[2]:
                os.makedirs(os.path.join(args.output_dir, TF_FOLDER_NAME, DATASETS_FOLDERS[2]), exist_ok=True)
            else:
                os.makedirs(os.path.join(args.output_dir, TF_FOLDER_NAME, dataset), exist_ok=True)



            objs = get_obj_names(os.path.join(args.input_dir, dataset))
            for obj in objs:
                ids = get_img_ids(os.path.join(args.input_dir, dataset, obj))
                for counter, item in enumerate(ids):
                    if dataset == DATASETS_FOLDERS[0]:
                        dest_file = os.path.join(
                            args.output_dir, TF_FOLDER_NAME, DATASETS_FOLDERS[2], '{}_{}_{}.jpg'.format(obj, DATASETS_FOLDERS[0], counter))
                        construct_voc_xml(args.input_dir, args.output_dir,
                                        dataset, DATASETS_FOLDERS[2], obj, item, counter)

                    else:
                        dest_file = os.path.join(
                            args.output_dir, TF_FOLDER_NAME, dataset, '{}_{}_{}.jpg'.format(obj, dataset, counter))
                        construct_voc_xml(
                            args.input_dir, args.output_dir, dataset, dataset, obj, item, counter)

                    input_file = os.path.join(
                        args.input_dir, dataset, obj, item+'.jpg')
                    print(input_file, dest_file)
                    copyfile(input_file, dest_file)


if __name__ == "__main__":
    # creating argument parser
    parser = argparse.ArgumentParser(
        description='OpenImages to TensorFlow format converter')

    # adding arguments
    parser.add_argument('-i',
                        '--input_dir',
                        help='Path to input OpenImages directory',
                        type=str,
                        required=True)
    parser.add_argument('-o',
                        '--output_dir',
                        help='Path to input OpenImages directory',
                        type=str,
                        required=True)
    parser.add_argument('-v',
                        '--ignore_val',
                        help='Ignore validation images, default=False',
                        action='store_false')
    args = parser.parse_args()

    assert os.path.isdir(os.path.dirname(
        args.input_dir)), 'ERROR: No such input directory {} '.format(args.input_dir)
    assert os.path.isdir(os.path.dirname(
        args.output_dir)), 'ERROR: No such output directory {} '.format(args.output_dir)
    main(args)
