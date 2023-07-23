from typing import List
import pandas


def count_words(txt: str) -> pandas.DataFrame:
    words: List[str] = txt.split()
    # spliting the spaces
    frequency: dict = {}

    for word in words:
        # striping symbols and making lower case
        cleaned = word.strip(".?!,:;").lower()

        # "0" is a default value to be returned if the key is not present in the dictionary
        frequency[cleaned] = frequency.get(cleaned, 0) + 1

    frequency_df = pandas.DataFrame(
        frequency.items(), columns=['Word', 'Frequency'])

    return frequency_df.sort_values(by='Frequency', ascending=False)
