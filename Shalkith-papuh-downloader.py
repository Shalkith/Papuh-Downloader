# Quick and dirty script for those nostalgic guys!

import urllib.request, json 
import os,wget
thewalls=[

'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/aicp_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/brokenos_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/du_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/eos_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/fav_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/liquidsmooth_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/omni_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/original_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/pacrom_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/slim_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/solid_wallpapers.json',
'https://raw.githubusercontent.com/Shalkith/Papuh-Resources/master/validus_wallpapers.json'
]



for papuh in thewalls:
    with urllib.request.urlopen(papuh) as url:
        data = json.loads(url.read().decode())
        #print(data)
    for walls in data:
            walls = walls
    for wp in data[walls]:
        try:
            os.makedirs(walls, exist_ok=False)
        except:
            pass
        try:
            
            wget.download(wp['url'],out=walls+'/'+wp['name'].replace(' ',"_").lower()+wp['url'][-4:])
        except:
            print("Couldn't get",walls+'/'+wp['name'].replace(' ',"_").lower()+wp['url'][-4:])
            print()


        
