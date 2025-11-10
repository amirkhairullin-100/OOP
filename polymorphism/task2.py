class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
    def add_word(self, word):
        self.words.append(word)
    def end(self):
        lines = []
        current = []
        for word in self.words:
            if current and len(' '.join(current + [word])) > self.width:
                lines.append(' '.join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(' '.join(current))
        for line in lines:
            print(line)
        self.words = []
class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
    def add_word(self, word):
        self.words.append(word)
    def end(self):
        lines = []
        current = []
        for word in self.words:
            if current and len(' '.join(current + [word])) > self.width:
                lines.append(' '.join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(' '.join(current))
        for line in lines:
            spaces = self.width - len(line)
            print(' ' * spaces + line)
        self.words = []
lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()
rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
