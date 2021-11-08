import folium

name = "京王ストア"
latlon_list = [
    ['35.700706', '139.734699'], ['35.706673', '139.687289'], ['35.735761', '139.629504'], 
    ['35.669846', '139.616025'], ['35.676131', '139.643217'], ['35.683546', '139.614132'], 
    #['0', '0'], 
    ['35.668922', '139.6502'], ['35.667562', '139.6319'], ['35.626984', '139.587695'], 
    ['35.662286', '139.584943'], ['35.658208', '139.575502'], ['35.653598', '139.530921'], 
    ['35.70276', '139.580072'], ['35.684488', '139.544946'], ['35.633683', '139.531071'], 
    ['35.619461', '139.473314'], ['35.593935', '139.345621']
]
map = folium.Map(location=['35.700706', '139.734699'], zoom_start=12)

for latlon in latlon_list:
    folium.Marker(location=latlon, popup=name).add_to(map)
    
map.save("map_keiostore.html")