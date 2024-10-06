Board Game Recommender Project

Introduction

Our group is passionate about board games and the joy they bring to family time. George enjoys having game nights with his family and wants to help his kids enjoy quality time without screens. Katie loves playing games with her dad, who has a vast collection, and Chris has been playing since childhood, sharing fun moments with both family and friends. Together, we wanted to create a recommendation system that helps families discover new games they will love.

Project Goal

The goal of our project was to build an effective board game recommendation system that considers each family's unique preferences. We focused on various aspects such as age ranges, game categories, playtimes, and game mechanics. By addressing these elements, we aim to ensure our recommendations fit different family dynamics and make game nights even more enjoyable.

Exploratory Data Analysis (EDA)

To start the project, we conducted exploratory data analysis (EDA) using Python. We cleaned the dataset by removing duplicates and filling in missing values. By examining the distributions of features like game categories and playtimes, we gained insights that would guide our recommendations. We created simple visualizations using Matplotlib to help us understand the trends in the data better.

Machine Learning Approach

For our recommendation system, we used the Nearest Neighbors algorithm. This algorithm helps us find games similar to ones users like based on their preferences. We combined two approaches: collaborative filtering, which looks at what similar users enjoyed, and content-based filtering, which focuses on the attributes of the games, like their categories and mechanics.

To make our process smoother, we set up a Scikit-Learn pipeline for data preprocessing. This included scaling numerical features, encoding categorical variables, and handling missing data effectively. Using a pipeline helped us keep everything organized and consistent.

Technical Stack

We built the project using:

Python: Our main programming language for data analysis and modeling.
Pandas: For data manipulation and cleaning.
Scikit-Learn: To implement the Nearest Neighbors algorithm and build our recommendation system.
Flask: To create a web application that allows users to interact with our recommender system.
Visualizations

We also created visualizations to display our findings and the performance of our recommendation system. Using Tableau, we designed dashboards to highlight important metrics and trends in board gaming, making it easier for users to engage with our data.

Conclusion and Future Work

In summary, our board game recommender system aims to simplify the process of finding the right games for families. This way, they can spend more quality time together. Looking ahead, we plan to enhance our system by incorporating user feedback to improve recommendations continually. We also want to explore more algorithms and further refine how well our model performs.