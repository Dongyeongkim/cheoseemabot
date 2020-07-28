import numpy as np
from scipy import stats
from konlpy.tag import Kkma
from konlpy.utils import pprint
from collections import Counter

kkma = Kkma()
f = open('x.txt','w')
f.write(input("시 적으세요"))
f.close()
f = open('x.txt','r')
sentences = f.read()
sentence_list = kkma.sentences(sentences)

어조dict = {"EF": 'nan',
          "EFA": 0,       
          "EFI": 1,
          "EFN": 2,
          "EFO": 3,
          "EFQ": 4,
          "EFR": 5}
Compressed_dict = {0:"불명",1:"감탄",2:"담담",3:"명령",4:"의문",5:"존칭"}

# EFA: 청유
# EFI: 감탄
# EFN: 평서
# EFO: 명령
# EFQ: 의문
# EFR: 존칭 



class cheoseema:
    def __init__(self,sentence_list,어조dict,Compressed_dict):
        self.어조dict = 어조dict
        
        self.sentence_list = sentence_list
        print(self.처지(), self.심정(),self.어조(Compressed_dict), self.입장(), self.소망(), self.표현())
        
    #처지
    def 처지(self):
        pass

    #심정
    def 심정(self):
        pass
        
    #어조
    def 어조(self,Compressed_dict):
        fqwr = []
        for sentence in self.sentence_list:
            print(sentence)
            for n in kkma.pos(sentence):
                try:
                    fqwr.append(self.어조dict[n[1]])
                except KeyError:
                    pass
        fqwr = np.array(fqwr)
        m = stats.mode(fqwr)
        print(m[0])
        if m[0].size == 0:
            print("알 수 없음")
        else:
            print(Compressed_dict[m[0][0]])


    #입장
    def 입장(self):
        pass

    #소망
    
    def 소망(self):
        pass
    
    #표현
    def 표현(self):
        pass

cheoseem = cheoseema(sentence_list,어조dict,Compressed_dict)

print(cheoseem)
    


















