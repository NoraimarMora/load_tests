from locust import HttpLocust, TaskSet, task
from random import randint

class MyTaskSet(TaskSet):
    def on_start(self):
        self.client.post("/login", {
            "email": "noraimar.mora@gmail.com",
            "password": "tesiscriminal01"
        })

    @task(6)
    def categories(self):
        self.client.request(method="GET",
            url="/categories",
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkYjYzODliYjAzMDU4MDAyMGEyZDBlOSIsImVtYWlsIjoibm9yYWltYXIubW9yYUBnbWFpbC5jb20iLCJpYXQiOjE1NzIyMjU0MzMsImV4cCI6MTU3MzQzNTAzM30.pVB8sCJ3d6L8KvrLPn-B3cIP4KZaG5DdPfclW_HV0k4"
            }
        )

    @task(6)
    def brands(self):
        id = randint(1, 5)
        self.client.request(method="GET",
            url="/categories/" + str(id) + "/brands",
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkYjYzODliYjAzMDU4MDAyMGEyZDBlOSIsImVtYWlsIjoibm9yYWltYXIubW9yYUBnbWFpbC5jb20iLCJpYXQiOjE1NzIyMjU0MzMsImV4cCI6MTU3MzQzNTAzM30.pVB8sCJ3d6L8KvrLPn-B3cIP4KZaG5DdPfclW_HV0k4"
            }
        )

    @task(5)
    def products(self):
        id = randint(1, 25)
        self.client.request(method="GET",
            url="/brands/" + str(id) + "/products",
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkYjYzODliYjAzMDU4MDAyMGEyZDBlOSIsImVtYWlsIjoibm9yYWltYXIubW9yYUBnbWFpbC5jb20iLCJpYXQiOjE1NzIyMjU0MzMsImV4cCI6MTU3MzQzNTAzM30.pVB8sCJ3d6L8KvrLPn-B3cIP4KZaG5DdPfclW_HV0k4"
            }
        )

    @task(1)
    def profile(self):
        self.client.request(method="GET",
            url="clients/5db6389bb030580020a2d0e9",
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkYjYzODliYjAzMDU4MDAyMGEyZDBlOSIsImVtYWlsIjoibm9yYWltYXIubW9yYUBnbWFpbC5jb20iLCJpYXQiOjE1NzIyMjU0MzMsImV4cCI6MTU3MzQzNTAzM30.pVB8sCJ3d6L8KvrLPn-B3cIP4KZaG5DdPfclW_HV0k4"
            }
        )

    @task(1)
    def addresses(self):
        self.client.request(method="GET",
            url="clients/5db6389bb030580020a2d0e9/addresses",
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkYjYzODliYjAzMDU4MDAyMGEyZDBlOSIsImVtYWlsIjoibm9yYWltYXIubW9yYUBnbWFpbC5jb20iLCJpYXQiOjE1NzIyMjU0MzMsImV4cCI6MTU3MzQzNTAzM30.pVB8sCJ3d6L8KvrLPn-B3cIP4KZaG5DdPfclW_HV0k4"
            }
        )

    @task(2)
    def cart(self):
        self.client.request(method="GET",
            url="clients/5db6389bb030580020a2d0e9/cart",
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkYjYzODliYjAzMDU4MDAyMGEyZDBlOSIsImVtYWlsIjoibm9yYWltYXIubW9yYUBnbWFpbC5jb20iLCJpYXQiOjE1NzIyMjU0MzMsImV4cCI6MTU3MzQzNTAzM30.pVB8sCJ3d6L8KvrLPn-B3cIP4KZaG5DdPfclW_HV0k4"
            }
        )

    @task(2)
    def orders(self):
        self.client.request(method="GET",
            url="clients/5db6389bb030580020a2d0e9/orders",
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkYjYzODliYjAzMDU4MDAyMGEyZDBlOSIsImVtYWlsIjoibm9yYWltYXIubW9yYUBnbWFpbC5jb20iLCJpYXQiOjE1NzIyMjU0MzMsImV4cCI6MTU3MzQzNTAzM30.pVB8sCJ3d6L8KvrLPn-B3cIP4KZaG5DdPfclW_HV0k4"
            }
        )

    @task(2)
    def orderDetail(self):
        i = randint(0, 3)
        order = ["5db900668b19fa0022347851", "5db9dd6efd04b30021d9b35c", "5db9e99b951a4e00211d3988", "5dba703c951a4e00211d398d"]
        self.client.request(method="GET",
            url="orders/" + order[i],
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkYjYzODliYjAzMDU4MDAyMGEyZDBlOSIsImVtYWlsIjoibm9yYWltYXIubW9yYUBnbWFpbC5jb20iLCJpYXQiOjE1NzIyMjU0MzMsImV4cCI6MTU3MzQzNTAzM30.pVB8sCJ3d6L8KvrLPn-B3cIP4KZaG5DdPfclW_HV0k4"
            }
        )

    @task(2)
    def addCartItem(self):
        id = randint(1, 125)
        i = randint(0, 3)
        cart = ["5dba71a8ac9bb10021220ecf", "5dba71d5db65500020a5718e", "5dba71edac9bb10021220ed1", "5dba71fbac9bb10021220ed3"]
        self.client.request(method="POST",
            url="carts/" + cart[i] + "/add",
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkYjYzODliYjAzMDU4MDAyMGEyZDBlOSIsImVtYWlsIjoibm9yYWltYXIubW9yYUBnbWFpbC5jb20iLCJpYXQiOjE1NzIyMjU0MzMsImV4cCI6MTU3MzQzNTAzM30.pVB8sCJ3d6L8KvrLPn-B3cIP4KZaG5DdPfclW_HV0k4"
            },
            data={
                "id": id,
                "quantity": randint(1, 10),
                "unit_price": randint(10000, 100000)
            }
        )

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 10000