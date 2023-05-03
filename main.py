from fastapi import FastAPI
from fastapi.responses import Response
import os
import json
import sys
import platform
import sysconfig

app = FastAPI()

@app.get("/")
def root():
    json_str = json.dumps(foo(), indent=4, default=str)
    return Response(content=json_str, media_type='application/json')

def foo():
    return {"{:<30}".format("System name (os.name)"): os.name, 
            "{:<30}".format("Platform name (sys.platform)"):  sys.platform,
            "{:<30}".format("System/OS name"):  platform.system(),
            "{:<30}".format("Platform"):  sysconfig.get_platform(),
            "{:<30}".format("Machine type"):  platform.machine(),
            "{:<30}".format("Machine architecture"):  platform.architecture()}
