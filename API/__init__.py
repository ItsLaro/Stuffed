from flask_restful import Api

from Stuffed import app
from API.Task import Task1, Task2
from API.TaskByID import TaskByID

restServer = Api(app)

restServer.add_resource(Task1, "/api/v0.1/task1")
restServer.add_resource(Task2, "/api/v0.1/task2")
restServer.add_resource(TaskByID, "/api/v0.1/task/id/<string:taskID>")