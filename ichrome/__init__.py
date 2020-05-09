from .async_utils import Chrome as AsyncChrome
from .async_utils import Tab as AsyncTab
from .base import (AsyncChromeDaemon, Chrome, ChromeDaemon, ChromeWorkers, Tab,
                   Tag)
from .logs import logger

__version__ = "1.1.5"
__tips__ = "[github]: https://github.com/ClericPy/ichrome\n[cdp]: https://chromedevtools.github.io/devtools-protocol/\n[cmd args]: https://peter.sh/experiments/chromium-command-line-switches/"
__all__ = [
    'Chrome', 'ChromeDaemon', 'Tab', 'Tag', 'AsyncChrome', 'AsyncTab', 'logger',
    'AsyncChromeDaemon'
]
