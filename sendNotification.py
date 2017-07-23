import requests, os
#curl -sS -H 'Content-type: application/json' -H "Authorization: Bearer $HIPCHAT_TOKEN" -d @message.json $HIPCHAT_URL/v2/room/$HIPCHAT_ROOM_ID/notification

#Issue with encoding. Does not work unless url is entered as a string.

def main():
	hipchat_token=os.environ['HIPCHAT_TOKEN']
	hipchat_room_id=os.environ['HIPCHAT_ROOM_ID']
	uri=os.environ['HIPCHAT_URI']
	#post_data = {'room_id':'<HIPCHAT_ROOM_ID>', 'from':'Aditya', 'message': 'Sending test message from python code', 'auth_token': '<HIPCHAT_TOKEN>'}
	post_data = "{'room_id': '" + hipchat_room_id + "', 'from':'Aditya', 'message': 'Sending test message from python code', 'auth_token': '" + hipchat_token + "'}"
	print(post_data)
	print(uri)
	#requests.post(url='https://api.hipchat.com/v2/room/<HIPCHAT_ROOM_ID>/notification', data=post_data)
	print(requests.post(uri, post_data, headers={'Content-Type': 'application/json'}))

main()
