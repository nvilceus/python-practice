from urllib.request import urlopen
import json, time

while True:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    
    # key_iterable = data.keys() # Gets the keys from the data dictionary
    # key_list = list(key_iterable)
    # print(f'{key_list} \n')
    # for k, v in data.items():
    #     print(f'{k} \n {v} \n')
    
    current_price = data['bpi']['USD']['rate']
    float_current_price = float(current_price.replace(',', ''))
    edit_str_current_price = current_price[:-2]
    
    local_time = time.localtime()
    current_time = time.strftime('on %B %d, %Y at %I:%M:%S %p', local_time)
    sync_val = current_time[-4]
    
    print('The current price of one Bitcoin {t} is ${r}'.format(t = current_time , r = edit_str_current_price))
    if float_current_price >= 53000: # Breaks out of while loop if Bitcoin price is less than $53,000
        print('You have met your price target!')
        break
    
    while int(sync_val) != 0: # Syncs the time so the delay does not infinitely increase with infinite operational time
        sync_time = time.localtime()
        sync_val = time.strftime('on %B %d, %Y at %I:%M:%S %p', sync_time)[-4]
        if sync_val == 0:
            continue
    
    time.sleep(60)