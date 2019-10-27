from flask_restful import Resource
import logging as logger

class TaskByID(Resource):

    def get(self, taskID):
        logger.debug("Get Method:")
        return {"message" : f"inside get method of Task by ID: {taskID}"}, 200
    def post(self, taskID):
        logger.debug("Post Method:")
        return {"message" : f"inside get method of Task by ID: {taskID}"}, 200
    def put(self, taskID):
        logger.debug("Put Method:")
        return {"message" : f"inside get method of Task by ID: {taskID}"}, 200
    def delete(self, taskID):
        logger.debug("Delete Method:")
        return {"message" : f"inside get method of Task by ID: {taskID}"}, 200
