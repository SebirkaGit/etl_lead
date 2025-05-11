def transform(data):
    #Convert height which is in inches to millimeter
    #Conver inches to merters and round off to two decimals (one inch is 0.0254 meters)
    data['height'] = round(data.height * 0.0254,2)

    #Convert pounds to kilograms and round off to two decimals( one pound in 0.45359237 kilograms)
    data['weight'] = round(data.weight * 0.45359237,2)
    return data