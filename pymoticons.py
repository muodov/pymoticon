class BaseEmo(object):
    def __repr__(self):
        return 'hmm...'

class Damn(BaseEmo):
    def __repr__(self):
        return 'doh!'

class Cool(BaseEmo):
    def __repr__(self):
        return 'Awesome!'

class Indeed(BaseEmo):
    def __repr__(self):
        return 'You are so right!'

class Lol(BaseEmo):
    def __repr__(self):
        return 'lol!'

class Ah(BaseEmo):
    def __repr__(self):
        return 'ah, now I see'

class Omg(BaseEmo):
    def __repr__(self):
        return 'Oh my Gosh, this is so'

class Kenny(BaseEmo):
    def __repr__(self):
        return 'Oh my god, they killed Kenny! You, bastards!'

class Wtf(BaseEmo):
    def __repr__(self):
        return 'what is this supposed to mean?!'

class Oops(BaseEmo):
    def __repr__(self):
        return "oops, that wasn't me"


damn = Damn()
cool = Cool()
indeed = Indeed()
lol = Lol()
ah = Ah()
omg = Omg()
kenny = Kenny()
wtf = Wtf()
oops = Oops()
