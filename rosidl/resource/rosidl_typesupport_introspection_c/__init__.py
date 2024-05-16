from . import template_idl_typesupport_h
from . import template_idl_typesupport_c
from . import template_msg_typesupprt_introspection_h
from . import template_msg_typesupprt_c
from . import template_srv_typesupport_introspection_h
from . import template_srv_type_support_c


def get_template(template_name):
    if template_name == "idl__rosidl_typesupport_introspection_c.h.em":
        return template_idl_typesupport_h.get_template()
    if template_name == "idl__type_support.c.em":
        return template_idl_typesupport_c.get_template()
    if template_name == "msg__rosidl_typesupport_introspection_c.h.em":
        return template_msg_typesupprt_introspection_h.get_template()
    if template_name == "msg__type_support.c.em":
        return template_msg_typesupprt_c.get_template()
    if template_name == "srv__rosidl_typesupport_introspection_c.h.em":
        return template_srv_typesupport_introspection_h.get_template()
    if template_name == "srv__type_support.c.em":
        return template_srv_type_support_c.get_template()

    raise ValueError("Unknown template '%s'" % template_name)
