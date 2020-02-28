# scientific kit
import argparse

def wind_chill(degreesF: int, windVelocityMph: int) -> float:
    """Caluclate windchill factor.
    Currently supports Farenheit.
    TODO: Add Celcius suport:
    13.12 + (0.6215 * degreesC) - (11.37 * (windVelocityMph ** 0.16)) + 0.3965 * degreesC * (windVelocityMph ** 0.16)
    if not degreesC > -273.15:
        raise ValueError('Degrees Celcius cannot be less than absoulte zero, 273.15 degrees Celcius.')
    
    Arguments:
        degreesF {int} -- Degrees Farenheit
        windVelocityMph {int} -- Wind velocity in Mph.
    
    Raises:
        ValueError: 'Degrees Farenheit cannot be less than absoulte zero, -273.15 degrees Farenheit.'
        ValueError: 'Windchill velocity in Mph cannot be less than or equal to 0.'
    
    Returns:
        float -- Windchill factor.
    """

    if not degreesF > -459.67:
        raise ValueError('Degrees Farenheit cannot be less than absoulte zero, -459.67 degrees Farenheit.')

    if not windVelocityMph > 0:
        raise ValueError('Windchill velocity in Mph cannot be less than or equal to 0.')

    return 35.74 + (0.6215 * degreesF) - (35.75 * (windVelocityMph ** 0.16)) + 0.4275 * degreesF * (windVelocityMph ** 0.16)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--degrees', action='store')
    parser.add_argument('-w', '--windchill', action='store')
    args = parser.parse_args()

    result = wind_chill(int(args.degrees), int(args.windchill))
    print(result)
