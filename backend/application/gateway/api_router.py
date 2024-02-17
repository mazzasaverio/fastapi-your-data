from fastapi import Request


def call_api_gateway(request: Request):
    portal_id = request.path_params["portal_id"]
    print(request.path_params)
    if portal_id == str(1):
        raise RedirectSubApp1PortalException()


class RedirectSubApp1PortalException(Exception):
    pass
