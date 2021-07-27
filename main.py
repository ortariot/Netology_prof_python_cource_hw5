import json
import requests
from simple_logger import target_logger


class WikiCountry():
    URL = 'https://en.wikipedia.org/wiki/'

    def __init__(self, filename_in, filename_out):
        self.outfile = filename_out
        with open(filename_in, 'r', encoding='utf-8') as file:
            metadata = json.load(file)
            self.countries_list = [country['name']['common']
                                   for country in metadata]
            self.end = len(self.countries_list)
        with open(self.outfile, 'w', encoding='utf-8') as file:
            file.write('[    \n')

    def __iter__(self):
        self.curssor = 0
        return self

# case - 3
    @target_logger('log.txt')
    def __next__(self):
        if self.curssor == self.end:
            with open(self.outfile, 'a', encoding='utf-8') as file:
                file.truncate(file.tell()-3)
                file.write('\n]')
            raise StopIteration

        country = self.countries_list[self.curssor]
        link = self.URL + country
        req = requests.get(link)
        self.curssor += 1

        if req.ok:
            with open(self.outfile, 'a', encoding='utf-8') as file:
                file.write('    {"country":' + '"' + country + '"' +
                           ',\n     "url": ' + '"' + link + '"' + '\n    },\n')
                return (f"{country} and it wikilink"
                        f" write to {self.outfile} file"
                        )
        else:
            return (f"info about {country} not in wiki,"
                    f" most likely this is a fictional country"
                    )


if __name__ == '__main__':
    countries = WikiCountry('countries.json', 'out.json')

    for item in countries:
        print(item)
