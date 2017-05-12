# -*- coding: utf-8 -*-
import httplib
import urllib
import base64
import json
import requests
import gevent

__author__ = 'zx'
__date__ = '11/05/2017 20:05'

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '587dff62c4ac473fad2a599ea1d2e0aa',
}

params = urllib.urlencode({
})


def getNewData(date, playerID):
    conn = httplib.HTTPSConnection('api.fantasydata.net')
    requestData = "/v3/nba/stats/JSON/PlayerGameStatsByPlayer/{0}/{1}?%s".format(date, playerID)
    conn.request("GET", requestData % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    jsondata = json.loads(data)

    playerStatus = {
        'name': jsondata['Name'],
        'fantasy_score': jsondata['FantasyPoints'],
        'isGameOver': jsondata['IsGameOver']
    }

    return playerStatus

