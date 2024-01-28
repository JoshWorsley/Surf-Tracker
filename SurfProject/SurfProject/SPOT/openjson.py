import json

def get_closest_city(surf_spots, surf_spot_name):
    for spot in surf_spots["surf_spots"]:
        if spot["name"] == surf_spot_name:
            return spot["closest_city"]
    return None


# with open('SurfProject\SurfProject\SPOT\SurfSpotList.json', 'r') as file:
#     data = json.load(file)
#     print(get_closest_city(data,"Sumner"))


