# calculateRiskPeriod


## Micro Service Description
Service that runs an algorithm to measure each reunion's "risk period" based on the COVID incubation period.

## Functional Requirements
- The day 0 of possible infection will be the day the reunion is created
- An initial risk % (initialRisk) is calculated as soon as the reunion is created based on the following metrics and weighting their inputs:
  * Algorithm should take into account number of people in the reunion
  * Algorithm should take into account how many time was the reunion
  * Algorithm should take into account if people were waring mask
  * Algorithm should take into account whether or not as an open space
  * Algorithm should take into account the two week span of transmission
- The initial risk will be classified on quarters in a semaphore scale:
  * Green: 0-25%
  * Yellow: 25-50%
  * Orange: 50-75%
  * Red: 75-100%
- A second partial risk (daysFromReunion) will be calculated depending on the days from the reunion:
  * Red: 1-4 days
  * Orange: 4-7 days
  * Yellow: 7-11 days
  * Green: 11-14 days
- An initial risk % (initialRisk) is calculated as soon as the reunion is created based on the following metrics and weighting their inputs:
- 
-  Red - really contagious: someone from the reunion tested possitive or is showing symptomps up to seven days after the reunion. 
-  Orange - not sure if contagiuous: it has passed less than a week since the reunion AND no one has shown symptoms nor tested postive
-  Yellow - mildly contagious: 
- Green
- It updates every day if no new update is made, e.g. any of the reunion's participant got the virus.

- Algorithm should take into account the two week span of transmission

## Non Functional Requirements
- The risk of reunion is presented easily and visually on the UI
- 

## Deployment URL


