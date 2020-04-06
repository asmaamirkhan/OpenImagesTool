import argparse
import cv2
import xml.etree as tree

def get_ids(folder):
    for file in os.listdir(folder):
        fi

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
                        '--validation',
                        help='Add validation images to train directory (boolean), default',
                        default=True,
                        type=float)
    args = parser.parse_args()

    assert os.path.isdir(os.path.dirname(
        args.input_dir)), 'ERROR: No such input directory {} '.format(args.input_dir)
    assert os.path.isdir(os.path.dirname(
        args.output_dir)), 'ERROR: No such output directory {} '.format(args.output_dir)

    main(args)
