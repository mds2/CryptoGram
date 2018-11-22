
class WordUtil:
    letters = "abcdefghijklmnopqrstuvwxyz"
    def strip(in_str):
        return "".join([l for l in in_str.lower() if l in WordUtil.letters])
    class CipherConstructionException(Exception):
        def __init(self, msg):
            Exception.__init__(self, msg)
        def __init__(self, w1, w2):
            Exception.__init__(self, w1 + " -does not match- " + w2)
    class Cipher:
        def __init__(self, w1, w2):
            self.m = {}
            self.r_m = {}
            self.m[" "] = " "
            self.r_m[" "] = " "
            if len(w1) != len(w2):
                raise CipherConstructionException(w1, w2)
            for i in range(len(w1)):
                if self.m.get(w1[i], w2[i]) != w2[i]:
                    raise CipherConstructionException(w1, w2)
                self.m[w1[i]] = w2[i]
                if self.r_m.get(w2[i], w1[i]) != w1[i]:
                    raise CipherConstructionException(w1, w2)
                self.r_m[w2[i]] = w1[i]
        def copy(self):
            o = WordUtil.Cipher("", "")
            o.m = self.m.copy()
            o.r_m = self.r_m.copy()
            return o
        def copy_and_extend(self, w1, w2):
            o = self.copy()
            if len(w1) != len(w2):
                return None
            for i in range(len(w1)):
                if o.m.get(w1[i], w2[i]) != w2[i]:
                    return None
                o.m[w1[i]] = w2[i]
                if o.r_m.get(w2[i], w1[i]) != w1[i]:
                    return None
                o.r_m[w2[i]] = w1[i]
            return o
        def apply(self, msg):
            if type(msg) == type("hi"):
                return "".join([self.m.get(l,".") for l in msg])
            return " ".join([self.apply(w) for w in msg])
