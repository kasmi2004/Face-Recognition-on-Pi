from webexteamssdk import WebexTeamsAPI

def alert_teams():

    teams_token = "NTdkMTJlMjUtZjg1ZC00ZWZmLWEwNGYtZjgyNjRmYzk3YzUyMzI5M2Y1ZDQtYzMx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
    #bot_url = "http://127.0.0.1:4040"

    api = WebexTeamsAPI(access_token = teams_token)

    message = api.messages.create(toPersonEmail="elisejlandman@hotmail.com",
               text="test", markdown=None, files=["alert.png"], attachments=None)
