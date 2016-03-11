__kupfer_name__ = _('Pass')
__kupfer_sources__ = ('PassSource', )
__kupfer_actions__ = ('GetPassword', )
__description__ = _('Access to pass')
__version__ = '0.0.1'
__author__ = ('Michal Klich <michal@michalklich.com>')

import os
from subprocess import check_output

from kupfer.objects import Action, TextLeaf, Source


class PassSource(Source):
    def __init__(self, name=_('Passwords list')):
        super(PassSource, self).__init__(name)

    def get_items(self):
        # return only gpg files, with no extension
        # TODO: location of storage should be taken from env
        # TODO: this needs to return exact ID of the password, with the directory
        for root, _dirn, filn in os.walk('/home/majki/.password-store/'):
            for f in filn:
                name, _ = os.path.splitext(f)
                yield PassLeaf(os.path.join(root, name), name)

    def provides(self):
        yield PassLeaf


class GetPassword(Action):
    def item_types(self):
        yield PassLeaf

    def activate(self, obj):
        call = check_output(['pass', 'show', obj.name])
        print(call)


class PassLeaf(TextLeaf):
    def get_actions(self):
        return [GetPassword()]

    def repr_key(self):
        return self.object
