import keyword_extract_rules as ker
import logique_stanza as lg
import stanza_parseTree as sp
import stanza
nlp = stanza.Pipeline("en")

def is_rule(method,sentence):
    '''
    method: 'keyword' or 'bert'
    sentence: a string
    '''
    if method == 'keyword':
        return ker.is_rule(sentence)
    elif method == 'bert':
        import classification_bertas as bert
        return bert.is_causal([sentence])[0]        
    else:
        raise Exception('Incorrect method')

def extract_rules(method,text):
    L = []
    phrases = [s for s,_,_,_ in ker.sentencify(text)]
    for phrase in phrases:
        if is_rule(method,phrase):
            L.append(phrase)
    return L

def cause_consequence(method,sentence):
    '''
    method: 'logic' or 'syntaxic'
    sentence: a string
    '''
    if method=='logic':
        return lg.cause_consequences(sentence)
    else:
        return sp.list_cause_consequence(sentence)