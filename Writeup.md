Board Game Recommender System: Analysis and Findings
Data Insights and Preprocessing
To develop a recommender system for board games, we first explored a dataset consisting of 10,000 plus games, each with details about categories, mechanics, player numbers, playtime, and ratings. A detailed analysis helped us understand the data and laid the groundwork for the recommender model.

Key Insights from Data:
Completeness: The dataset was fully populated with no missing values, ensuring all features were available for modeling.
Descriptive Analysis:
The average game allows around 5 players, with a few games designed for large groups (up to 999).
On average, games have a playtime of roughly 85 minutes, though some games recorded extreme playtimes of up to 60,000 minutes.
The average user rating sits at 6.43, indicating a positive reception for most games.
Relationships in the Data:
The correlation between maximum players and maximum playtime was practically non-existent (-0.0026), suggesting that games with many players don’t necessarily take longer to play.
A weak correlation (0.0713) was found between minimum players and minimum playtime, indicating a slight tendency for more players to increase game length, but not significantly.
Building the K-Nearest Neighbors (KNN) Recommender
Using the cleaned and preprocessed data, we implemented the K-Nearest Neighbors (KNN) algorithm to generate recommendations. The goal was to suggest games similar to those a user already likes by analyzing key attributes such as category, mechanic, playtime, and recommended age.

Feature Selection:
The categories and mechanics were simplified into binned groups to make comparison easier.
Playtime and age data were normalized to standardize the scales across different features.
Model Process:
We used the K-Nearest Neighbors algorithm with k=5 to calculate similarities between games.
Games that shared the most similar attributes, based on the selected features, were recommended as the closest matches.
Tableau Dashboards for Visualization
To provide further insights into user behavior and game features, we created two interactive dashboards using Tableau. These dashboards visualize the relationships between age, playtime, category, and mechanics.

1. Dashboard 1: Age, Category, and Mechanic Preferences
Purpose: This dashboard visualizes how different age groups gravitate toward certain game categories and mechanics.
Visualization: A heatmap displays the number of games played by each age group in various categories (like Strategy, Family, Party) and their corresponding mechanic preferences (such as Dice Rolling, Card Drafting).
Key Takeaways: Players under 18 tend to prefer family and party games, often featuring simpler mechanics like dice rolling. Meanwhile, older players favor strategy games, with more complex mechanics such as resource management and area control.
2. Dashboard 2: Age and Playtime per Category
Purpose: This dashboard explores how playtime and category preferences vary with age.
Visualization: A scatter plot with age on the x-axis and playtime on the y-axis highlights how different categories cater to different age groups. Color-coding by category makes it easy to see which types of games have longer or shorter playtimes.
Key Takeaways: Games designed for younger players tend to have shorter playtimes, while those aimed at older audiences, like strategy games, often involve longer and more involved gameplay.
Final Thoughts
Through a combination of K-Nearest Neighbors for recommendations and Tableau dashboards for visual analysis, we created a comprehensive board game recommendation system. The model effectively analyzes game categories, mechanics, and user preferences to suggest games that users are likely to enjoy. The dashboards further enrich the understanding of how player age affects game preferences in terms of categories, mechanics, and playtime.