#!/bin/python3

import argparse
import os
import sys
import pathlib

from rosidl.rosidl_adapter import convert_to_idl
from rosidl.rosidl_pycommon import generate_files_noose
from rosidl.rosidl_generator_type_description import generate_type_hash_noose
import template_cmake

from rosidl import rosidl_generator_c
from rosidl import rosidl_generator_cpp
from rosidl.resource import rosidl_typesupport_introspection_cpp


def convert_rosidl_to_idl(input_dir, package_name, file, output_dir):
    if file.endswith(".msg") or file.endswith(".action") or file.endswith(".srv"):
        convert_to_idl(pathlib.Path(input_dir), package_name, pathlib.Path(file),
                       pathlib.Path(output_dir) / package_name)


def get_all_rosidl_files(input_dir):
    rosidl_files = os.listdir(input_dir)
    return rosidl_files


def collect_idl_files(directory):
    idl_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".idl"):
                idl_files.append(os.path.join(root, file))

    return idl_files


def collect_all_idl_files(input_dir, idl_dir):
    idl_files = collect_idl_files(idl_dir)
    idl_files += collect_idl_files(input_dir)
    return idl_files


def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)


def generate_cpp_typesupport_fastrtps(idl_files, output_dir, package_name):
    mapping = {
        'idl__rosidl_typesupport_fastrtps_cpp.hpp.em':
            'detail/%s__rosidl_typesupport_fastrtps_cpp.hpp',
        'idl__type_support.cpp.em': 'detail/dds_fastrtps/%s__type_support.cpp',
    }

    generated_files = generate_files_noose(idl_files, mapping, "rosidl_typesupport_fastrtps_cpp", package_name,
                                           output_dir)

    from rosidl.resource.rosidl_typesupport_fastrtps_cpp import template_visibility_control_h
    visibility_file_path = os.path.join(output_dir, "msg", "rosidl_typesupport_fastrtps_cpp__visibility_control.h")
    write_file(visibility_file_path, template_visibility_control_h.render(package_name, package_name.upper()))

    generated_files.append(visibility_file_path)

    return generated_files


def generate_cpp_typesupport_introspection(idl_files, output_dir, package_name):
    mapping = {
        'idl__rosidl_typesupport_introspection_cpp.hpp.em':
            'detail/%s__rosidl_typesupport_introspection_cpp.hpp',
        'idl__type_support.cpp.em': 'detail/%s__type_support.cpp',
    }

    return generate_files_noose(idl_files, mapping, "rosidl_typesupport_introspection_cpp", package_name, output_dir)


def generate_cpp(idl_files, output_dir, package_name):
    mapping = {
        'idl.hpp.em': '%s.hpp',
        'idl__builder.hpp.em': 'detail/%s__builder.hpp',
        'idl__struct.hpp.em': 'detail/%s__struct.hpp',
        'idl__traits.hpp.em': 'detail/%s__traits.hpp',
        'idl__type_support.hpp.em': 'detail/%s__type_support.hpp',
    }

    generate_files = generate_files_noose(idl_files, mapping, "rosidl_generator_cpp", package_name, output_dir)
    from rosidl.resource.rosidl_generator_cpp import template_visibility_control_hpp
    visibility_file_path = os.path.join(output_dir, "msg", "rosidl_generator_cpp__visibility_control.hpp")
    write_file(visibility_file_path, template_visibility_control_hpp.render(package_name, package_name.upper()))

    generate_files.append(visibility_file_path)

    return generate_files


def generate_c(idl_files, output_dir, package_name, type_description_map):
    mapping = {
        'idl.h.em': '%s.h',
        'idl__description.c.em': 'detail/%s__description.c',
        'idl__functions.c.em': 'detail/%s__functions.c',
        'idl__functions.h.em': 'detail/%s__functions.h',
        'idl__struct.h.em': 'detail/%s__struct.h',
        'idl__type_support.c.em': 'detail/%s__type_support.c',
        'idl__type_support.h.em': 'detail/%s__type_support.h',
    }

    generate_files = generate_files_noose(idl_files, mapping, "rosidl_generator_c", package_name, output_dir,
                                          type_description_map,
                                          additional_context={
                                              'disable_description_codegen': False
                                          })

    from rosidl.resource.rosidl_generator_c import template_visibility_control_h
    visibility_file_path = os.path.join(output_dir, "msg", "rosidl_generator_c__visibility_control.h")
    write_file(visibility_file_path, template_visibility_control_h.render(package_name, package_name.upper()))

    generate_files.append(visibility_file_path)

    return generate_files


