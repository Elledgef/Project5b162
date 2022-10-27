#Author: Faith Elledge
#Github user: Elledgef
#Date: 10/26/22
#Description: Imports a json file containing data from the Nobel prizes through out the years
import json


class NobelData:

    def __init__(self):
        """ Imports data from nobel Json file"""
        with open ('nobels.json', 'r') as infile:
            self._nobels_data = json.load(infile)['data']

    def search_nobel(self, year, category):
        """ Allows user to search for winners by name, year and category"""
        category_list= [ 'chemistry', 'economics', 'literature', 'peace', 'physics', 'medicine']
        surname_of_winners = []
        self._nobels_data = ['prizes']
        self._category = category
        self._year = str()

        for prize_winner in self._nobels_data:
            if prize_winner ['year'] == self._year and prize_winner['category'] == category_list:
                surname_of_winners = self._nobels_data(prize_winner['surname'])
            return sorted(surname_of_winners)

