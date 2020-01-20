import requests, json, os

token = ''

params = data={'access_token':token,'v':'5.103'}
group_id = requests.post('https://api.vk.com/method/groups.getById',params).json()['response'][0]['id']

lpb = requests.post('https://api.vk.com/method/groups.getLongPollServer',data={'access_token':token,'v':'5.85','group_id':group_id}).json()['response']
ts = lpb['ts']

def apisay(text,toho):
    param = {'v':'5.80','peer_id':toho,'access_token':token,'message':text}
    requests.post('https://api.vk.com/method/messages.send', data=param)

while True:
    try:
        response = requests.post(lpb['server']+'?act=a_check&key='+lpb['key']+'&ts='+str(ts)+'&wait=25').json()
        ts = response['ts']
    except Exception as error: 
        if error == KeyboardInterrupt: os._exit(0)
        params = {'access_token':token,'v':'5.85','group_id':group_id}
        lpb = requests.post('https://api.vk.com/method/groups.getLongPollServer',data=params,timeout=100).json()['response']
        ts = lpb['ts']
        continue
    
    for updates in response['updates']:
        if updates['type'] == 'message_new':
            updates = updates['object']['message']
            text = updates['text'] #текст сообщения
            peer_id = updates['peer_id'] #откуда сообщение
            userid = updates['from_id'] #ид юзера

            if 'тест' in text:
                apisay('хуест',peer_id)

