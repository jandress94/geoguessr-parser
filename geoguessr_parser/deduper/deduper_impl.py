from geopy import distance
import itertools

from geoguessr_parser.deduper.deduper import DeDuper


class DeDuperImpl(DeDuper):
    def __init__(self, dist_cutoff_ft=50, lat_long_precision=3):
        self.locs = {}
        self.dist_cutoff_ft = dist_cutoff_ft
        self.lat_long_precision = lat_long_precision

    def add_locs(self, locs):
        for l1 in locs:
            buckets, l1_bucket = self.get_buckets(l1)

            match = False
            for bucket in buckets:
                for l2 in self.locs.get(bucket, []):
                    if match or distance.distance(l1, l2).feet < self.dist_cutoff_ft:
                        match = True
                        break

            if not match:
                if l1_bucket not in self.locs:
                    self.locs[l1_bucket] = set()

                self.locs[l1_bucket].add(l1)

    def get_buckets(self, loc):
        def _get_buckets(x):
            x_rnd = round(x, self.lat_long_precision)
            delta = pow(10, -1 * self.lat_long_precision)
            return f'{x_rnd:.6f}', f'{x_rnd - delta:.6f}', f'{x_rnd + delta:.6f}'

        lat_buckets = _get_buckets(loc[0])
        long_buckets = _get_buckets(loc[1])

        return itertools.product(lat_buckets, long_buckets), (lat_buckets[0], long_buckets[0])

    def get_locs(self):
        return set().union(*self.locs.values())
