import os, requests


def login(request):
    #email = request.form.get('email')
    #password = request.form.get('password')
    #if not email or not password:
    #    return None, ("missing credentials", 401)
    auth = request.authorization
    if not auth:
        return None, ("missing authorization", 401)
    
    basicAuth = (auth.username, auth.password)

    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS', '127.0.0.1:5000')}/login", 
        auth=basicAuth
    )

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)