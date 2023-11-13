from juriscraper.opinions.united_states.state import nj


class Site(nj.Site):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.court_id = self.__module__
        self.url = "https://www.njcourts.gov/attorneys/opinions/published-tax"
        self.status = "Published"
