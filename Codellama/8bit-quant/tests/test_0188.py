import pytest
from src_0188 import task_func


def test_task_func():
    # Test that the function raises a ValueError when the dictionary does not contain 'Lon' and 'Lat' keys
    with pytest.raises(ValueError):
        task_func({'foo': (1, 2), 'bar': (3, 4)})

    # Test that the function raises a ValueError when the 'Lon' and 'Lat' values are not tuples
    with pytest.raises(ValueError):
        task_func({'Lon': 1, 'Lat': 2})

    # Test that the function returns a GeoDataFrame with the correct columns and data types
    gdf = task_func({'Lon': (-180, 180), 'Lat': (-90, 90)})
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert set(gdf.columns) == {'City', 'Coordinates'}
    assert gdf['City'].dtype == object
    assert gdf['Coordinates'].dtype == object

    # Test that the function returns a GeoDataFrame with the correct number of rows
    assert len(gdf) == 5

    # Test that the function returns a GeoDataFrame with the correct coordinates
    assert gdf['Coordinates'].apply(lambda x: isinstance(x, Point)).all()
    assert gdf['Coordinates'].apply(lambda x: x.x >= -180 and x.x <= 180).all()
    assert gdf['Coordinates'].apply(lambda x: x.y >= -90 and x.y <= 90).all()