import requests

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjNiYjg3ZGNhM2JjYjY5ZDcyYjZjYmExYjU5YjMzY2M1MjI5N2NhOGQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZmFzdGFwaS1hdXRoLTQ3ZGQ1IiwiYXVkIjoiZmFzdGFwaS1hdXRoLTQ3ZGQ1IiwiYXV0aF90aW1lIjoxNzA5NjI0NTYyLCJ1c2VyX2lkIjoieVl5NFdVZk02S2E2VmFlbGFWWVljcFFiSUg0MiIsInN1YiI6InlZeTRXVWZNNkthNlZhZWxhVllZY3BRYklINDIiLCJpYXQiOjE3MDk2MjQ1NjIsImV4cCI6MTcwOTYyODE2MiwiZW1haWwiOiJ5ZW51bGljaGFtb2R5YUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsieWVudWxpY2hhbW9keWFAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.FlEs7w8Ou0iEUtIcs3Y8tXJFUGAA1esEc3N51b6mC3FFRqL4Fduthe4fwpXenNoHgY1UwEkmj__d0gYOW1cO10WwA72M3fBmRlusIbaB1mtTaRd1okX5HfxAETgTjrDhEVyVsFjjNTlvXfmKpEd-dcvjkAwAijZFP07DdluT6GK9jThLDgjFZNqLzw56Vo7XQ34bfTF-jnsvUjDOC-nlvLEfPgDXpif1eag2F3f4DEiqzW035zVNx0IKWTRb4naZ-LPm4VjiGjNHdrt1BFytJhBrdq2SrvgPgfveVUz8q1UUYCO0GSbRnm3LxEjF1Q7D_PUil7FF2XYpdbyhgcLPPQ"

def test_validate_endpoints():
    headers = {
        'authorization': token
    }
    
    response = requests.post(
        "http://127.0.0.1:8000/ping",
        headers=headers
    )
    
    return response.text

print(test_validate_endpoints())

{"iss":"https://securetoken.google.com/fastapi-auth-47dd5",
 "aud":"fastapi-auth-47dd5","auth_time":1709624562,
 "user_id":"yYy4WUfM6Ka6VaelaVYYcpQbIH42",
 "sub":"yYy4WUfM6Ka6VaelaVYYcpQbIH42",
 "iat":1709624562,
 "exp":1709628162,
 "email":"yenulichamodya@gmail.com",
 "email_verified":false,
  "firebase":{"identities":{"email":["yenulichamodya@gmail.com"]},"sign_in_provider":"password"},
 "uid":"yYy4WUfM6Ka6VaelaVYYcpQbIH42"}

