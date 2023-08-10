"""documentation module"""
import requests as r
import sys as s


if __name__ == "__main__":
    response = r.get(s.argv[1])
    print(response.headers.get("X-Request-Id"))