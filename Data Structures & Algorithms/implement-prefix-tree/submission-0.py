class PrefixTree:

    def __init__(self):
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        for w in self.words:
            if word == w:
                return True
        #not found    
        return False

    def startsWith(self, prefix: str) -> bool:
        sliceSize = len(prefix)
        for w in self.words:
            if len(w) >= sliceSize and prefix == w[:sliceSize]:
                return True
        return False

        