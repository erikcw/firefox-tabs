from __future__ import print_function
import argparse
import json
import lz4
import os
import sys

def load_data(path):
    """
    Parse compressed Firefox session file and return json.

    Example path:
    path = '~/Library/Application Support/Firefox/Profiles/495vnzik.Default User/sessionstore-backups/recovery.jsonlz4'
    """
    mozlz4_magic = b'mozLz40\x00'
    with open(path, 'rb') as f:
        data = f.read()
    session_data = json.loads(lz4.block.decompress(data.replace(mozlz4_magic, b'', 1)))
    return session_data


def list_open_tabs(path):
    path = os.path.expanduser(path)

    session_data = load_data(path)

    for window_idx, window in enumerate(session_data['windows']):
        for tab in window['tabs']:
            current_tab = tab['entries'][-1]
            output = {
                'url': current_tab['url'],
                'title': current_tab['title'],
                'window': window_idx,
            }
            print(json.dumps(output))


def main():
    sample_path = '~/Library/Application Support/Firefox/Profiles/495vnzik.Default User/sessionstore-backups/recovery.jsonlz4'
    parser = argparse.ArgumentParser(description='List your open Firefox tabs.')
    parser.add_argument('path', metavar='recovery.jsonlz4 path', type=str,
                        help='The path to your Firefox profile recover.jsonlz4 file (ie {0})'.format(sample_path))

    args = parser.parse_args()

    list_open_tabs(args.path)

if __name__ == "__main__":
    main()
