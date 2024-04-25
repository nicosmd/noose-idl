#!/bin/python3

import argparse
import os
import sys
import pathlib

from rosidl.rosidl_adapter import convert_to_idl


def convert_rosidl_to_idl(input_dir, package_name, file, output_dir):
    convert_to_idl(pathlib.Path(input_dir), package_name, pathlib.Path(file), pathlib.Path(output_dir))


def get_all_rosidl_files(input_dir):
    rosidl_files = os.listdir(input_dir)
    return rosidl_files


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Noose IDL Generator')
    parser.add_argument('--package-name', required=True, help='The name of the package name')
    parser.add_argument('--input-dir', required=True,
                        help='Noose IDL input directory. Generate interfaces for all IDL files in this directory.')
    parser.add_argument('--cpp-output-dir', help='generated C++ code output directory.', default='generated')
    parser.add_argument('--idl-output-dir', help='idl output directory.', default='idl')

    args = parser.parse_args(argv)

    input_dir = args.input_dir
    package_name = args.package_name
    cpp_output_dir = args.cpp_output_dir
    idl_output_dir = args.idl_output_dir

    for rosidl_file in get_all_rosidl_files(args.input_dir):
        convert_rosidl_to_idl(input_dir, package_name, rosidl_file, idl_output_dir)


if __name__ == '__main__':
    main()
