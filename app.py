import pandas
from cli.core import output_error, show_info, prompt_user, get_input
from constants.cli_constants import MANUALLY, CLIPBOARD, EXIT
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
    sys.path.append('../')
    show_info()
    chosen_command = prompt_user().get('input')
    txt: str
    try:
        if chosen_command == MANUALLY:
            txt = get_input()
        elif chosen_command == CLIPBOARD:
            txt = pandas.read_clipboard().index(-1)
            txt = str(' '.join(txt))
        else:
            exit(code=0)
    except pandas.errors.EmptyDataError as e:
        output_error("Try copying the text again into your clipboard")
    except ValueError as e:
        output_error(str(e))

    # words = txt.split()
    # # spliting the spaces
    # frequency = {}

    # for word in words:
    #     cleaned = word.strip(".?!,:;").lower()
    #     # striping symbols and making lower case

    #     frequency[cleaned] = frequency.get(cleaned, 0) + 1
    #     # "0" is a default value to be returned if the key is not present in the dictionary

    # frequency_df = pandas.DataFrame(
    #     frequency.items(), columns=['Word', 'Frequency'])

    # sorted_df = frequency_df.sort_values(by='Frequency', ascending=False)

    # sorted_df.plot(x='Word', y='Frequency', kind='bar')
    # plt.xlabel('Words')
    # plt.ylabel('Frequency')
    # plt.title('Word Frequency Bar Chart')
    # plt.show()
    # # visualization using bar chart
