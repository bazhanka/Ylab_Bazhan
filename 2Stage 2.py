from datetime import datetime, timedelta
from typing import Generator


class Movie:
    def __init__(self, title, dates):
        self.title = title
        self.dates = dates

    @property
    def schedule(self) -> Generator[datetime, None, None]:
        for el in self.dates:
            start = el[0] - timedelta(1)
            stop = el[-1]
            while start < stop:
                start += timedelta(1)
                yield start


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule:
    print(d)
