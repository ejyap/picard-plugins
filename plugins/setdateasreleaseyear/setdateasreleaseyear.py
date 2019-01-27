PLUGIN_NAME = 'Date As Release Year'
PLUGIN_AUTHOR = 'Eduardo Yap'
PLUGIN_DESCRIPTION = 'Sets date to the release year (yyyy).'
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15", "0.16", "2.0"]

import re
from picard.metadata import register_track_metadata_processor


_year_re = re.compile(r"\d{4}", re.IGNORECASE)


def set_date_as_release_year(tagger, metadata, release, track):
    m = re.search(_year_re, metadata["date"])
    if m:
        metadata["date"] = m.group(0)

register_track_metadata_processor(set_date_as_release_year)

