import CA01.prod.StarCatalog as StarCatalog

# -------------- __init__ -----------------------------
# Instantiate a star catalog
stars = StarCatalog.StarCatalog()


# -------------- loadCatalog -----------------------------
# Load the catalog with a valid file
# The return value will be a count of the number of stars loaded
starCount = stars.loadCatalog(starFile="SaoChart.txt")
print starCount
# Attempts to load the catalog using a non-existent file or 
# a file that does not contain legitimate star information
# should result in a ValueError exception bearing a
# diagnostic message.
try:
    stars.loadCatalog(starFile="aValidStarFile.txt")
except ValueError as e:
    diagnosticString1 = e.args[0]

print diagnosticString1  

# -------------- getStarCount -----------------------------
# Get a count of stars with magnitudes between 2 and 5, inclusive.
starsBetween2And5 = stars.getStarCount(2, 5)
print starsBetween2And5
# Get a count of stars with magnitudes .LE. 5.
starsLE5 = stars.getStarCount(upperMagnitude=5)
print starsLE5
# Get a count of stars with magnitudes .GE. 3
starsGE3 = stars.getStarCount(lowerMagnitude=3)
print starsGE3
# Get a count of all stars
allStars = stars.getStarCount()
print allStars
# Attempt to get a count of stars using an invalid magnitude
try:
    stars.getStarCount('a', 5)
except ValueError as e:
    diagnosticString2 = e.args[0]
print diagnosticString2

# -------------- getMagnitude -----------------------------
# Get the magnitude of the brightest star within a square area that is
# 0.017453 radians by 0.017453 radians (meaning, a 1-degree field of view)
brightestStar = stars.getMagnitude(4.712389, 0.00027227, 0.3)
print brightestStar
# Attempt to determine the brightest star in a field of view
# using an invalid parameter
try:
    stars.getMagnitude(597, 0.9452005, 0.017453)
except ValueError as e:
    diagnosticString3 = e.args[0]
print diagnosticString3

# -------------- emptyCatalog -----------------------------
# empty the catalog
starsDeleted = stars.emptyCatalog()
print starsDeleted