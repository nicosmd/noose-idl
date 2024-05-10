_template = """
// generated from rosidl_generator_c/resource/rosidl_generator_c__visibility_control.h.in
// generated code does not contain a copyright notice

#ifndef {project_name_upper}__MSG__ROSIDL_GENERATOR_C__VISIBILITY_CONTROL_H_
#define {project_name_upper}__MSG__ROSIDL_GENERATOR_C__VISIBILITY_CONTROL_H_

#ifdef __cplusplus
extern "C"
{{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define ROSIDL_GENERATOR_C_EXPORT_{project_name} __attribute__ ((dllexport))
    #define ROSIDL_GENERATOR_C_IMPORT_{project_name} __attribute__ ((dllimport))
  #else
    #define ROSIDL_GENERATOR_C_EXPORT_{project_name} __declspec(dllexport)
    #define ROSIDL_GENERATOR_C_IMPORT_{project_name} __declspec(dllimport)
  #endif
  #ifdef ROSIDL_GENERATOR_C_BUILDING_DLL_@PROJECT_NAME@
    #define ROSIDL_GENERATOR_C_PUBLIC_{project_name} ROSIDL_GENERATOR_C_EXPORT_@PROJECT_NAME@
  #else
    #define ROSIDL_GENERATOR_C_PUBLIC_{project_name} ROSIDL_GENERATOR_C_IMPORT_@PROJECT_NAME@
  #endif
#else
  #define ROSIDL_GENERATOR_C_EXPORT_{project_name} __attribute__ ((visibility("default")))
  #define ROSIDL_GENERATOR_C_IMPORT_{project_name}
  #if __GNUC__ >= 4
    #define ROSIDL_GENERATOR_C_PUBLIC_{project_name} __attribute__ ((visibility("default")))
  #else
    #define ROSIDL_GENERATOR_C_PUBLIC_{project_name}
  #endif
#endif

#ifdef __cplusplus
}}
#endif

#endif  // {project_name_upper}__MSG__ROSIDL_GENERATOR_C__VISIBILITY_CONTROL_H_
"""


def render(project_name_upper, project_name):
    return _template.format(project_name_upper=project_name_upper, project_name=project_name)
