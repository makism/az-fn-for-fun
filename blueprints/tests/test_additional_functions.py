import azure.functions as func

from additional_functions import fn_ping


def test_fn_ping():
    # Construct a mock HTTP request.
    req = func.HttpRequest(
        method="GET",
        body=None,
        url="/api/fn_ping",
        # params={"value": "21"},
    )
    func_call = fn_ping.build().get_user_function()
    resp = func_call(req)

    # self.assertEqual(
    # resp.get_body(),
    # "pong",
    # b"21 * 2 = 42",
    # )
