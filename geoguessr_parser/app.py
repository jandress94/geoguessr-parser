import os

from geoguessr_parser.parsers.arc_geoparser import ArcGeoParser
from geoguessr_parser.parsers.moves_geoparser import MovesGeoParser
from geoguessr_parser.deduper.deduper_impl import DeDuperImpl


DATA_DIR = 'data'
ARC_DIR = os.path.join(DATA_DIR, 'arc')
MOVES_DIR = os.path.join(DATA_DIR, 'moves')


def main():
    deduper = DeDuperImpl(dist_cutoff_ft=150)

    arc_parser = ArcGeoParser()

    for filename in os.listdir(ARC_DIR):
        if not filename.endswith('.json'):
            continue

        print(filename)
        deduper.add_locs(arc_parser.parse(os.path.join(ARC_DIR, filename)))

    # parse moves data
    moves_parser = MovesGeoParser()
    deduper.add_locs(moves_parser.parse(os.path.join(MOVES_DIR, 'places.json')))

    for l in deduper.get_locs():
        print(f"{l[0]}, {l[1]}")

    print(len(deduper.get_locs()))




if __name__ == '__main__':
    main()
