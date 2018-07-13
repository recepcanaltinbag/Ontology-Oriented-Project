import shapefile
from owlready2 import *

sf = shapefile.Reader("/Users/recep/Desktop/ontology/Ergene_OlcumNoktalari_wIDs/Ergene_OlcumNoktalari_wIDs.shp")



shapes = sf.shapes()
fields = sf.fields

records = sf.records()


shapeRecs = sf.shapeRecords()

print(fields)


print(records[0])
print(records[0][0])
print(records[0][1])
print(records[0][2])
print(records[0][3])


onto = get_ontology("http://web.itu.edu.tr/altinbagr/ontology/TheOntologyGISDSS.owl")   #online updated version
#onto = get_ontology("file:///Users/recep/Desktop/ontology-master/ProjectOwl_v4.owl")
onto.load()

my_obs = []

for element in range (0,len(records)):
    my_obs.append(onto.Observation(records[element][0]))



my_measurement37 = onto.Measurement("Msr_37")

my_obs37 = onto.Observation("Obs_37")
my_obs37.latitude.append('36.45')
my_obs37.measure.append(my_measurement37)

ObservationInd = list(onto.search(type = onto.Observation))

print(ObservationInd, my_obs37.measure, my_obs37.latitude)


#print(shapeRecs[0].record[1])    Another way to read lines





