"""Console script for projet_rochet."""
import projet_rochet

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for projet_rochet."""
    console.print("Replace this message by putting your code into "
               "projet_rochet.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
