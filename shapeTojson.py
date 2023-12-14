# Python >= 3.7
from osgeo import ogr
import json

def shp2json(shp_path:str):
  """
  Description -- Convert SHP files to GeoJSON with OGR.
  Author -- Yash Sanghvi
  
  shap_path -- Exact file location from the shape files.
  return -- Outputs JSON file to same directory as the SHP files.
  """
  driver = ogr.GetDriverByName('ESRI Shapefile')
  data_source = driver.Open(shp_path, 0)

  fc = {
      'type': 'FeatureCollection',
      'features': []
      }

  lyr = data_source.GetLayer(0)
  for feature in lyr:    
      fc['features'].append(feature.ExportToJson(as_object=True))

  output_name = shp_path.split(".")[0] + ".json"

  with open(output_name, 'w') as f:
      json.dump(fc, f)
      print("GeoJSON file created: {}".format(output_name))