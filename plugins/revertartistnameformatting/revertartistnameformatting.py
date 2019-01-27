PLUGIN_NAME = 'Revert Artist Name Formatting'
PLUGIN_AUTHOR = 'Eduardo Yap'
PLUGIN_DESCRIPTION = 'Revert formatting of [First Name] [Last Name] to [Last Name], [First Name] in Album Artist Sort Order and Artist Sort Order metadata.'
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15", "0.16", "2.0"]

import re
from picard.metadata import register_track_metadata_processor


def isascii(s):
    return len(s) == len(s.encode())

def revert_artist_name_formatting(tagger, metadata, release, track):
    albumartist = metadata["albumartist"]
    if not albumartist.lower().startswith("the ") and not albumartist.lower().startswith("a ") and isascii(albumartist):
        metadata["albumartistsort"] = albumartist
        metadata["artistsort"] = albumartist


register_track_metadata_processor(revert_artist_name_formatting)

