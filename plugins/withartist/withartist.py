PLUGIN_NAME = 'with Artists from Artist to Title'
PLUGIN_AUTHOR = 'Eduardo Yap'
PLUGIN_DESCRIPTION = 'Move "with" from artist names to track titles. Match is case insensitive.'
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15", "0.16", "2.0"]

from picard.metadata import register_track_metadata_processor
import re

_with_re = re.compile(r"([\s\S]+) with ([\s\S]+)", re.IGNORECASE)


def move_track_withartists(tagger, metadata, release, track):
    match_artist = _with_re.match(metadata["artist"])
    match_albumartist = _with_re.match(metadata["albumartist"])
    if match_artist and not match_albumartist:
        metadata["artist"] = match_artist.group(1)
        metadata["title"] += " (with %s)" % match_artist.group(2)
    match_artistsort = _with_re.match(metadata["artistsort"])
    if match_artistsort and not match_albumartist:
        metadata["artistsort"] = match_artistsort.group(1)


register_track_metadata_processor(move_track_withartists)

