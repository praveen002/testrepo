from fastapi import FastAPI
from fastapi import APIRouter 
from cryptography.fernet import Fernet
 
app = FastAPI()

key = bytes("o11Z3kCdtT-VmXxHMhf04aUmjFXRiAYgTvIo4EHKBfE=", 'UTF-8')
fernet = Fernet(key)
#decMessage = fernet.decrypt(bytes("gAAAAABjvB6iUv8nJRk2AapO8VtSJkOa8pP1PV_0M6FFlHq5EsWcOjF1fknp4QHhyivAj9PsE-ws2ZU4Xv8REtHpyfxlFBHX3w==", 'UTF-8')).decode()

decMessage = fernet.decrypt(bytes("gAAAAABjvmw6h5yrjv9u4qf-wfEM6G-09P4loauBhnSVgThrLqNltITNLbgUrWj_7YYNJVvVCImfwhf_z6JmGLAt_ZYqbDAe5Q==", 'UTF-8')).decode()
print(decMessage) 