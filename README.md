# calculateRiskPeriod


## Micro Service Description
Service that runs an algorithm to measure each reunion's "risk period" based on the COVID incubation period.

## Functional Requirements
- This algorithm will update the risk period based on the days the reunion was created:
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
https://us-south.functions.appdomain.cloud/api/v1/web/is708177%40iteso.mx_dev/ProyectoFinal/calculateRiskPeriod

Example of body expected on GET
{
  "registeredDate": "22/04/11",
  "users": ["mariana@mail.com", "caro@mail.com", "dario@mail.com" ],
  "duration": 30,
  "masks": true,
  "openSpace": true,
  "risk": 2
}

