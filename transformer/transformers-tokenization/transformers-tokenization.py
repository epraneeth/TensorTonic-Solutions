class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}
        self.vocab_size = 0
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"

    def build_vocab(self, texts: list[str]) -> None:
        """
        Builds the vocabulary in place.
        """
        seperated = sorted(set(x for y in texts for x in  y.lower().split()))
        self.word_to_id={"<PAD>":0,"<UNK>":1,"<BOS>":2,"<EOS>":3}
        self.word_to_id.update({word:index+4 for index,word in enumerate(seperated)})
        self.id_to_word={v:k for k,v in self.word_to_id.items()}
        self.vocab_size = len(self.word_to_id)

       
        
        pass

    def encode(self, text: str) -> list[int]:
        """
        Returns token IDs for the input text.
        """
        textList = text.lower().split()
        unk_id=self.word_to_id.get(self.unk_token,1)
        encoded = [self.word_to_id.get(x,unk_id)  for x in textList]
        return encoded

    def decode(self, ids: list[int]) -> str:
        """
        Returns the decoded, space-separated text.
        """
        sentence=[self.id_to_word.get(x,"<UNK>") for x in ids]
        
        return " ".join(sentence)