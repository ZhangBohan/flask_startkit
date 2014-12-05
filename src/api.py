import requests

API_URL_BASE = 'http://guides.appchina.com/guide/'


def get_app(package_name):
    return _get_json_from_api('%spackageNames/%s' % (API_URL_BASE, package_name))


def _get_json_from_api(url):
    r = requests.get(url=url)
    if r.status_code == 200:
        return r.json()
    else:
        pass

if __name__ == '__main__':
    print get_app('sh.lilith.dgame.yyh')