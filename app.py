import pandas
from app.word_counter import count_words
from cli.core import output_error, show_info, prompt_user, get_input
from constants.cli_constants import MANUALLY, CLIPBOARD, EXIT
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
    sys.path.append('../')
    show_info()
    txt: str
    while True:
        try:
            chosen_command = prompt_user().get('input')
            if chosen_command == MANUALLY:
                txt = get_input()
            elif chosen_command == CLIPBOARD:
                txt = pandas.read_clipboard()
                txt = str(' '.join(txt))
            else:
                exit(code=0)

            sorted_df = count_words(txt)

            # visualization using bar chart
            sorted_df.plot(x='Word', y='Frequency', kind='bar')
            plt.xlabel('Words')
            plt.ylabel('Frequency')
            plt.title('Word Frequency Bar Chart')
            plt.show()
        except pandas.errors.EmptyDataError as e:
            output_error("Try copying the text again into your clipboard")
        except ValueError as e:
            output_error(str(e))
