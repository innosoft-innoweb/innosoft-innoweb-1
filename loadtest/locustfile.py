from locust import HttpUser, SequentialTaskSet, TaskSet, task, between

"""
Para ejecutar los tests de carga:
    1. Vaciar tablas de la base de datos
    2. Para poblarla con datos estáticos, ejecutar el siguiente comando: python manage.py loaddata "fixtures/initial.json"
"""

HOST = "http://localhost:8000"
PARTICIPANT_ID = 2
EVENT_ID = 1


class DefHome(TaskSet):
    @task
    def home(self):
        self.client.get("")


class DefLogin(TaskSet):
    @task
    def login(self):
        self.client.get("/login")


class DefRegister(TaskSet):
    @task
    def register(self):
        self.client.get("/registro")


class DefParticipantProfile(TaskSet):
    @task
    def participant_profile(self):
        self.client.get("/participante/{0}".format(PARTICIPANT_ID))


class DefEventDetails(TaskSet):
    @task
    def event_details(self):
        self.client.get("/evento/{0}".format(EVENT_ID))


class Home(HttpUser):
    host = HOST
    tasks = [DefHome]
    wait_time = between(3, 5)


class Login(HttpUser):
    host = HOST
    tasks = [DefLogin]
    wait_time = between(3, 5)


class Register(HttpUser):
    host = HOST
    tasks = [DefRegister]
    wait_time = between(3, 5)


class ParticipantProfile(HttpUser):
    host = HOST
    tasks = [DefParticipantProfile]
    wait_time = between(3, 5)


class EventDetails(HttpUser):
    host = HOST
    tasks = [DefEventDetails]
    wait_time = between(3, 5)
