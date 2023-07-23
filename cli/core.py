from pytz import VERSION
from rich.console import Console
from rich.align import Align
from inquirer import List, prompt
from constants.cli_constants import APP_NAME, YEAR, VERSION, APP_DESCRIPTION
from constants.cli_theme import custom_theme

console = Console(theme=custom_theme)


def show_info() -> None:
    """Show basic Information about the App
    """
    """Show basic information about the Word Frequency Counter."""
    console.print(Align.center(
        f"[bold yellow]{APP_NAME}[/] - [info]{YEAR}[/info][info] - [bold]V[/bold]{VERSION}[/info]\n"))
    console.print(Align.center(
        f"[info][bold]{APP_DESCRIPTION}[/bold][/info]\n"))


def prompt_user() -> dict[str, str]:
    """Prompt the user with a set of choices

    Returns:
        dict[str, str]: {'input': 'Enter manually'}
    """
    questions = [
        List(
            "input",
            message="",
            choices=["Enter manually", "Copy from clipboard", "Exit"],
        ),
    ]
    answer: dict[str, str] = prompt(questions)
    return answer


def get_input() -> str:
    txt = input(': ')
    if len(txt.strip()) == 0:
        raise ValueError("Empty value is not allowed")
    return txt
