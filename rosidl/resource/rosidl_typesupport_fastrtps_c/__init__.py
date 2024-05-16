from . import template_idl_typesupport_h
from . import template_idl_typesupport_cpp
from . import template_msg_typesupport_h
from . import template_msg_typesupport_cpp
from . import template_srv_typesupport_h
from . import template_srv_typesupport_cpp


def get_template(template_name):
    if template_name == 'idl__rosidl_typesupport_fastrtps_c.h.em':
        return template_idl_typesupport_h.get_template()
    if template_name == 'idl__type_support_c.cpp.em':
        return template_idl_typesupport_cpp.get_template()
    if template_name == 'msg__rosidl_typesupport_fastrtps_c.h.em':
        return template_msg_typesupport_h.get_template()
    if template_name == 'msg__type_support_c.cpp.em':
        return template_msg_typesupport_cpp.get_template()
    if template_name == 'srv__rosidl_typesupport_fastrtps_c.h.em':
        return template_srv_typesupport_h.get_template()
    if template_name == 'srv__type_support_c.cpp.em':
        return template_srv_typesupport_cpp.get_template()

    raise ValueError("Unknown template '%s'" % template_name)
