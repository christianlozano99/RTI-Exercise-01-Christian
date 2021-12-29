#SQLite commands to export tables
#open sqlite file
.open exercise01.sqlite

#set header to on to keep lables
.header on

# set to CSV output
.mode csv

# output to file called extractedData
.output extractedData.csv

# we need to replace the following
# workclass_id, education_level_id, maritial_status_id, occupation_id, relationship_id, race_id
# sex_id, country_id

SELECT records.id,
records.age, 
records.education_num,
records.capital_gain, 
records.capital_loss, 
records.hours_week,
records.over_50k,
workclasses.name,
education_levels.name,
marital_statuses.name,
occupations.name,
relationships.name,
races.name,
sexes.name,
countries.name

FROM records

LEFT OUTER JOIN workclasses
ON  records.workclass_id =workclasses.id

LEFT OUTER JOIN education_levels
ON  records.education_level_id = education_levels.id

LEFT OUTER JOIN marital_statuses
ON  records.marital_status_id = marital_statuses.id

LEFT OUTER JOIN occupations
ON  records.occupation_id = occupations.id

LEFT OUTER JOIN relationships
ON  records.relationship_id = relationships.id

LEFT OUTER JOIN races
ON  records.race_id = races.id

LEFT OUTER JOIN sexes
ON  records.sex_id = sexes.id

LEFT OUTER JOIN countries
ON  records.country_id = countries.id
;