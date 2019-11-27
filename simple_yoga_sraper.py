import requests
import json
import urllib.request
import os

from shutil import copyfile
all_poses=[]
# for i in range(1,11):
#     page = requests.get("https://api.pocketyoga.com/poses?page="+str(i))
#     content=json.loads(page.content.decode('utf-8'))
#     for pose in content['poses']:
#         all_poses.append(pose["base_name"])


#print(all_poses)
# for pose in all_poses:
#     pose_page=requests.get('https://api.pocketyoga.com/poses/base/'+str(pose))
#     pose_content=json.loads(pose_page.content.decode('utf-8'))
#     description=pose_content['description'] #description needs to be written to a file
#     #directory needs to be changed
#     urllib.request.urlretrieve("https://pocketyoga.com/assets/images/poses/"+pose+".png", "/home/dhirensr/test.png")
pose_not_there=[]
pose_to_be_figured_out=[]
poses_exactly_match=[]
pwd=os.getcwd()
for fname in os.listdir(pwd+'/asana_gt/'):
    pose_name=fname.split(".")[0]
    pose_page=requests.get('https://api.pocketyoga.com/poses?search='+pose_name)
    pose_content=json.loads(pose_page.content.decode('utf-8'))
    if ('poses' not in pose_content.keys()) or (pose_content['poses']==[]):
        pose_not_there.append(fname)
    elif (len(pose_content['poses']))>1:
        pose_to_be_figured_out.append(fname)
    else:
        pocket_yoga_pose_name=pose_content['poses'][0]['base_name']
        pose_inner_page=requests.get('https://api.pocketyoga.com/poses/base/'+pocket_yoga_pose_name)
        pose_page_content=json.loads(pose_inner_page.content.decode('utf-8'))
        poses_exactly_match.append(pocket_yoga_pose_name)
        #pose_inner_page=requests.get('https://api.pocketyoga.com/poses/base/'+pocket_yoga_pose_name)
        #pose_page_content=json.loads(pose_inner_page.content.decode('utf-8'))
        #print(pose_page_content['description'])
        print(fname,pocket_yoga_pose_name)
        copyfile(pwd+'/asana_gt/'+fname, pwd+'/img/'+fname)
        with open(pwd+'/txt/'+pose_name+".txt",'w') as f:
            f.write(pose_page_content['description'])
