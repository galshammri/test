import pandas as pd
import folium
import requests

url = 'https://ibm.box.com/shared/static/nmcltjmocdi8sd5tk93uembzdec8zyaq.csv'
DF_SFC = pd.read_csv(url)

# group by neighborhood
DF_D = DF_SFC.PdDistrict.value_counts()

#DF_D = DF_SFC['PdDistrict'].value_counts()
DF_D1 = pd.DataFrame(data = DF_D.values, index = DF_D.index, columns = ['Count'])
DF_D1 = DF_D1.reindex(["CENTRAL", "NORTHERN", "PARK", "SOUTHERN", "MISSION", "TENDERLOIN", "RICHMOND", "TARAVAL", "INGLESIDE", "BAYVIEW"])

DF_D1 = DF_D1.reset_index()
DF_D1.rename({'index': 'Neighborhood'}, axis = 'columns', inplace = True)
print(DF_D1)

geojson = r'https://cocl.us/sanfran_geojson'

SF_Map = folium.Map(location = [37.77, -122.42], zoom_start = 13)

SF_Map.choropleth(
       geo_data = geojson,
       data = DF_D1,
       columns = ['Neighborhood','Count'],
       key_on = 'feature.properties.DISTRICT',
       fill_color = 'YlOrRd',
       fill_opacity = '0.7',
       line_opacity = '0.2',
       legend_name = 'Crime Rate in San Francisco')

SF_Map