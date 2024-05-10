from . import template_action_builder_hpp
from . import template_action_struct_hpp
from . import template_action_traits_hpp
from . import template_action_type_support_hpp
from . import template_idl_hpp
from . import template_idl_builder_hpp
from . import template_idl_struct_hpp
from . import template_idl_traits_hpp
from . import template_idl_type_support
from . import template_msg_builder_hpp
from . import template_msg_struct_hpp
from . import template_msg_traits_hpp
from . import template_msg_type_support_hpp
from . import template_srv_builder_hpp
from . import template_srv_struct_hpp
from . import template_srv_traits_hpp
from . import template_srv_type_support_hpp


# Map old ros template names to noose-idl template modules
def get_template(template_name):
    if template_name == "action__builder.hpp.em":
        return template_action_builder_hpp.get_template()
    if template_name == "action__struct.hpp.em":
        return template_action_struct_hpp.get_template()
    if template_name == "action__traits.hpp.em":
        return template_action_traits_hpp.get_template()
    if template_name == "action__type_support.hpp.em":
        return template_action_type_support_hpp.get_template()
    if template_name == "idl.hpp.em":
        return template_idl_hpp.get_template()
    if template_name == "idl__builder.hpp.em":
        return template_idl_builder_hpp.get_template()
    if template_name == "idl__struct.hpp.em":
        return template_idl_struct_hpp.get_template()
    if template_name == "idl__traits.hpp.em":
        return template_idl_traits_hpp.get_template()
    if template_name == "idl__type_support.hpp.em":
        return template_idl_type_support.get_template()
    if template_name == "msg__builder.hpp.em":
        return template_msg_builder_hpp.get_template()
    if template_name == "msg__struct.hpp.em":
        return template_msg_struct_hpp.get_template()
    if template_name == "msg__traits.hpp.em":
        return template_msg_traits_hpp.get_template()
    if template_name == "msg__type_support.hpp.em":
        return template_msg_type_support_hpp.get_template()
    if template_name == "srv__builder.hpp.em":
        return template_srv_builder_hpp.get_template()
    if template_name == "srv__struct.hpp.em":
        return template_srv_struct_hpp.get_template()
    if template_name == "srv__traits.hpp.em":
        return template_srv_traits_hpp.get_template()
    if template_name == "srv__type_support.hpp.em":
        return template_srv_type_support_hpp.get_template()

    raise ValueError("Unknown template '%s'" % template_name)
