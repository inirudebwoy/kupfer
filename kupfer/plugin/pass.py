"""Plugin for password store

https://www.passwordstore.org/

"""
__kupfer_name__ = _('Pass')
__kupfer_sources__ = ('PassSource', )
__kupfer_actions__ = ('CopyPassword', )
__description__ = _('Access to password store')
__version__ = '0.0.1'
__author__ = ('Michal Klich <michal@michalklich.com>')

import os
from subprocess import check_call

from kupfer.objects import Action, TextLeaf, Source

PSROOT_PATH = os.path.expanduser('~/.password-store/')


class PassSource(Source):
    def __init__(self, name=_('Passwords list')):
        super(PassSource, self).__init__(name)

    def get_items(self):
        for root, _dirn, filn in os.walk(PSROOT_PATH):
            for f in filn:
                name, ext = os.path.splitext(f)
                if ext == '.gpg':
                    abs_path = os.path.join(root, name)
                    yield TextLeaf(os.path.relpath(abs_path, PSROOT_PATH))

    def provides(self):
        yield TextLeaf


class CopyPassword(Action):
    def get_description(self):
        return _('Copy password to the clipboard')

    def item_types(self):
        yield TextLeaf

    def activate(self, obj):
        check_call(['pass', 'show', '-c', obj.name])

    def get_icon_name(self):
        return 'edit-copy'
