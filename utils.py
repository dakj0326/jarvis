
import requests
import json
# Stoppa in i jarvis.config
#HA config
URL = "http://jarvis-main:8123"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJlMmNiNTUyNTEwNTI0MzIwYmNmNzM4MDVjOTQ0NGUyYyIsImlhdCI6MTczODM1OTIxMiwiZXhwIjoyMDUzNzE5MjEyfQ.kEAU6kHDXq9QriRYBDeFRpC_t2xPO4veH3Y3jF_tHII"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

