from penelope.dictionary import Dictionary, DictionaryEntry
import re

regex = re.compile("[\[({][^\])}]*[\])}]")

def parse(dictionary, args):
    """
    Transforms this dictionary so that all headwords
    are changed to not contain any [..], {..} or (..) parts.
    Either use this parse function OR transform_headword (see below).

    Given the input dictionary and arguments,
    return a (possibly, modified) dictionary.

    The returned dictionary might be the same (input) instance,
    or a new one.

    :param dictionary: the (raw) input dictionary
    :type  dictionary: Dictionary
    :param arguments: the command line arguments
    :type  arguments: Namespace from argparse
    :rtype: Dictionary
    """
    if dictionary is None:
        return
    res: Dictionary = Dictionary(dictionary.metadata)
    entry: DictionaryEntry
    for entry in dictionary.entries:
        newHeadword = transform_headword(entry.headword)
        res.add_entry(headword=newHeadword, definition=entry.definition)
    return res

def transform_headword(headword):
    if headword is None: return None
    return regex.sub("", headword).strip()
