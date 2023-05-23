# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
import numpy as np
import pandas as pd

initialize_app()


@https_fn.on_request(region="australia-southeast1")
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    x = np.random.randn(10,10)
    return https_fn.Response(np.array2string(x))