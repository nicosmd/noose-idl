from jinja2 import Template

_template = """
project({{ package_name }})

add_library({{ package_name }})

target_include_directories({{ package_name }} PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_sources({{ package_name }} PRIVATE
    {% for source_file in source_files %}
        {{ source_file }}
    {% endfor %}
)
"""


def render_template(package_name, source_files):
    return Template(_template).render(package_name=package_name, source_files=source_files)
