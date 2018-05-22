from urllib.request import urlopen
import urllib
import re
import string
import json

appid = '9Y5PH2-9KAGK9LXWA'


num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 
            5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven',
            12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
            17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
            'Eighty', 'Ninety']


def spell(num):
    if num == 0:
        return 'Zero'
    if num < 20:
        return (num2words[num])
    elif num < 100:
        ray = divmod(num, 10)
        return (num2words2[ray[0]-2]+" "+spell(ray[1]))
    elif num < 1000:
        ray = divmod(num, 100)
        if ray[1] == 0:
            mid = " hundred"
        else:
            mid = " hundred and "
        return(num2words[ray[0]]+mid+spell(ray[1]))


def find(query):
    # import pdb; pdb.set_trace()
    """controls get function to wolfram's APIs"""
    if 'who created you' in query:
        speech_output = "Andrii, Mr. Peter, and Ramon created me."
        return speech_output
    if 'sudo' in query:
        speech_output = "Ooooh, wow! Look at you. Are you trying to be a hacker or something?"
        return speech_output
    if query == '':
        speech_output = "Can you repeat your question?"
        return speech_output
    # print(query)
    arr = query.split(' ')
    # print(arr)

    for item in range(len(arr)):
        try:
            if int(arr[item]):
                arr[item] = spell(int(arr[item]))
        except ValueError:
            continue
        if arr[item] == '+':
            arr[item] = 'plus'
        if arr[item] == '-':
            arr[item] == 'minus'

    query = '+'.join(arr).strip(' ')
    print(query)
                
    url = 'http://api.wolframalpha.com/v1/spoken?i=' + query + '&appid=' + appid
    url1 = 'http://api.wolframalpha.com/v1/result?i=' + query + '&appid=' + appid

    try:
        data = urlopen(url)
    except urllib.error.URLError:
        try:
            data = urlopen(url1)
        except urllib.error.URLError:
            try:
                url2 = 'https://api.wolframalpha.com/v2/query?input=' + query + '&format=plaintext&output=JSON&appid=' + appid
                data = urlopen(url2)
                tree = data.read().decode('utf-8')
                tree = json.loads(tree)
                try:
                    tree = tree['queryresult']['pods'][1]['subpods'][0]['plaintext']
                    if len(tree) > 5:
                        tree = re.sub('[%s]' % re.escape(string.punctuation), '', tree)
                        speech_output = tree
                        return speech_output
                    else:
                        speech_output = 'I have no data'
                    return speech_output

                except KeyError:
                    speech_output = 'Can you repeat your question?'
                    return speech_output
            except urllib.error.URLError:
                speech_output = 'I may be smart but I also have a limits.'
                return speech_output
    tree = data.read().decode('utf-8')
    tree = re.sub('[%s]' % re.escape(string.punctuation), '', tree)
    return tree
