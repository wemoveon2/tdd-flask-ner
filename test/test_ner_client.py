import unittest
from ner_client import NamedEntityClient
from test_doubles import NerTestDouble


class TestNERClient(unittest.TestCase):
    # { ents: [{...}],
    # html: "<span>..."}

    def test_get_ents_returns_dict_given_empty_str_causes_empty_spacy_doc_ents(self):
        model = NerTestDouble(
            "eng"
        )  # behaves like the spacy model but doesn't load the entire thing
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dict_given_nonempty_str_causes_empty_spacy_doc_ents(self):
        model = NerTestDouble("eng")
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in Wisconsin")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerTestDouble("eng")
        doc_ents = [{"text": "Bill Gates", "label_": "PERSON"}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_results = {
            "ents": [{"ent": "Bill Gates", "label": "Person"}],
            "html": "",
        }
        self.assertListEqual(result["ents"], expected_results["ents"])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerTestDouble("eng")
        doc_ents = [{"text": "Illuminati", "label_": "NORP"}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_results = {
            "ents": [{"ent": "Illuminati", "label": "Group"}],
            "html": "",
        }
        self.assertListEqual(result["ents"], expected_results["ents"])
    
    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NerTestDouble("eng")
        doc_ents = [{"text": "Toronto", "label_": "LOC"}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_results = {
            "ents": [{"ent": "Toronto", "label": "Location"}],
            "html": "",
        }
        self.assertListEqual(result["ents"], expected_results["ents"])
    
    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        model = NerTestDouble("eng")
        doc_ents = [{"text": "ASL", "label_": "LANGUAGE"}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_results = {
            "ents": [{"ent": "ASL", "label": "Language"}],
            "html": "",
        }
        self.assertListEqual(result["ents"], expected_results["ents"])
    
    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        model = NerTestDouble("eng")
        doc_ents = [{"text": "Australia", "label_": "GPE"}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_results = {
            "ents": [{"ent": "Australia", "label": "Location"}],
            "html": "",
        }
        self.assertListEqual(result["ents"], expected_results["ents"])
    
    def test_get_ents_given_multiple_ents_serializes_all(self):
        model = NerTestDouble("eng")
        doc_ents = [{"text": "Australia", "label_": "GPE"}, {'text': 'Jeff Besos', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_results = {
            "ents": [{"ent": "Australia", "label": "Location"}, {'ent': 'Jeff Besos', 'label': 'Person'}],
            "html": "",
        }