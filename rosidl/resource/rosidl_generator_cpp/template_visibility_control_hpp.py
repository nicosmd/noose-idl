_template = """
// generated from rosidl_generator_cpp/resource/rosidl_generator_cpp__visibility_control.hpp.in
// generated code does not contain a copyright notice

#ifndef {project_name_upper}__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_
#define {project_name_upper}__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_

#ifdef __cplusplus
extern "C"
{{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define ROSIDL_GENERATOR_CPP_EXPORT_{project_name} __attribute__ ((dllexport))
    #define ROSIDL_GENERATOR_CPP_IMPORT_{project_name} __attribute__ ((dllimport))
  #else
    #define ROSIDL_GENERATOR_CPP_EXPORT_{project_name} __declspec(dllexport)
    #define ROSIDL_GENERATOR_CPP_IMPORT_{project_name} __declspec(dllimport)
  #endif
  #ifdef ROSIDL_GENERATOR_CPP_BUILDING_DLL_{project_name}
    #define ROSIDL_GENERATOR_CPP_PUBLIC_{project_name} ROSIDL_GENERATOR_CPP_EXPORT_@PROJECT_NAME@
  #else
    #define ROSIDL_GENERATOR_CPP_PUBLIC_{project_name} ROSIDL_GENERATOR_CPP_IMPORT_{project_name}
  #endif
#else
  #define ROSIDL_GENERATOR_CPP_EXPORT_{project_name} __attribute__ ((visibility("default")))
  #define ROSIDL_GENERATOR_CPP_IMPORT_{project_name}
  #if __GNUC__ >= 4
    #define ROSIDL_GENERATOR_CPP_PUBLIC_{project_name} __attribute__ ((visibility("default")))
  #else
    #define ROSIDL_GENERATOR_CPP_PUBLIC_{project_name}
  #endif
#endif

#ifdef __cplusplus
}}
#endif

#endif  // {project_name_upper}__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_
"""


def render(project_name_upper, project_name):
    return _template.format(project_name_upper=project_name_upper, project_name=project_name)
