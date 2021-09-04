# Polygons API
## Create Polygon
### Request
``` POST /polygons/```
```
{
    "name": "Alireza Shabano",
    "price": "90.00",
    "polygon": "{'type': 'Polygon', 'coordinates': [[[-48.25, 23.61], [-10.59, 48.96], [-36.99, 29.17], [-98.73, 18.87]]]}",
    "provider": "<Provider_Name>"
}
```

### Response
```
{
    "id": 1,
    "name": "Alireza Shabano",
    "price": "90.00",
    "polygon": "{'type': 'Polygon', 'coordinates': [[[-48.25, 23.61], [-10.59, 48.96], [-36.99, 29.17], [-98.73, 18.87]]]}",
    "provider": "<Provider_Name>"
}
```

## Delete Polygon
### Request
``` DELETE /polygons/id```
### Response
```
HTTP/1.1 204 0
```

## Update Polygon
### Request
``` PUT /polygons/id```
```
{
    "name": "Alireza Shabani 2",
    "price": "10.00",
    "polygon": "{'type': 'Polygon', 'coordinates': [[[-48.25, 23.61], [-10.59, 48.96], [-36.99, 29.17], [-98.73, 18.87]]]}",
    "provider": "<Provider_Name>"
}
```

### Response
```
{
    "id": 1,
    "name": "Alireza Shabani 2",
    "price": "10.00",
    "polygon": "{'type': 'Polygon', 'coordinates': [[[-48.25, 23.61], [-10.59, 48.96], [-36.99, 29.17], [-98.73, 18.87]]]}",
    "provider": "<Provider_Name>"
}
```

## Update Polygon Partially
### Request
``` PATCH /polygons/id```
```
{
    "name": "Alireza Shabani 3",
}
```

### Response
```
{
    "id": 1,
    "name": "Alireza Shabani 3",
    "price": "10.00",
    "polygon": "{'type': 'Polygon', 'coordinates': [[[-48.25, 23.61], [-10.59, 48.96], [-36.99, 29.17], [-98.73, 18.87]]]}",
    "provider": "<Provider_Name>"
}
```
## View Specific Polygon
### Request
``` GET /polygons/id```

### Response
```
{
    "id": 1,
    "name": "Alireza Shabani 3",
    "price": "10.00",
    "polygon": "{'type': 'Polygon', 'coordinates': [[[-48.25, 23.61], [-10.59, 48.96], [-36.99, 29.17], [-98.73, 18.87]]]}",
    "provider": "<Provider_Name>"
}
```

## Get list of Polygons
### Request
``` GET /polygons/```

### Response
```
{
    "id": 1,
    "name": "Alireza Shabani 3",
    "price": "10.00",
    "polygon": "{'type': 'Polygon', 'coordinates': [[[-48.25, 23.61], [-10.59, 48.96], [-36.99, 29.17], [-98.73, 18.87]]]}",
    "provider": "<Provider_Name>"
},
{
    "id": 1,
    "name": "Alireza Shabani 4",
    "price": "25.00",
    "polygon": "{'type': 'Polygon', 'coordinates': [[[-98.25, 23.61], [-57.99, 48.96], [-30.19, 94.17], [-98.73, 28.87]]]}",
    "provider": "<Provider_Name>"
}
```
## Get Polygons from Point
### Request
``` POST /polygon-point/```
```
{
    "lat": -98.25,
    "lon": 23.61
}
```

### Response
```
[
    {
        "name": "Alireza Shabani 4",
        "price": "25.00",
        "provider_id": 2
    }
]
```