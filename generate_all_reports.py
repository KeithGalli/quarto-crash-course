import os

genres = ['action', 'adventure', 'drama', 'science fiction', 'thriller', 'comedy', 
          'crime', 'animation', 'fantasy', 'horror', 'family', 'mystery', 'western', 
          'history', 'music', 'war', 'romance', 'documentary']

for genre in genres:
    print(f"Generating report for {genre} movies")
    os.system(f"quarto render parameterized-report.qmd -P genre:{genre} --output {genre}.html")