import pytest
from src_0188 import task_func

def test_task_func():
    # Test that the function raises a ValueError when the dictionary is missing 'Lon' or 'Lat' keys
    with pytest.raises(ValueError):
        task_func({'Lat': (-90, 90)})

    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180)})

    # Test that the function raises a ValueError when the dictionary values are not tuples
    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180), 'Lat': (-90, 90, 0)})

    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180), 'Lat': (-90, 90, 0)})

    # Test that the function returns a GeoDataFrame with the correct columns and data types
    gdf = task_func({'Lon': (-180, 180), 'Lat': (-90, 90)})
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert gdf.columns.tolist() == ['City', 'Coordinates']
    assert gdf['City'].dtype == object
    assert gdf['Coordinates'].dtype == object

    # Test that the function returns a GeoDataFrame with the correct number of rows
    assert len(gdf) == len(cities)

    # Test that the function returns a GeoDataFrame with the correct coordinates
    for i in range(len(gdf)):
        assert isinstance(gdf.iloc[i]['Coordinates'], Point)
        assert gdf.iloc[i]['Coordinates'].x >= lon_min and gdf.iloc[i]['Coordinates'].x <= lon_max
        assert gdf.iloc[i]['Coordinates'].y >= lat_min and gdf.iloc[i]['Coordinates'].y <= lat_max