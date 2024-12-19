import typer

from typing_extensions import Annotated
from typing import *

def what(
    create: Annotated[bool, typer.Argument(help='Whether the what information should be created')] = True,
    np: Annotated[bool, typer.Argument(help='Whether placeholders should be removed from the created what file')] = False,
):
    if create:
        pass