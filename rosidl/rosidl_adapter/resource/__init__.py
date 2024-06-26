# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from io import StringIO
import os
import sys

import em

from rosidl.resource import rosidl_adapter as resources


def expand_template(template_name, data, output_file, encoding='utf-8'):
    content = evaluate_template(template_name, data)

    if output_file.exists():
        existing_content = output_file.read_text(encoding=encoding)
        if existing_content == content:
            return
    elif output_file.parent:
        os.makedirs(str(output_file.parent), exist_ok=True)

    output_file.write_text(content, encoding=encoding)


_interpreter = None


def evaluate_template(template_name, data):
    global _interpreter
    # create copy before manipulating
    data = dict(data)
    data['TEMPLATE'] = _evaluate_template

    output = StringIO()
    try:
        _interpreter = em.Interpreter(
            output=output,
            options={
                em.BUFFERED_OPT: True,
                em.RAW_OPT: True,
            })

        content = resources.get_template(template_name)
        _interpreter.string(content, locals=data)

        return output.getvalue()
    except Exception as e:  # noqa: F841
        print(
            f"{e.__class__.__name__} processing template '{template_name}'",
            file=sys.stderr)
        raise
    finally:
        _interpreter.shutdown()
        _interpreter = None


def _evaluate_template(template_name, **kwargs):
    global _interpreter
    content = resources.get_template(template_name)
    try:
        _interpreter.string(content, locals=kwargs)
    except Exception as e:  # noqa: F841
        print(
            f"{e.__class__.__name__} processing template '{template_name}': "
            f'{e}', file=sys.stderr)
        sys.exit(1)
