import CA01.prod.StarCatalog as StarCatalog

stars = StarCatalog.StarCatalog()

starCount = stars.loadCatalog(starFile="SaoChart.txt")
print starCount
#starsDeleted = stars.emptyCatalog()
#print starsDeleted
noOfStarsNow = stars.getCurrentCount()
print noOfStarsNow
print stars.getStar(10954)