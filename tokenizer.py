class CharacterTokenizer:
    def __init__(self, text: str):
        """
        A simple character-level tokenizer.
        :param text: The text corpus used to build the vocabulary.
        """
        self.chars = sorted(list(set(text)))
        self.vocab_size = len(self.chars)
        self.stoi = {ch: i for i, ch in enumerate(self.chars)}
        self.itos = {i: ch for i, ch in enumerate(self.chars)}

    def encode(self, s: str) -> list[int]:
        """
        Converts a string of text into a list of token IDs.
        """
        return [self.stoi[c] for c in s if c in self.stoi]

    def decode(self, l: list[int]) -> str:
        """
        Converts a list of token IDs back into a string of text.
        """
        return ''.join([self.itos[i] for i in l])
