import urllib.parse
import requests
import json

url = 'https://api.github.com/orgs/byu-oit/repos'
json_data = requests.get(url).json()

for repodata in json_data:
    reponame = repodata["name"]
#   repo = json.load(repodata)
#   print(repodata)
    print(reponame)
    url2 = "https://api.github.com/repos/byu-oit/" + reponame + "/contents"
    json2_data = requests.get(url2).json()
    for assetdata in json2_data:
#        print(assetdata)
        asset_path = assetdata["path"]
#        asset_download_url = assetdata["dowload_url"]
        if asset_path == '.repo-meta.yml':
            print("Asset Path:" + asset_path)
            url3 = "https://api.github.com/repos/byu-oit/" + reponame + "/contents/" + asset_path
            json3_data = requests.get(url3).json()
#            for filedata in json3_data:
#                print(filedata)



"""
for repo in data:
    print('repo')

print('data')

for json_repo in data['name']:
    print('json_repo')
"""

#https://api.github.com/repos/byu-oit/byu-ws-cli-python/contents
#API for All Files in repository use to get paths
#

#https://api.github.com/repos/byu-oit/byu-ws-cli-python/contents/@path
#API content of a specific file
#
