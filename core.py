import requests, json
group_id = 'ид группы'
token = 'токен'
lpb = requests.post('https://api.vk.com/method/groups.getLongPollServer',data={'access_token':token,'v':'5.85','group_id':group_id}).text
lpb = json.loads(lpb)['response']
ts = lpb['ts']
while True:
    try:
        response = requests.post(lpb['server']+'?act=a_check&key='+lpb['key']+'&ts='+str(ts)+'&wait=25').text
        response = json.loads(response)
        for result in response['updates']:
            ts = response['ts']
            text = result['object']['text']
            print(text)
    except KeyError:
        lpb = requests.post('https://api.vk.com/method/groups.getLongPollServer',data={'access_token':token,'v':'5.85','group_id':group_id}).text
        lpb = json.loads(lpb)['response']
        ts = lpb['ts']
        continue
