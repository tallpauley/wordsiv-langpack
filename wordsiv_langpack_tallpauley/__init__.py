from importlib import resources
import json
from wordsiv.sources import WordCountSource
from wordsiv.models import ProbDistModel
import sys

MODULE_PATH = resources.files(sys.modules[__name__])

def _get_meta(path):
    with open(MODULE_PATH.joinpath(path), 'r') as f:
        return json.loads(f.read())

namespace = "tallpauley"

punctuation = {
    "en": {
        "start": {"": 100},
        # make no ending punctuation extremely low probability so
        # it only happens when period is not available
        "end": {"": 0.00001, ".": 100, "?": 40, "!": 20},
        "inner": {"": 100, ",": 80, "-": 40, ":": 30, ";": 20},
        "wrap": {("", ""): 100, ("“", "”"): 9, ("‘", "’"): 6},
    },
    "ar": {
        "start": {"": 100},
        # make no ending punctuation extremely low probability so
        # it only happens when period is not available
        "end": {"": 0.00001, ".": 100, "؟": 40, "!": 20},
        "inner": {"": 100, "،": 80, ":": 30, "؛": 20},
        "wrap": {("", ""): 100, ("”", "“"): 9, ("’", "‘"): 6},
    },
    "fa": {
        "start": {"": 100},
        # make no ending punctuation extremely low probability so
        # it only happens when period is not available
        "end": {"": 0.00001, ".": 100, "؟": 40, "!": 20},
        "inner": {"": 100, "،": 80, ":": 30, "؛": 20},
        "wrap": {("", ""): 100, ("”", "“"): 9, ("’", "‘"): 6},
    },
    "es": {
        "start": {"": 100},
        # make no ending punctuation extremely low probability so
        # it only happens when period is not available
        "end": {"": 0.00001, ".": 100, "!": 20},
        "inner": {"": 100, ",": 80, "-": 40, ":": 30, ";": 20},
        "wrap": {("", ""): 100, ("¿", "?"): 45, ("“", "”"): 18, ("‘", "’"): 12},
    },
}

ar_wordcount_subs = WordCountSource(
    MODULE_PATH.joinpath('data/ar_wordcount_subs.tsv'),
    _get_meta(MODULE_PATH.joinpath('data/ar_wordcount_subs_meta.json')),
)

en_wordcount_books = WordCountSource(
    MODULE_PATH.joinpath('data/en_wordcount_books.tsv'),
    _get_meta(MODULE_PATH.joinpath('data/en_wordcount_books_meta.json')),
)

es_wordcount_subs = WordCountSource(
    MODULE_PATH.joinpath('data/es_wordcount_subs.tsv'),
    _get_meta(MODULE_PATH.joinpath('data/es_wordcount_subs_meta.json')),
)

fa_wordcount_subs = WordCountSource(
    MODULE_PATH.joinpath('data/fa_wordcount_subs.tsv'),
    _get_meta(MODULE_PATH.joinpath('data/fa_wordcount_subs_meta.json')),
)

sources = {
    'ar_wordcount_subs': ar_wordcount_subs,
    'ar': ar_wordcount_subs,
    'en_wordcount_books': en_wordcount_books,
    'en': en_wordcount_books,
    'es_wordcount_subs': es_wordcount_subs,
    'es': es_wordcount_subs,
    'fa_wordcount_subs': fa_wordcount_subs,
    'fa': fa_wordcount_subs,
}

ar_prob_subs = ProbDistModel(ar_wordcount_subs, punctuation['ar'])
en_prob_books = ProbDistModel(en_wordcount_books, punctuation['en'])
es_prob_subs = ProbDistModel(es_wordcount_subs, punctuation['es'])
fa_prob_subs = ProbDistModel(fa_wordcount_subs, punctuation['fa'])

models = {
    'ar_prob_subs': ar_prob_subs,
    'ar': ar_prob_subs,
    'en_prob_books': en_prob_books,
    'en': en_prob_books,
    'es_prob_subs': es_prob_subs,
    'es': es_prob_subs,
    'fa_prob_subs': fa_prob_subs,
    'fa': fa_prob_subs
}