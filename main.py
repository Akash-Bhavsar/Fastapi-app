from fastapi import FastAPI
import git


app = FastAPI()


@app.get('/')
async def root():
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    return {'FastAPI': {
      "version": "1.0",
      "description": "my-application's description.",
      "sha": sha  
    }}