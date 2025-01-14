from Preln.preprocessing import Preprocessing

def test_preprocessing():
    pipeline = Preprocessing(punctuation=False, stopwords=False)
    assert pipeline.pipeline('I LoVe NLp') == 'i love nlp'
    
    pipeline = Preprocessing(stopwords=False)
    assert pipeline.pipeline('I LoVe NLp{}[]?¿¡!;,:._-^*·#') == 'i love nlp'
    
    pipeline = Preprocessing()
    assert pipeline.pipeline('I b LoVe a hola NLp{}[]?¿¡!;,:._-^*·#') == 'love nlp'
    