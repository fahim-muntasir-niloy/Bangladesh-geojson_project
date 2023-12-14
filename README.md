<img src= https://raw.githubusercontent.com/fahim-muntasir-niloy/Bangladesh-geojson_project/main/Divisions%20in%20Bangladesh.png>

# About the project

Geo json files contain the lat-long informations about any place, so that it can be mapped. Every country has their unique geo json, that can be used for visualizations. However, for `Bangladesh`, the updated geojson file along with example was not available. This repo is aimed to solve this issue. 


## Download Original Shape File
Shape files in SHP format: [[Bangladesh - Subnational Administrative Boundaries]](https://data.humdata.org/dataset/administrative-boundaries-of-bangladesh-as-of-2015) (Original Source)<br>
From there, download the file: **bgd_adm_bbs_20201113_SHP.zip (186.6M)**

Extract and save the 64 files in a folder.

## Converting Shape Files

1. adm = Administration Regions
2. adm0 = Entire Bangladesh
3. adm1 = 8 Divisions
4. adm2 = 64 Districts/Zilas
5. adm3 = 492 Upazilas
6. adm4 = 5160 Thanas/Unions

The folder `Geo Json Maps` contains the geo json files of 2,3 and 4. You can do for the rest if needed.

```python
import shapeTojson
from osgeo import ogr


shapeTojson.shp2json('Shape_files/path_to_shp_file.shp')
```
Source of converter function: [Yash Sanghvi](https://medium.com/tech-carnot/interactive-map-based-visualization-using-plotly-44e8ad419b97) <br>

Installing Osgeo to import ogr: [Open Source Geo Spatial Foundation](https://gdal.org/download.html#windows)




## Working with Geo Json File
- All the instructions given in the `bd map.ipynb` file.

- A friendly  [tutorial](https://www.youtube.com/watch?v=aJmaw3QKMvk) on choropleth map using plotly can be found here.



## If this repo helps you, consider giving it a star. Thanks ❤️

### Acknowledgments

The repo from [Yasser Aziz](https://github.com/yasserius/bangladesh_geojson_shapefile/blob/main/README.md) inspired this work.