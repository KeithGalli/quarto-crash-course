import os

genres = ['action', 'adventure', 'drama', 'science fiction', 'thriller', 'comedy', 
          'crime', 'animation', 'fantasy', 'horror', 'family', 'mystery', 'western', 
          'history', 'music', 'war', 'romance', 'documentary']


for genre in genres:
    for i in range(5,25):
        print(f"Generating report for {genre} movies with {i} movies")
        os.system(f"quarto render parameterized-report.qmd -P genre:{genre} -P num_movies:{i} --output {genre}_{i}.pdf")