from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class Server:
    def __init__(self):
        self.app = FastAPI(
            title='rental App'
        )
        self.origins = ['*']

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=self.origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


server = Server()
