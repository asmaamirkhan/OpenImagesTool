# author ~ Asmaa 2020
import argparse
import os
from xml_utils import construct_voc_xml
from shutil import copyfile

DATASETS_FOLDERS = ['validation', 'test', 'train']
LABEL_FOLDER_NAME = 'Label'
TF_FOLDER_NAME = 'images'


def get_img_ids(folder):
    """ returns unique file names in source image directory

    Arguments:
    folder -- path of source directory

    Returns:
    ids -- list of file names
    """

    ids = []
    for file in os.listdir(folder):
        if os.path.splitext(file)[1] == '.jpg':
            ids.append(os.path.splitext(file)[0])
    return ids


def get_obj_names(folder):
    """ returns object names in dataset directory

    Arguments:
    folder -- path of source directory

    Returns:
    objs -- list of object names
    """
    objs = []
    if os.path.isdir(folder):
        objs = [f.name for f in os.scandir(folder) if f.is_dir()]
    return objs


def main(args):
    # create main folder that will contain all files
    os.makedirs(os.path.join(args.output_dir, TF_FOLDER_NAME), exist_ok=True)

    # iter over splitted datasets
    for dataset in DATASETS_FOLDERS:
        # check validation -> train argument
        if dataset == DATASETS_FOLDERS[0] and not args.ignore_val:
            continue

        if os.path.isdir(os.path.join(args.input_dir, dataset)):
            # create targer folders
            if dataset == DATASETS_FOLDERS[0] or dataset == DATASETS_FOLDERS[2]:
                os.makedirs(os.path.join(args.output_dir,
                                         TF_FOLDER_NAME, DATASETS_FOLDERS[2]), exist_ok=True)
            else:
                os.makedirs(os.path.join(args.output_dir,
                                         TF_FOLDER_NAME, dataset), exist_ok=True)

            # extract object names
            objs = get_obj_names(os.path.join(args.input_dir, dataset))

            # iterate over object directories
            for obj in objs:

                # extract ids from object directories
                ids = get_img_ids(os.path.join(args.input_dir, dataset, obj))
                for counter, item in enumerate(ids):
                    # specify source image path
                    input_file = os.path.join(
                        args.input_dir, dataset, obj, item+'.jpg')

                    # specify target image path
                    if dataset == DATASETS_FOLDERS[0]:
                        dest_file = os.path.join(
                            args.output_dir, TF_FOLDER_NAME, DATASETS_FOLDERS[2], '{}_{}_{}.jpg'.format(obj, DATASETS_FOLDERS[0], counter))

                        # create xml file
                        construct_voc_xml(args.input_dir, args.output_dir,
                                          dataset, DATASETS_FOLDERS[2], obj, item, counter)

                    else:
                        dest_file = os.path.join(
                            args.output_dir, TF_FOLDER_NAME, dataset, '{}_{}_{}.jpg'.format(obj, dataset, counter))
                        construct_voc_xml(
                            args.input_dir, args.output_dir, dataset, dataset, obj, item, counter)

                    print(input_file, dest_file)

                    # copy image file
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
