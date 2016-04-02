"""Plugin for password store

https://www.passwordstore.org/

"""
__kupfer_name__ = _('Pass')
__kupfer_sources__ = ('PassSource', )
__kupfer_actions__ = ('CopyPassword', )
__description__ = _('Integration with pass. (https://passwordstore.org)')
__version__ = '0.0.1'
__author__ = ('Michal Klich <michal@michalklich.com>')

import os
from subprocess import Popen, PIPE

from kupfer import plugin_support
from kupfer.objects import Action, TextLeaf, Source
from kupfer.pretty import debug, print_debug

__kupfer_settings__ = plugin_support.PluginSettings({
    'key': 'storage_location',
    'label': _('Password store location'),
    'type': str,
    'value': '~/.password-store/'
})


class PassSource(Source):
    def __init__(self, name=_('Passwords list')):
        super(PassSource, self).__init__(name)

    def get_items(self):
        pass_store_dir = os.path.expanduser(
            __kupfer_settings__['storage_location'])
        for root, _dirn, filn in os.walk(pass_store_dir):
            for f in filn:
                name, ext = os.path.splitext(f)
                if ext == '.gpg':
                    abs_path = os.path.join(root, name)
                    yield TextLeaf(os.path.relpath(abs_path, pass_store_dir))

    def provides(self):
        yield TextLeaf


class CopyPassword(Action):
    def get_description(self):
        return _('Copy password to the clipboard')

    def item_types(self):
        yield TextLeaf

    def activate(self, obj):
        try:
            Popen(['pass', 'show', '-c', obj.name], stdout=PIPE)
        except OSError as e:
            if debug:
                print_debug(e)
            pass

    def get_icon_name(self):
        return 'edit-copy'
