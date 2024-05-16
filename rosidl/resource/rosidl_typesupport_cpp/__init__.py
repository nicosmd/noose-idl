from . import template_action_typesupport_cpp
from . import template_idl_typesupport_cpp
from . import template_msg_typesupport_cpp
from . import template_srv_typesupport_cpp


def get_template(template_name):
    if template_name == "action__type_support.cpp.em":
        return template_action_typesupport_cpp.get_template()
    if template_name == "idl__type_support.cpp.em":
        return template_idl_typesupport_cpp.get_template()
    if template_name == "msg__type_support.cpp.em":
        return template_msg_typesupport_cpp.get_template()
    if template_name == "srv__type_support.cpp.em":
        return template_srv_typesupport_cpp.get_template()

    raise ValueError("Unknown template '%s'" % template_name)
