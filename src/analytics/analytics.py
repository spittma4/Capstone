#stuart

from . import private
import json
from watson_developer_cloud import ToneAnalyzerV3

class Analytics:
    tone_analyzer = None

    def __init__(self):
        self.tone_analyzer = ToneAnalyzerV3(
            username=private.kss_tone_username,
            password=private.kss_tone_password,
            version='2017-09-26')
    
    def watson_parser(self,json_item):
        items=json_item['document_tone']['tones']
        result={}
        for item in items:
            result[item['tone_id']]=item['score']
        return result

    def watson_setup(self,post):
        if (not (isinstance(post, str))):
            post=str(post)
        return post

    def watson_send(self,text):
        tone=self.tone_analyzer.tone(tone_input=text,
                              content_type='text/plain')
        return tone

    def sentement_analyis(self,posts):
        result=[]
        for post in posts:
            data=self.watson_setup(post)
            ans=self.watson_send(data)
            result.append(self.watson_parser(ans))
        result=self.aggrigate(result)
        return result

    def aggrigate(self,sentment):
        result={}
        length=len(sentment)
        for item in sentment:
            for key,value in item.items():
                if key in result.keys():
                    result[key]+=value
                else:
                    result[key]=value

        for key in result:
            result[key]=result[key]/length

        return result
