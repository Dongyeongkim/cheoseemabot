import csv
import numpy as np
from scipy import stats
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from textrank import TextRank, RawSentenceReader, RawTaggerReader


class cheoseema(object):
    def __init__(self, sentence_list):
        tsv_file = open("word_vector.tsv", 'r')
        self.어조dict = {"EF": 'nan', "EFA": 0, "EFI": 1, "EFN": 2, "EFO": 3, "EFQ": 4, "EFR": 5}
        self.compressed_dict = {0: "불명", 1: "감탄", 2: "담담", 3: "명령", 4: "의문", 5: "존칭"}
        self.word_vector_list = csv.reader(tsv_file, delimiter="\t")
        self.sentence_list = sentence_list

    # 처지
    def 처지(self):
        tr = TextRank()
        from konlpy.tag import Komoran
        tagger = Komoran()
        stopword = set([('있', 'VV'), ('하', 'VV'), ('되', 'VV')])
        tr.loadSents(RawSentenceReader('x.txt'),
                     lambda sent: filter(lambda x: x not in stopword and x[1] in ('NNG', 'NNP', 'VV', 'VA'),
                                         tagger.pos(sent)))
        tr.build()
        ranks = tr.rank()
        if tr.summarize(0.4) is None:
            return "모름"
        else:
            return tr.summarize(0.4)

    # 심정
    def 심정(self):
        tr = TextRank(window=5, coef=1)
        stopword = set([('있', 'VV'), ('하', 'VV'), ('되', 'VV'), ('없', 'VV')])
        tr.load(RawTaggerReader('x.txt'), lambda w: w not in stopword and (w[1] in ('NNG', 'NNP', 'VV', 'VA')))
        tr.build()
        kw = tr.extract(0.4)
        if kw is None:
            return "모름"
        else:
            return kw

    # 어조
    def 어조(self):
        fqwr = []
        kkma = Kkma()
        for sentence in self.sentence_list:
            for n in kkma.pos(sentence):
                try:
                    fqwr.append(self.어조dict[n[1]])
                except KeyError:
                    pass
        fqwr = np.array(fqwr)
        m = stats.mode(fqwr)
        if m[0].size == 0:
            return None
        else:
            return self.compressed_dict[m[0][0]]

    # 입장
    def 입장(self):
        pass

    # 소망

    def 소망(self):
        pass

    # 표현
    def 표현(self):
        print("We didn't support yet")
