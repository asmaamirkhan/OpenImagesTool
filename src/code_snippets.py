# author ~ Asmaa 2020
import os
import xml.etree.ElementTree as ET


def string_replacer(source, old_string, new_string):
    """ Replaces a string in all .txt files in given directory

    Arguments:
    source -- path of source directory
    old_string -- string to be replaced
    new_stirng -- value of new string

    """
    for filename in os.listdir(source):
        with open(os.path.join(source, filename), 'r+') as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(old_string, new_string))


def xml_replacer(source, tag, value):
    """ Replaces a specific tag value in all xml files in given directory

    Arguments:
    source -- path of source directory
    tag -- xml tag that its value will change
    value -- value of the tag    
    """

    for filename in os.listdir(source):
        if not filename.endswith('.xml'):
            continue
        fullname = os.path.join(source, filename)
        tree = ET.parse(fullname)
        tree.find(tag).text = value
        tree.write(fullname)


def file_renamer(source, dest, extension, prefix=''):
    """ rename all files that have given extension in given directory 

    Arguments:
    source -- path of source directory
    dest -- destnation directory path
    extesnion -- target extension
    prefix -- prefix to be written in new filename    
    """
    for counter, filename in enumerate(os.listdir(source)):
        if filename.endswith(extension):
            os.rename(os.path.join(source, filename), os.path.join(
                dest, '{}{}{}'.format(prefix, counter, extension)))
