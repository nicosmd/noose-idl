from . import template_action_type_support_c
from . import template_action_type_support_h
from . import template_empty_description_c
from . import template_full_description_c
from . import template_idl_h
from . import template_idl_description_c
from . import template_idl_functions_c
from . import template_idl_functions_h
from . import template_idl_struct_h
from . import template_idl_type_support_c
from . import template_idl_type_support_h
from . import template_msg_functions_c
from . import template_msg_functions_h
from . import template_msg_struct_h
from . import template_msg_type_support_h
from . import template_srv_type_support_c
from . import template_srv_type_support_h


def get_template(template_name):
    if template_name == "action__type_support.c.em":
        return template_action_type_support_c.get_template()
    if template_name == "action__type_support.h.em":
        return template_action_type_support_h.get_template()
    if template_name == "empty__description.c.em":
        return template_empty_description_c.get_template()
    if template_name == "full__description.c.em":
        return template_full_description_c.get_template()
    if template_name == "idl.h.em":
        return template_idl_h.get_template()
    if template_name == "idl__description.c.em":
        return template_idl_description_c.get_template()
    if template_name == "idl__functions.c.em":
        return template_idl_functions_c.get_template()
    if template_name == "idl__functions.h.em":
        return template_idl_functions_h.get_template()
    if template_name == "idl__struct.h.em":
        return template_idl_struct_h.get_template()
    if template_name == "idl__type_support.c.em":
        return template_idl_type_support_c.get_template()
    if template_name == "idl__type_support.h.em":
        return template_idl_type_support_h.get_template()
    if template_name == "msg__functions.c.em":
        return template_msg_functions_c.get_template()
    if template_name == "msg__functions.h.em":
        return template_msg_functions_h.get_template()
    if template_name == "msg__struct.h.em":
        return template_msg_struct_h.get_template()
    if template_name == "msg__type_support.h.em":
        return template_msg_type_support_h.get_template()
    if template_name == "srv__type_support.c.em":
        return template_srv_type_support_c.get_template()
    if template_name == "srv__type_support.h.em":
        return template_srv_type_support_h.get_template()

    raise ValueError("Unknown template '%s'" % template_name)
