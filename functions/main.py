# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app, firestore
import numpy as np

initialize_app()

REGION = "australia-southeast1"

@https_fn.on_request(region=REGION)
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    x = np.random.randn(10,10)
    return https_fn.Response(np.array2string(x))

@https_fn.on_request(region=REGION)
def add_todo(req: https_fn.Request) -> https_fn.Response:
    # client = firestore.client()
    # todos = client.collection("todos")
    # for i in range(10):
    #     new_doc = todos.document()
    #     new_doc.set({"testing123": "testing123_" + str(i), "i": i})
    return(https_fn.Response("Done"))