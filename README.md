# firefox-tabs
List your open Firefox tabs.

## Installation

`pip install firefox-tabs`

## Useage

From the cli:

`fftabs "~/Library/Application Support/Firefox/Profiles/410vnzik.Default User/sessionstore-backups/recovery.jsonlz4"`

From python:

```python
from firefox_tabs import list_data
import os

path = "~/Library/Application Support/Firefox/Profiles/410vnzik.Default User/sessionstore-backups/recovery.jsonlz4"
path = os.path.expanduser(path)

# retrieve all data about the current firefox session.
session_data = load_data(path)
```
