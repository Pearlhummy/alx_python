"""documentation module"""
import requests as r
import sys as s


if __name__ == "__main__":
    email = s.argv[2]
    response = r.post(s.argv[1], {"email": email})
    content = response.content.decode()
    print(content)