
import costyl as cstyl

def test_database(costyl, database_path):

  costyl.import_authors_files(database_path + "/src")
  costyl.import_target_files(database_path + "/target")

  costyl.generate_model(silenceWarnings=True)
  return costyl.predict_authors()

def getCorrectAnswersPercentage(guessesDict):
  
  totalGuesses = len(guessesDict)
  correctAnswers = 0

  for file, guess in guessesDict.items():
    
    try:
      if file.split("(")[1][:-1] == guess:
        correctAnswers += 1
    except:
      print('ERROR')
      print(file)
      print(guess)
      input()

  percentage = (correctAnswers / totalGuesses) * 100
  return percentage

