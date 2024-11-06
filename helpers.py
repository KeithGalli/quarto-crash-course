import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def plot_top_movies_by_rating(df, n=10):
    """
    Creates a bar plot of top N movies by vote average.
    
    Parameters:
    df (pandas.DataFrame): Movie dataset
    n (int): Number of movies to display
    """
    plt.figure(figsize=(12, 6))
    top_movies = df.nlargest(n, 'vote_average')
    sns.barplot(data=top_movies, x='vote_average', y='title')
    plt.title(f'Top {n} Movies by Rating')
    plt.xlabel('Vote Average')
    plt.ylabel('Movie Title')
    plt.tight_layout()
    return plt

def plot_revenue_vs_budget(df):
    """
    Creates a scatter plot of revenue vs budget with additional information.
    
    Parameters:
    df (pandas.DataFrame): Movie dataset
    """
    # plt.figure(figsize=(10, 6))
    plt.scatter(df['budget'], df['revenue'], alpha=0.5)
    plt.xlabel('Budget ($)')
    plt.ylabel('Revenue ($)')
    plt.title('Movie Budget vs Revenue')
    
    # Add a break-even line
    max_value = max(df['budget'].max(), df['revenue'].max())
    plt.plot([0, max_value], [0, max_value], 'r--', label='Break-even line')
    plt.legend()
    plt.tight_layout()
    return plt

def create_genre_distribution(df):
    """
    Creates a bar plot of genre distribution.
    
    Parameters:
    df (pandas.DataFrame): Movie dataset
    """
    # Extract all genres
    all_genres = []
    for genres in df['genres'].str.split(','):
        if isinstance(genres, list):
            all_genres.extend([g.strip() for g in genres])
    
    # Count genre frequencies
    genre_counts = pd.Series(all_genres).value_counts()
    
    genre_counts.plot(kind='bar')
    plt.title('Distribution of Movie Genres')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

def create_keyword_wordcloud(df):
    """
    Creates a word cloud from movie keywords.
    
    Parameters:
    df (pandas.DataFrame): Movie dataset
    """
    all_keywords = []
    for keywords in df['keywords'].fillna(''):
        # Split the keywords string and clean each keyword
        if isinstance(keywords, str):
            keywords_list = [k.strip() for k in keywords.split(',')]
            all_keywords.extend(keywords_list)
    
    # Join all keywords into a single string
    keywords_text = ' '.join(all_keywords)
    
    # Create and generate a word cloud image
    wordcloud = WordCloud(width=800, height=400, 
                         background_color='white',
                         max_words=100).generate(keywords_text)
    
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Movie Keywords Word Cloud')
    plt.tight_layout(pad=0)
    return plt

def plot_release_year_distribution(df):
    """
    Creates a histogram of movie release years.
    
    Parameters:
    df (pandas.DataFrame): Movie dataset
    """
    # Extract years from release_date
    df['year'] = pd.to_datetime(df['release_date']).dt.year
    
    # plt.figure(figsize=(10, 6))
    plt.hist(df['year'], bins=20, edgecolor='black')
    plt.title('Distribution of Movie Release Years')
    plt.xlabel('Release Year')
    plt.ylabel('Number of Movies')
    plt.tight_layout()
    return plt

