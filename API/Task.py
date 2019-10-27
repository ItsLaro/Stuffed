from flask_restful import Resource
import logging as logger

class Task1(Resource):

    def get(self):
        logger.debug("Get Method:")
        return {"message" : "inside get method of Task 1"}, 200
    def post(self):
        logger.debug("Post Method:")
        return {"message" : "inside post method of Task 1"}, 200
    def put(self):
        logger.debug("Put Method:")
        return {"message" : "inside put method of Task 1"}, 200
    def delete(self):
        logger.debug("Delete Method:")
        return {"message" : "inside debug method of Task 1"}, 200

class Task2(Resource):

    def get(self):
        logger.debug("Get Method:")
        return {"message" : "inside get method inside of Task 2"}, 200
    def post(self):
        logger.debug("Post Method:")
        return {"message" : "inside post method of Task 2"}, 200
    def put(self):
        logger.debug("Put Method:")
        return {"message" : "inside put method of Task 2"}, 200
    def delete(self):
        logger.debug("Delete Method:")
        return {"message" : "inside debug method of Task 2"}, 200
