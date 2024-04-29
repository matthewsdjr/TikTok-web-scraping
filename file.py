from tikapi import TikAPI, ValidationException, ResponseException
import json

api = TikAPI("D0VMJRFqIi5dr5HWMeWmo7nYGxSWCNGa4bEfcOgxzGKDiwnr")
response = api.public.hashtag(
        name="inmuebles"
    )

hashtagId = response.json()
print(hashtagId)