import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon'])
outputWriter.writerow(['Здравствуй Мир!', 333])
outputWriter.writerow([1, 33 ,77])
outputFile.close()