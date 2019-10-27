from flask_restful import Resource
import logging as logger

class Vision(Resource):

    def get(self, image_url):

        from clarifai.rest import ClarifaiApp, Image

        app = ClarifaiApp(api_key='2a018a8bc2e443f9912f4f962c1a4653')

        model = app.models.get('food-items-v1.0')
        image = Image(url="https://samples.clarifai.com/" + image_url + ".jpg")
        result_items = model.predict([image])['outputs'][0]['data']['concepts']
        result_list = []
        for tag in range(len(result_items)):
            result_item =result_items[tag]['name']
            result_list.append(result_item)

        return {"message" : result_list}