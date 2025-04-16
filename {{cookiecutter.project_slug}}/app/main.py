from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
import uvicorn
from uvicorn.supervisors import ChangeReload

# Example router delete and add your own
from routers.example import router as example_router


from settings import Settings


def get_app(settings: Settings) -> FastAPI:
    origins = [
        "http://localhost:3000",
    ]

    # Create and run app
    _app = FastAPI(title="{{cookiecutter.project_name}}", debug=True, dependencies=[])
    _app.state.settings = settings
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    _app.include_router(example_router)

    return _app

settings = Settings.load()
app = get_app(settings=settings)

## Add a basic fastapi endpoint
@app.get("/")
async def root():
    return {"message": "Hello World!"}   

if __name__ == "__main__":
    config = uvicorn.Config("main:app", host="0.0.0.0", port={{cookiecutter.webapp_port}}, reload=True)
    server = uvicorn.Server(config)
    ChangeReload(config, target=server.run, sockets=[config.bind_socket()]).run()
