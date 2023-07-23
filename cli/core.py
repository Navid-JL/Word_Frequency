from pytz import VERSION
from rich.console import Console
from rich.align import Align
from inquirer import List, prompt
from constants.cli_constants import APP_NAME, YEAR, VERSION, APP_DESCRIPTION
from constants.cli_theme import custom_theme


def show_info() -> None:
    """Show basic Information about the App
    """
    console = Console(theme=custom_theme)
    """Show basic information about the Word Frequency Counter."""
    console.print(Align.center(
        f"[bold yellow]{APP_NAME}[/] - [info]{YEAR}[/info][info] - [bold]V[/bold]{VERSION}[/info]\n"))
    console.print(Align.center(
        f"[info][bold]{APP_DESCRIPTION}[/bold][/info]\n"))
