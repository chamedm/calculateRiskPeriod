# calculateRiskPeriod


## Micro Service Description
Service that runs an algorithm to measure each reunion's "risk period" based on the COVID incubation period.

## Functional Requirements
- The day 0 of possible infection will be the day the reunion is created
- An initial risk % (initialRiskFactor) is calculated as soon as the reunion is created based on the following metrics and weighting their inputs:
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
- The status should update each day according to the above metrics
- It should calculate a high risk (red) if a participant of the reunion gets infected and logs it on the app
- Algorithm should take into account the two week span of transmission
- Algorithm stops calculating after two weeks of the reunion

## Non Functional Requirements
- The risk of reunion is presented easily and visually on the UI
- The algorithm gets the input if any infection is reported
- The algorithm should run automatically on a new day
- All information about the reunion should be provided

## Deployment URL


