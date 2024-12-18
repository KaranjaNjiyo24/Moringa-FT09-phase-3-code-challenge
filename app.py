from database.setup import create_tables, drop_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Reset database (optional - comment out if you want to preserve data)
    drop_tables()
    
    # Initialize the database and create tables
    create_tables()

    # Demonstration of model creation and interactions
    try:
        # Create Authors
        john = Author(None, "John Doe")
        jane = Author(None, "Jane Smith")
        mike = Author(None, "Mike Johnson")

        # Create Magazines
        tech_weekly = Magazine(None, "Tech Weekly", "Technology")
        science_today = Magazine(None, "Science Today", "Science")
        
        # Create Articles
        article1 = Article(None, "AI Revolution", "Exploring the future of artificial intelligence", john.id, tech_weekly.id)
        article2 = Article(None, "Quantum Computing Basics", "Introduction to quantum mechanics", jane.id, tech_weekly.id)
        article3 = Article(None, "Climate Change Insights", "Understanding global warming", john.id, science_today.id)
        article4 = Article(None, "Space Exploration", "Latest developments in space research", mike.id, science_today.id)
        article5 = Article(None, "Machine Learning Trends", "Current trends in ML", john.id, science_today.id)

        # Demonstrate model methods
        print("\n--- Authors and Their Articles ---")
        for author in [john, jane, mike]:
            print(f"\n{author}")
            print("Articles:")
            for article in author.articles():
                print(f"- {article.title} (in {article.magazine.name})")
            
            print("\nMagazines:")
            for magazine in author.magazines():
                print(f"- {magazine.name}")

        print("\n--- Magazines and Their Details ---")
        for magazine in [tech_weekly, science_today]:
            print(f"\n{magazine}")
            print("Articles:")
            for article in magazine.articles():
                print(f"- {article.title} by {article.author.name}")
            
            print("\nContributors:")
            for contributor in magazine.contributors():
                print(f"- {contributor.name}")
            
            print("\nArticle Titles:")
            print(magazine.article_titles())
            
            print("\nContributing Authors:")
            print(magazine.contributing_authors())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
