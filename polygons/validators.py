class Polygons:
    @staticmethod
    def polygons_point_validator(request):
        check_list = ["lat", "lon"]
        errors = {}
        data = request.data
        for field in check_list:
            try:
                if field not in data:
                    errors[field] = ["This field is required."]
                    continue
                float(data[field])

            except Exception as e:
                errors[field] = ["This field must be float or number."]

        if errors == {}:
            return True

        return errors

    @staticmethod
    def polygon_field_validator(polygon):
        try:
            if polygon.get("type") != "Polygon":
                return False
            if not isinstance(polygon.get("coordinates"), list) or not isinstance(polygon.get("coordinates")[0], list):
                return False

            for coordinate in polygon.get("coordinates")[0]:
                if len(coordinate) != 2:
                    return False
                lat, lon = coordinate
                float(lat), float(lon)

        except:
            return False