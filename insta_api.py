import requests


def get_user_info(username):
    data = f'signed_body=SIGNATURE.{{"q":"{username}","skip_recovery":"1"}}'
    headers = {
        "Accept-Language": "en-US",
        "User-Agent": "Instagram 353.2.0.49.90",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-IG-App-ID": "124024574287414",
        "Accept-Encoding": "gzip, deflate",
        "Host": "i.instagram.com",
        "Connection": "keep-alive",
        "Content-Length": str(len(data)),
    }
    try:
        response = requests.post(
            "https://i.instagram.com/api/v1/users/lookup/", data=data, headers=headers
        )
        res_data = response.json()
        return res_data
    except:
        return None
