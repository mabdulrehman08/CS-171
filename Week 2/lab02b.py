import math

def yarnRequired(skeinWeight, swatchLength, swatchWidth, swatchWeight, projectLength, projectWidth):
    # Calculate the area of the swatch and the project
    swatchArea = swatchLength * swatchWidth
    projectArea = projectLength * projectWidth

    # Determine the weight of yarn required for the project
    yarnPerUnitArea = swatchWeight / swatchArea
    projectWeight = yarnPerUnitArea * projectArea

    # Add a 10% safety margin
    yarnMarginSafetyFactor = 1.10
    totalYarnWeight = projectWeight * yarnMarginSafetyFactor

    # Calculate the number of skeins needed and round up
    skeinsNeeded = math.ceil(totalYarnWeight / skeinWeight)
    
    return skeinsNeeded

# Example usage
print(yarnRequired(170, 10, 10, 4, 150, 125))  # Output: 5
