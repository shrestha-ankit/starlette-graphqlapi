from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from ariadne.asgi import GraphQL
from app.schema.schema import schema


app = Starlette()

app.add_middleware(CORSMiddleware
                   ,allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )


app.mount("/graphql", GraphQL(schema=schema, debug=True))


