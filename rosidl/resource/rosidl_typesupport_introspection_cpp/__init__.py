from . import template_idl_hpp
from . import template_idl_type_support_cpp
from . import template_msg_hpp
from . import template_msg_type_support_cpp
from . import template_srv_hpp
from . import template_srv_type_support_cpp


def get_template(template_name):
    if template_name == "idl__rosidl_typesupport_introspection_cpp.hpp.em":
        return template_idl_hpp.get_template()
    if template_name == "idl__type_support.cpp.em":
        return template_idl_type_support_cpp.get_template()
    if template_name == "msg__rosidl_typesupport_introspection_cpp.hpp.em":
        return template_msg_hpp.get_template()
    if template_name == "msg__type_support.cpp.em":
        return template_msg_type_support_cpp.get_template()
    if template_name == "srv__rosidl_typesupport_introspection_cpp.hpp.em":
        return template_srv_hpp.get_template()
    if template_name == "srv__type_support.cpp.em":
        return template_srv_type_support_cpp.get_template()

    raise ValueError("Unknown template '%s'" % template_name)