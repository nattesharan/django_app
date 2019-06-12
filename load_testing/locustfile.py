from locust import HttpLocust, TaskSet, task

class UserBehaviour(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()
    
    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()
    
    def login(self):
        response = self.client.post('/api/v1/auth/me/login/', {"username": "nattesharan@gmail.com","password": "13341a05a7"})
        data = response.json()
        self.token = data['token']
    
    def logout(self):
        self.client.post('/api/v1/auth/me/logout/', headers={'Authorization': 'Token {}'.format(self.token)})
    
    @task(5)
    def users(self):
        self.client.get('/api/v1/users/', headers={'Authorization': 'Token {}'.format(self.token)})

class User(HttpLocust):
    task_set = UserBehaviour
    min_wait = 5000
    max_wait = 9000

# added locust for load testing
# locust -f locust_files/my_locust_file.py --host=http://localhost:8000
# start locust with the above command and then go to http://127.0.0.1:8089 and then configure total users and users per sec
# and start the load testing
