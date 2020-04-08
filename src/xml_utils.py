# author ~ Asmaa 2020

from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.etree.cElementTree as ET
import cv2
import os

TF_FOLDER_NAME = 'images'
LABEL_FOLDER_NAME = 'Label'

""" Constructs xml file and saves it to dest folder 

    Arguments:
    input_dir -- path of source directory
    output_dir -- path of output directory
    in_dataset -- name of source dataset
    out_dataset -- name of target dataset
    obj -- name of object 
    item -- ID of source file item
    counter -- value of file iterator in source folder to be added to saved file name    
"""
def construct_voc_xml(input_dir, output_dir, in_dataset, out_dataset, obj, item, counter):

    # input text path
    txt_path = os.path.join(input_dir, in_dataset, obj,
                            LABEL_FOLDER_NAME, item+'.txt')

    # input image path
    img_path = os.path.join(input_dir, in_dataset, obj, item+'.jpg')

    # output xml path
    xml_path = os.path.join(output_dir, TF_FOLDER_NAME, out_dataset,
                            '{}_{}_{}.xml'.format(obj, out_dataset, counter))

    # open source text file 
    txt_file = open(txt_path)

    # open image with opencv to get width and height 
    img_file = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # create root tag of xml file
    root_tag = Element('annotation')

    # add sub elements
    folder_tag = SubElement(root_tag, 'folder')
    folder_tag.text = obj

    filename_tag = SubElement(root_tag, 'filename')
    filename_tag.text = '{}_{}_{}'.format(obj, out_dataset, counter)

    path_tag = SubElement(root_tag, 'path')
    path_tag.text = os.path.join(output_dir, TF_FOLDER_NAME, out_dataset,
                                 '{}_{}_{}.jpg'.format(obj, out_dataset, counter))

    source_tag = SubElement(root_tag, 'source')

    db_tag = SubElement(source_tag, 'database')
    db_tag.text = 'Unknown'

    size_tag = SubElement(root_tag, 'size')
    width_tag = SubElement(size_tag, 'width')

    # extract width value from opencv image
    width_tag.text = str(img_file.shape[1]) 

    height_tag = SubElement(size_tag, 'height')
    
    # extract height value from opencv image
    height_tag.text = str(img_file.shape[0])

    depth_tag = SubElement(size_tag, 'depth')
    if len(img_file.shape) == 3:
        depth_tag.text = str(img_file.shape[2])
    else:
        depth_tag.text = '3'

    seg_tag = SubElement(root_tag, 'segmented')
    seg_tag.text = '0'

    for line in txt_file:
        # format <object_name> <xmin> <ymin> <xmax> <ymax>
        # example: Bell pepper 5.12 56.94018 1023.36 681.3602841
        # split every line into string list
        details = list(line.split())
        obj_tag = SubElement(root_tag, 'object')

        name_tag = SubElement(obj_tag, 'name')
        
        # get all elements before coordinates in list
        sub = details[:-4]
        name_tag.text = (''.join(str(e + ' ') for e in sub))[:-1]

        pose_tag = SubElement(obj_tag, 'pose')
        pose_tag.text = 'Unspecified'

        trun_tag = SubElement(obj_tag, 'truncated')
        trun_tag.text = '0'

        diff_tag = SubElement(obj_tag, 'difficult')
        diff_tag.text = '0'

        box_tag = SubElement(obj_tag, 'bndbox')
        xmin_tag = SubElement(box_tag, 'xmin')
        xmin_tag.text = str(int(float(details[-4])))

        ymin_tag = SubElement(box_tag, 'ymin')
        ymin_tag.text = str(int(float(details[-3])))

        xmax_tag = SubElement(box_tag, 'xmax')
        xmax_tag.text = str(int(float(details[-2])))

        ymax_tag = SubElement(box_tag, 'ymax')
        ymax_tag.text = str(int(float(details[-1])))

    # convert root tag to dom
    dom = minidom.parseString(tostring(root_tag))
    
    # format root tag
    formatted_xml = dom.toprettyxml()
    
    # create xml tree from root tag 
    tree = ET.ElementTree(ET.fromstring(formatted_xml))

    # save xml file
    tree.write(xml_path)