def collect_include_path_tuples(include_paths):
    include_path_tuples = {}
    for include_path in include_paths:
        for root, _, files in os.walk(include_path):
            for file in files:
                if file.endswith(".json"):
                    file_path = pathlib.Path(root) / file
                    package_name = file_path.parent.parts[-2]
                    if package_name not in include_path_tuples:
                        include_path_tuples[package_name] = file_path.parent.parent

    return include_path_tuples


def generate_type_description(idl_files, output_dir, package_name, include_paths_tuples):
    return generate_type_hash_noose(package_name, os.path.join(output_dir, package_name), idl_files,
                                    include_paths_tuples)


def map_idl_paths_to_type_description_paths(idl_file_paths, type_description_paths):
    mapped_idl_paths = {}
    for idl_file_path in idl_file_paths:
        for type_description_path in type_description_paths:
            idl_pathlib_path = pathlib.Path(idl_file_path)
            idl_message_type = idl_pathlib_path.parent.parts[-1]
            type_description_message_type = type_description_path.parent.parts[-1]
            if idl_pathlib_path.stem == type_description_path.stem and idl_message_type == type_description_message_type:
                idl_type = idl_pathlib_path.parent.parts[-1]
                idl_name = idl_pathlib_path.name
                relative_idl_path = os.path.join(idl_type, idl_name)
                mapped_idl_paths[relative_idl_path] = str(type_description_path)

    return mapped_idl_paths


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Noose IDL Generator')
    parser.add_argument('--package-name', required=True, help='The name of the package name')
    parser.add_argument('--input', required=True,
                        help='Noose IDL input file.')
    parser.add_argument('--cpp-output-dir', help='generated C++ code output directory.', default='generated')
    parser.add_argument('--idl-output-dir', help='idl output directory.', default='idl')
    parser.add_argument('--include-dir', nargs='+', default=[],
                        help='Absolute include paths containing type description jsons. The folder is expected to contain a structure like: <package_name>/[msg/service/action]/<type_name>.json')

    args = parser.parse_args(argv)

    input_file = args.input
    package_name = args.package_name
    cpp_output_dir = args.cpp_output_dir
    idl_output_dir = args.idl_output_dir
    include_dirs = args.include_dir

    input_path = pathlib.Path(input_file)
    input_dir = input_path.parent

    idl_files = []

    if input_file.endswith(".msg") or input_file.endswith(".action") or input_file.endswith(".srv"):
        idl_files.append(convert_to_idl(input_dir, package_name, input_path.relative_to(input_dir),
                       pathlib.Path(idl_output_dir)))
    elif input_file.endswith(".idl"):
        idl_files.append(input_file)
    else:
        print("Wrong file extension")
        exit(1)

    type_description_paths = generate_type_description(idl_files, idl_output_dir, package_name,
                                                       collect_include_path_tuples(include_dirs))
    type_description_map = map_idl_paths_to_type_description_paths(idl_files, type_description_paths)

    generated_sources = []

    generated_sources += generate_c(idl_files, cpp_output_dir, package_name, type_description_map)
    generated_sources += generate_cpp(idl_files, cpp_output_dir, package_name)
    generated_sources += generate_cpp_typesupport_introspection(idl_files, cpp_output_dir, package_name)
    generated_sources += generate_cpp_typesupport_fastrtps(idl_files, cpp_output_dir, package_name)

    source_files = []
    for source_file in generated_sources:
        if source_file.endswith('.cpp') or source_file.endswith('.c'):
            source_file_path = pathlib.Path(source_file)
            cpp_root_path = pathlib.Path(cpp_output_dir)
            source_files.append(str(source_file_path.relative_to(cpp_root_path)))

if __name__ == '__main__':
    main()
