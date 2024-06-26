_template = r"""
@# Included from rosidl_generator_cpp/resource/idl__builder.hpp.em
@{
TEMPLATE(
    'msg__builder.hpp.em',
    package_name=package_name, interface_path=interface_path,
    message=service.request_message, include_directives=include_directives)
}@

@{
TEMPLATE(
    'msg__builder.hpp.em',
    package_name=package_name, interface_path=interface_path,
    message=service.response_message, include_directives=include_directives)
}@

@{
TEMPLATE(
    'msg__builder.hpp.em',
    package_name=package_name, interface_path=interface_path,
    message=service.event_message, include_directives=include_directives)
}@
"""

def get_template():
    return _template