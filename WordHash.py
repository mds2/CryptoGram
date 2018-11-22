from WordUtil import *

class WordHash:
    letters = "abcdefghijklmnopqrstuvwxyz"
    hash_2_word_map = None
    hash_2_common = None
    common_words = None
    def __init__(self, in_str):
        self.str_val = WordUtil.strip(in_str)
        self.hash_val = None
    def hash_word(in_str):
        return WordHash.hash_word_(WordUtil.strip(in_str))
    def hash_word_(in_str):
        i = 0
        m = {}
        arr = [] # result as array to be converted to string
        for l in in_str:
            if l in m:
                arr.append(m[l])
            else:
                m[l] = WordHash.letters[i]
                arr.append(m[l])
                i += 1
        return "".join(arr)
    def val(self):
        if not self.hash_val:
            self.hash_val = hash_word_(self.str_val)
        return self.hash_val
    def set_str(self, in_str):
        self.str_val = WordUtil.strip(in_str)
        self.hash_val = None
    def hash_matches(in_str, thorough):
        if not (WordHash.hash_2_common and WordHash.common_words):
            WordHash.common_words = set([])
            WordHash.hash_2_common = {}
            from nltk.corpus import brown
            for word in brown.words():
                w = WordUtil.strip(word)
                if w in WordHash.common_words:
                    continue
                k = WordHash.hash_word(w)
                l = WordHash.hash_2_common.get(k, []) + [w]
                WordHash.hash_2_common[k] = l
                WordHash.common_words.add(w)
        if thorough and not WordHash.hash_2_word_map:
            h = {}
            import nltk
            from nltk.corpus import words
            for word in words.words():
                w = WordUtil.strip(word)
                if w in WordHash.common_words:
                    continue
                k = WordHash.hash_word(w)
                h[k] = h.get(k, []) + [w]
            WordHash.hash_2_word_map = h
        if thorough:
            return WordHash.hash_2_word_map.get(WordHash.hash_word(in_str), [])
        return WordHash.hash_2_common.get(WordHash.hash_word(in_str), [])
    
    
    
