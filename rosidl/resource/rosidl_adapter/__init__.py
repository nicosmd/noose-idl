from . import template_msg_idl, template_struct_idl

# Map old ros template names to noose-idl template modules
def get_template(template_name):
    if template_name == "msg.idl.em":
        return template_msg_idl.get_template()
    if template_name == "struct.idl.em":
        return template_struct_idl.get_template()
