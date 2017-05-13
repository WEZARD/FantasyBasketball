# -*- coding: utf-8 -*-

import boto3
import json

__author__ = 'zx'
__date__ = '12/05/2017 15:30'

sqs = boto3.resource('sqs')
sns = boto3.client('sns')
queue = sqs.get_queue_by_name(QueueName='FantansyBasketball')
arn = 'arn:aws:sns:us-east-1:993294956953:Twitt'


def worker(queue):
    messages = queue.receive_messages(MessageAttributeNames=['name', 'fantasy_score', 'isGameOver'])
    if len(messages) > 0:
        for message in messages:
            if message.message_attributes is not None:
                name = message.message_attributes.get('name')
                fantasy_score = message.message_attributes.get('fantasy_score')
                isGameOver = message.message_attributes.get('isGameOver')

                sns_message = {"name": name, "fantasy_score": fantasy_score, "isGameOver": isGameOver}
                sns.publish(TargetArn=arn, Message=json.dumps({'newNbaData': json.dumps(sns_message)}))

            message.delete()
