from typing import Optional

ACTIVATE: str
CURSOR_DOWN: str
CURSOR_LEFT: str
CURSOR_MAX_LEFT: str
CURSOR_MAX_RIGHT: str
CURSOR_PAGE_DOWN: str
CURSOR_PAGE_UP: str
CURSOR_RIGHT: str
CURSOR_UP: str
REDRAW_SCREEN: str

class CommandMap(object):
    def __init__(self) -> None:
    def __delitem__(self, key: str) -> None: ...
    def __getitem__(self, key: str) -> Optional[str]: ...
    def __setitem__(self, key: str, command: str) -> None: ...
    def clear_command(self, command: str) -> None: ...
    def copy(self) -> 'CommandMap': ...
    def restore_defaults(self) -> None: ...

command_map: CommandMap
