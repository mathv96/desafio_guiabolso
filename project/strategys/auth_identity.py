def identity(self, payload):
    user_id = payload['identidade']
    return {"user_id": user_id}