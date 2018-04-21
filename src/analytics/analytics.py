#stuart

import private
import json
from watson_developer_cloud import ToneAnalyzerV3

class Analtics:
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
        print(json.dumps(tone))
        return tone

    def sentement_analyis(self,posts):
        result=[]
        num_posts=len(posts)
        for post in posts:
            data=self.watson_setup(post)
            ans=self.watson_send(data)
            result.append(self.watson_parser(ans))
        return result

    def aggrigate(self,sentment):
        result={}
        length=len(sentment)
        for item in sentment:
            for key in item:
                if key in result.keys():
                    result[key]+=sentment[key]
                else:
                    print(key)                    
                    result[key]=sentment[key]

        for key in result:
            result[key]=result[key]/length

        return result
