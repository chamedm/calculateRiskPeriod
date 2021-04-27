from datetime import datetime

def main(reunion):
  factorFromDays = 0
  compoundRisk = 0
  currentDate = datetime.today()
  delta = ((reunion.registeredDate-currentDate).days) * -1
  if (delta < 14):
    factorFromDays = getRiskFactorFromDays(delta)
  else:
    factorFromDays = 1
  print("risk: " + str(reunion.risk))
  print("delta: " + str(delta))
  print("factor from days: " + str(factorFromDays))
  compoundRisk = getCompoundRisk(reunion.risk, factorFromDays)
  print("compound risk: " + str(compoundRisk))
  return compoundRisk

def getRiskFactorFromDays(dayFromReunion):
  factor = 0
  if(dayFromReunion >= 1 <=4):
    factor = 4
  elif(dayFromReunion > 4 and dayFromReunion <=7):
    factor = 3
  elif(dayFromReunion > 7 and dayFromReunion <=11):
    factor = 2
  else:
    factor = 1
  return factor

def getCompoundRisk(risk, factorFromDays):
  compundRisk = 0 
  if(risk == 1):
    if(factorFromDays == 1):
      compundRisk = 1
    elif(factorFromDays == 2):
      compundRisk = 2
    elif(factorFromDays == 3):
      compundRisk = 3
    else:
      compundRisk = 4
  elif(risk == 2):
    if(factorFromDays == 1):
      compundRisk = 1
    elif(factorFromDays == 2):
      compundRisk = 2
    elif(factorFromDays == 3):
      compundRisk = 3
    else:
      compundRisk = 4
  elif(risk == 3):
    if(factorFromDays == 1):
      compundRisk = 1
    elif(factorFromDays == 2):
      compundRisk = 2
    elif(factorFromDays == 3):
      compundRisk = 3
    else:
      compundRisk = 4
  elif(risk == 4):
    if(factorFromDays == 1):
      compundRisk = 1
    elif(factorFromDays == 2):
      compundRisk = 3
    else:
      compundRisk = 4
  return compundRisk




class Reunion:
  def __init__(self, users, duration, masks, openSpace, registeredDate):
    self.registeredDate = datetime.strptime(registeredDate,"%d/%m/%y")
    self.users = users
    self.duration = duration
    self.masks = masks
    self.openSpace = openSpace
    self.risk = 0
  

if(__name__ == "__main__"):
  # r1 = Reunion(3,20,True,True) 
  r2 = Reunion( ["mariana@mail.com", "caro@mail.com", "dario@mail.com" ],20,True,True, "20/04/21") 
  main(r2)