import azure.functions as func
from additional_functions import bp

app = func.FunctionApp()

app.register_functions(bp)
