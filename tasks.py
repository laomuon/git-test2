import os
from invoke import task,run

@task
def ls():
    path=os.path.dirname(os.getcwd())
    print(os.listdir(path))
    #run("cd ..")
    #cmd="ls -la"
    #run(cmd)
