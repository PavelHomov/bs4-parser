from pathlib import Path

WHATS_NEW_URL = 'https://docs.python.org/3/whatsnew/'

MAIN_DOC_URL = 'https://docs.python.org/3/'

DOWNLOADS_URL = 'https://docs.python.org/3/download.html'

MAIN_PEP_URL = 'https://peps.python.org/'

BASE_DIR = Path(__file__).parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'

DT_FORMAT = '%d.%m.%Y %H:%M:%S'

EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}
