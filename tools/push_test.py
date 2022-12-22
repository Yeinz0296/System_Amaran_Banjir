import requests
import json

def pushbullet_noti(title, body):
 
    TOKEN = 'o.1ZYve8KhesOcxpjVFiaK9tHq9G3QjGxq'  # Pass your Access Token here
    # Make a dictionary that includes, title and body
    msg = {"type": "note", "title": title, "body": body}
    # Sent a posts request
    resp = requests.post('https://api.pushbullet.com/v2/pushes',
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:  # Check if fort message send with the help of status code
        raise Exception('Error', resp.status_code)
    else:
        print('Message sent')
 
 
pushbullet_noti("Hey", "How you doing?")