from fastapi import FastAPI
from __manifest__ import __description__, __version__
import git


app = FastAPI()


@app.get('/')
async def root():
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    return {'FastAPI': {
      "version": __version__,
      "description": __description__,
      "sha": sha  
    }}