import json


class SearchByTag:
    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
      # data 없는경우
        if not self._data or not self._data["items"]:
            raise StopIteration
        movies = self._data['items']
        for movie in movies:
          # tags 없는경우
            if 'tags' in movie and self.query in movie['tags']:
                yield movie

    def first(self):
        if not self._data or not self._data["items"]:
            raise StopIteration
        movies = self._data['items']
        for movie in movies:
            if not 'tags' in movie:
                raise StopIteration
            if 'tags' in movie and self.query in movie['tags']:
                return movie


s = SearchByTag(
    '/Users/macintoshhd/Project/algorithmPython/codingTest/DeliveryHero/nono.json', 'crime')
for i in s.search():
    print(i)

# print(s.first())
