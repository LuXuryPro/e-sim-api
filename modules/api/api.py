#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from network import SimpleUrl
from network import CustomUrl

class OfficialApi:
    '''Wrapper around official e-sim's API
    For more info see wiki page http://wiki.e-sim.org/index.php/API'''
    def __init__(self, server):
        if server == 0:
            self.n = SimpleUrl("http://primera.e-sim.org/")
        elif server == 1:
            self.n = SimpleUrl("http://secura.e-sim.org/")

    def get_citizen_by_id(self,citizenId):
        page=self.n.open_url('apiCitizenById.html?id='+citizenId)
        return json.loads(page.read())

    def get_citizen_by_name(self,name):
        page=self.n.open_url('apiCitizenByName.html?name='+name)
        return json.loads(page.read())

    def get_military_unit_by_id(self,mu_id):
        page=self.n.open_url('apiMilitaryUnitById.html?id='+mu_id)
        return json.loads(page.read())

    def get_military_unit_members_list(self,mu_id):
        page=self.n.open_url('apiMilitaryUnitMembers.html?id='+mu_id)
        return json.loads(page.read())

    def get_countries_list(self):
        page=self.n.open_url('apiCountries.html')
        return json.loads(page.read())

    def get_ranks(self):
        page=self.n.open_url('apiRanks.html')
        return json.loads(page.read())

    def get_map_data(self):
        page=self.n.open_url('apiMap.html')
        return json.loads(page.read())

    def get_regions_data(self):
        page=self.n.open_url('apiRegions.html')
        return json.loads(page.read())

class UnofficialAPI:
    def __init__(self,server):
        self.o=CustomUrl()
        self.server=server

    def get_battle_info(self,battleId,round,format='json'):
        page=self.o.open('http://api.cscpro.org/esim/'+self.server+'/battle/'+battleId+'/'+round+'.'+format)
        return json.loads(page.read())
