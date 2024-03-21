import os
import requests
import mysql.connector


# Function to send a request to the API and return the post data
def get_post_data():
    api_url = "https://jsonplaceholder.typicode.com/posts?userId=1"
    response = requests.get(api_url)
    print(response.status_code)
    data = response.json()
    if isinstance(data, list) and len(data) > 0:
        return data  # Mengembalikan seluruh daftar data
    else:
        return None


# Function to insert post data into the MySQL table
def insert_into_mysql(posts):
    try:
        # Replace the connection parameters with your MySQL database details
        connection = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USERNAME"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME"),
        )

        cursor = connection.cursor()

        # Create the posts table if not exists
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS posts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                userId INT,
                title VARCHAR(255),
                body VARCHAR(255)
            )
        """
        )

        # Insert post data into the table
        for post in posts:
            cursor.execute(
                """
                INSERT INTO posts (userId, title, body)
                VALUES (%s, %s, %s)
            """,
                (post["userId"], post["title"], post["body"]),
            )

        connection.commit()
        print("Data inserted successfully into MySQL")

        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Step 1: Get post data from the API
    posts_data = get_post_data()

    if posts_data is not None:
        # Step 2: Extract relevant information and insert into MySQL
        if isinstance(posts_data, list) and posts_data:
            post_info_to_insert = [
                {
                    "userId": post["userId"],
                    "title": post["title"],
                    "body": post["body"],
                }
                for post in posts_data
            ]
            insert_into_mysql(post_info_to_insert)
        else:
            print("No post data retrieved from the API.")
    else:
        print("Error: Unable to retrieve post data from the API.")