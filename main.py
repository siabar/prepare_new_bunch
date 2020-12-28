# Press the green button in the gutter to run the script.
import argparse
import os
from shutil import copyfile

def read_removed_files(removed_path):
    removed_f = open(removed_path, 'r')
    listOfFiles = []
    for file in removed_f:
        listOfFiles.append(file.split("/")[-1].strip() + ".txt")
    return listOfFiles

def read_corpora_files(files):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(files):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames if file.endswith(".txt")]
    return listOfFiles

def read_annptated_files(files):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(files):
        listOfFiles += [file for file in filenames if file.endswith(".txt")]
    return listOfFiles


def selected_reports(list_origin, list_annptated_files, list_removed_files, needed_reports):
    counter = 1
    listofFiles = []
    for file in list_origin:
        nameFile = file.split("/")[-1]
        if nameFile not in list_annptated_files and nameFile not in list_removed_files:
            if counter <= needed_reports:
                listofFiles.append(file)
                counter += 1
            else:
                break
    return listofFiles


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="performance checker")
    parser.add_argument('--origin', help='Corpora')
    parser.add_argument('--annotated_files', help='annotated files by annotators')
    parser.add_argument('--removed_files', help='removed files by annotators')
    parser.add_argument('--output', help='output')

    args = parser.parse_args()

    origin = args.origin
    annotated_files = args.annotated_files
    removed_files = args.removed_files
    output = args.output

    list_origin = read_corpora_files(origin)
    print(len(list_origin))
    list_annotated_files = read_annptated_files(annotated_files)
    print(len(list_annotated_files))
    list_removed_files = read_removed_files(removed_files)
    print(len(list_removed_files))

    list_output_file = selected_reports(list_origin, list_annotated_files, list_removed_files, 100)
    for file in list_output_file:
        nameFile = file.split("/")[-1]
        outputFile = os.path.join(output, nameFile)
        copyfile(file, outputFile)



