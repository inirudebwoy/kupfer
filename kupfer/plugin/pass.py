__kupfer_name__ = _('Pass')
__kupfer_sources__ = ('PassSource', )
__kupfer_actions__ = ('GetPassword', )
__description__ = _('Access to pass')
__version__ = '0.0.1'
__author__ = ('Michal Klich <michal@michalklich.com>', )

from kupfer.objects import Action, TextLeaf, TextSource


class PassSource(TextSource):
    pass


class GetPassword(Action):
    pass


class PassLeaf(TextLeaf):
    pass
