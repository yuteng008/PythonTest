import requests

def download(url):
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    if req.status_code == 403:
        print("403")
        return
    filename = url.split('/')[-1]
    with open(filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("download over.")

if __name__ == '__main__':
    url = input("Enter a url:")
    download(url)
