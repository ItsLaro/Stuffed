from flask_restful import Api

from Stuffed import app
from API.Vision import Vision_Setup
from API.TaskByID import TaskByID

restServer = Api(app)

restServer.add_resource(Vision_Setup, "/api/vision/<string:image_url>")
restServer.add_resource(TaskByID, "/api/v0.1/task/id/<string:taskID>")