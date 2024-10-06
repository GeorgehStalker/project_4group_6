Board Game Recommender Project
Introduction
Our team has a genuine love for board games and the happiness they bring during family gatherings. George looks forward to game nights with his family, hoping to create screen-free experiences for his kids. Katie enjoys playing with her dad, who boasts an impressive collection of games, while Chris has cherished memories of playing games with both family and friends since childhood. Together, we decided to develop a recommendation system that helps families discover new board games they will enjoy.

Project Goal
The primary aim of our project was to create a personalized board game recommendation system tailored to the unique preferences of each family. We focused on several key factors, including age ranges, game categories, playtimes, and game mechanics. By considering these elements, we hope to ensure that our recommendations resonate with various family dynamics and enhance the enjoyment of game nights.

Exploratory Data Analysis (EDA)
To kick off our project, we performed exploratory data analysis (EDA) using Python. We began by cleaning the dataset, which involved removing duplicate entries and addressing missing values. By analyzing the distributions of features such as game categories and playtimes, we gathered valuable insights to inform our recommendations. We utilized visualizations with Matplotlib to gain a clearer understanding of the data trends.

Machine Learning Approach
Our recommendation system employs the Nearest Neighbors algorithm, which helps identify games that are similar to those preferred by users. We implemented a hybrid approach that combines collaborative filtering, which considers the preferences of similar users, with content-based filtering, which looks at the characteristics of the games, including their categories and mechanics.

To facilitate our workflow, we established a Scikit-Learn pipeline for data preprocessing. This pipeline includes steps for scaling numerical features, encoding categorical variables, and effectively managing missing data. The use of a pipeline allowed us to maintain organization and consistency throughout the process.

Technical Stack
The technologies we used in our project include:

Python: The primary programming language for our data analysis and modeling tasks.
Pandas: A library for data manipulation and cleaning.
Scikit-Learn: Utilized for implementing the Nearest Neighbors algorithm and developing our recommendation system.
Flask: Employed to create a web application that enables user interaction with our recommendation system.
Visualizations
We also developed visualizations to present our findings and demonstrate the effectiveness of our recommendation system. By using Tableau, we created dashboards that showcase important metrics and trends in the board gaming world, making the data more accessible and engaging for users.

Conclusion and Future Work
In conclusion, our board game recommender system is designed to make it easier for families to find the perfect games, ultimately allowing them to enjoy more quality time together. Looking ahead, we plan to enhance our system by incorporating user feedback for continuous improvement in our recommendations. Additionally, we aim to explore more algorithms to refine the performance of our model further.