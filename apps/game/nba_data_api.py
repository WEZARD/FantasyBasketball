# -*- coding: utf-8 -*-
import httplib
import urllib
import json
import boto3

__author__ = 'zx'
__date__ = '11/05/2017 20:05'

sqs = boto3.resource('sqs', region_name='us-west-1')
queue = sqs.get_queue_by_name(QueueName='FantansyBasketball')

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '587dff62c4ac473fad2a599ea1d2e0aa',
}

params = urllib.urlencode({
})


def getNewNbaData(date, playerID):
    try:
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

        # Send data to sqs
        # queue_data = {
        #     'name': {'DataType': 'String', 'StringValue': jsondata['Name']},
        #     'isGameOver': {'DataType': 'String', 'StringValue': str(jsondata['IsGameOver'])},
        #     'TotalReboundsPercentage': {'DataType': 'String', 'StringValue': str(jsondata['TotalReboundsPercentage'])},
        #     'Points': {'DataType': 'String', 'StringValue': str(jsondata['Points'])},
        #     'Assists': {'DataType': 'String', 'StringValue': str(jsondata['Assists'])},
        #     'Rebounds': {'DataType': 'String', 'StringValue': str(jsondata['Rebounds'])},
        #     'AssistsPercentage': {'DataType': 'String', 'StringValue': str(jsondata['AssistsPercentage'])},
        #     'FreeThrowsPercentage': {'DataType': 'String', 'StringValue': str(jsondata['FreeThrowsPercentage'])},
        #     'TwoPointersPercentage': {'DataType': 'String', 'StringValue': str(jsondata['TwoPointersPercentage'])},
        #     'ThreePointersPercentage': {'DataType': 'String', 'StringValue': str(jsondata['ThreePointersPercentage'])}
        # }
        # queue.send_message(MessageBody="NewNbaData", MessageAttributes=queue_data)

        conn.close()
        return playerStatus
    except Exception as e:
        print("[Errno: {0}]".format(e.message))
