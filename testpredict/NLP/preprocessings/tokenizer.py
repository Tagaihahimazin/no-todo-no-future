# -*- coding: utf-8 -*-
from collections import namedtuple


from janome.tokenizer import Tokenizer


class JanomeTokenizer(object):

    def __init__(self, user_dic_path='', user_dic_enc='utf8'):
        self._t = Tokenizer(udic=user_dic_path, udic_enc=user_dic_enc)

    def surface(self, token):
        return token.surface

    def baseform_or_surface(self, token):
        return token.base_form if token.base_form != '*' else token.surface

    def exist_pos(self, token, pos=('名詞')):
        if (token.pos in pos): return True
        return False

    def tokenize(self, sent):
        token = namedtuple('Token', 'surface, pos, pos_detail1, pos_detail2, pos_detail3,\
                                             infl_type, infl_form, base_form, reading, phonetic')
        tokens = []
        for t in self._t.tokenize(sent):
            poses = t.part_of_speech.split(',')
            tokens.append(token(t.surface, poses[0], poses[1], poses[2], poses[3],
                        t.infl_type, t.infl_form, t.base_form, t.reading, t.phonetic))
        return tokens
