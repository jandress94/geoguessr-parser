import json

from geoguessr_parser.parsers.geoparser import GeoParser


def pprint(x, indent="", recurr_depth=2):
    if isinstance(x, dict):
        if recurr_depth > 0:
            for k, v in x.items():
                print(indent, k, ":")
                pprint(v, indent + "  ", recurr_depth - 1)
        else:
            print(indent, 'dict with keys: ', list(x.keys()))
    elif isinstance(x, list):
        print(indent, 'length', len(x), 'list.')
        if recurr_depth > 0 and len(x) > 0:
            pprint(x[0], indent + "  ", recurr_depth - 1)
    else:
        print(indent, x)


class ArcGeoParser(GeoParser):

    def parse(self, filepath):
        with open(filepath, 'r') as fp:
            data = json.load(fp)

        locs = set()
        for timeline_item in data['timelineItems']:
            try:
                locs.add((timeline_item['place']['center']['latitude'], timeline_item['place']['center']['longitude']))
            except (KeyError, TypeError):
                pass

        return locs
