#!/usr/bin/python
# issue #555: I'm a module that cutpastes an old hack.

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import get_module_path
from ansible.module_utils import six

import os
import pwd
import socket
import sys

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def main():
    module = AnsibleModule(argument_spec={})
    module.exit_json(ok=True)

if __name__ == '__main__':
    main()