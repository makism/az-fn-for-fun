import logging

import azure.functions as func

bp = func.Blueprint()


@bp.route(route="ping")
def fn_ping(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    return func.HttpResponse("pong", status_code=200)


@bp.queue_output(arg_name="msg", queue_name="messages", connection="AzuriteConnection")
@bp.route(route="record")
def fn_write_to_queue(req: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:
    message = req.params.get("msg")
    msg.set(message)
    return func.HttpResponse("Message sent", status_code=200)


@bp.blob_trigger(
    arg_name="obj",
    path=f"main/incoming/{{name}}.csv",
    connection="AzuriteConnection",
)
def fn_blob_listener(obj: func.InputStream):
    logging.info(f"Blob listener triggered by: {obj.name}")
