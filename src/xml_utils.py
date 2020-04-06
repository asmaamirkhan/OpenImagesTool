from xml.etree.ElementTree import Element, SubElement, Comment
import xml.etree.cElementTree as ET
import cv2
import os

TF_FOLDER_NAME = 'images'
LABEL_FOLDER_NAME = 'Label'


def construct_voc_xml(dataset, obj, item, input_dir, output_dir):
    txt_path = os.path.join(input_dir, dataset, obj,
                            LABEL_FOLDER_NAME, item+'.txt')
    img_path = os.path.join(input_dir, dataset, obj, item+'.jpg')

    xml_path = os.path.join(output_dir, TF_FOLDER_NAME, item+'.xml')

    txt_file = open(txt_path)
    img_file = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    root_tag = Element('annotation')

    folder_tag = SubElement(root_tag, 'folder')
    folder_tag.text = obj

    filename_tag = SubElement(root_tag, 'filename')
    filename_tag.text = item+'.jpg'

    path_tag = SubElement(root_tag, 'path')
    path_tag.text = img_path

    source_tag = SubElement(root_tag, 'source')

    db_tag = SubElement(source_tag, 'database')
    db_tag.text = 'Unknown'

    size_tag = SubElement(root_tag, 'size')
    width_tag = SubElement(size_tag, 'width')
    width_tag.text = str(img_file.shape[1])

    height_tag = SubElement(size_tag, 'height')
    height_tag.text = str(img_file.shape[0])

    depth_tag = SubElement(size_tag, 'depth')
    if len(img_file.shape) == 3:
        depth_tag.text = str(img_file.shape[2])
    else:
        depth_tag.text = '3'

    seg_tag = SubElement(root_tag, 'segmented')
    seg_tag.text = '0'

    for line in txt_file:
        details = list(line.split())
        obj_tag = SubElement(root_tag, 'object')

        name_tag = SubElement(obj_tag, 'name')
        name_tag.text = details[0].replace(' ', '_')

        pose_tag = SubElement(obj_tag, 'pose')
        pose_tag.text = 'Unspecified'

        trun_tag = SubElement(obj_tag, 'truncated')
        trun_tag.text = '0'

        diff_tag = SubElement(obj_tag, 'difficult')
        diff_tag.text = '0'

        box_tag = SubElement(obj_tag, 'bndbox')
        xmin_tag = SubElement(box_tag, 'xmin')
        xmin_tag.text = str(int(details[1]))

        ymin_tag = SubElement(box_tag, 'ymin')
        ymin_tag.text = str(int(details[2]))

        xmax_tag = SubElement(box_tag, 'xmax')
        xmax_tag.text = str(int(details[3]))

        ymax_tag = SubElement(box_tag, 'ymax')
        ymax_tag.text = str(int(details[4]))

    tree = ET.ElementTree(root_tag)
    tree.write(xml_path)
