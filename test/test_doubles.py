class NerTestDouble:
    """
    Test double for SpaCy NLP NER model
    """

    def __init__(self, model) -> None:
        self.mode = model

    def returns_doc_ents(self, ents):
        self.ents = ents

    def __call__(self, sq):
        return DocTestDouble(sq, self.ents)


class DocTestDouble:
    """
    test double for SpaCy DOc
    """

    def __init__(self, sent, ents) -> None:
        self.ents = [SpanTestDouble(ent["text"], ent["label_"]) for ent in ents]

    def patch_method(self, attr, return_value):
        def patched():
            return return_value

        setattr(self, attr, patched)
        return self


class SpanTestDouble:
    def __init__(self, text, label) -> None:
        self.text = text
        self.label_ = label
