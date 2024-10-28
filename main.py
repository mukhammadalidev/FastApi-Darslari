from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
  return {"message":{"name":"Anvar"}}


@app.get("/about")
def about():
  return {"Page":{"about":"heyy"}}