# import pandas as pd
import pickle
# import nump


PICKLE_PATH = "../app/board_games_pipeline.pkl"


class ModelHelper():
    def __init__(self):
        with open(PICKLE_PATH, 'rb') as pickle_file:
            payload = pickle.load(pickle_file)

        self.feature_df = payload["feature_df"]
        self.preprocessor = payload["preprocessor"]
        self.model = payload["model"]


    def get_game(self, game_name):
        name_match_mask_s = self.feature_df['name'].str.lower() == game_name.strip().lower()
        matching_rows_df = self.feature_df[name_match_mask_s]
        return matching_rows_df
    

    def get_all_recommendations(self, game):
        preprocessor = self.preprocessor
        model = self.model
        df = self.feature_df

        game_features_df = game.drop(columns=['name'])
        game_features_preprocessed = preprocessor.transform(game_features_df) 
        distances, indices = model.kneighbors(game_features_preprocessed) 
        games = df.iloc[indices[0]]  # Select tracks corresponding to the nearest neighbors
        games["distance"] = distances[0]  # Add the distance of each neighbor as a new column

        # Step 10: Filter the columns for the final output
        cols = games.columns # you can explicitly choose to return specific columns here
        games = games.loc[:, cols]  # Keep the relevant columns
        games = games.sort_values(by="distance")  # Sort the tracks by their distance (most similar first)

        # Step 11: Return the recommended tracks as a list of dictionaries
        return games #.to_dict(orient="records")
    

    def filter_recommendations(self, recommended_games_df, gamelist_length, min_players, max_players, 
                               min_playtime, max_playtime, min_age, min_average_rating):
        filtered_games_df = recommended_games_df[
            (recommended_games_df['max_players'] <= max_players) &
            (recommended_games_df['max_playtime'] <= max_playtime) &
            (recommended_games_df['min_age'] >= min_age) &
            (recommended_games_df['min_players'] >= min_players) &
            (recommended_games_df['min_playtime'] >= min_playtime) &
            (recommended_games_df['average_rating'] >= min_average_rating)
        ]
        filtered_limited_games_df = filtered_games_df.head(gamelist_length)
        return filtered_limited_games_df.to_dict(orient="records")
    

    def make_game_recommendations(self, name, gamelist_length, min_players, max_players,
                              min_playtime, max_playtime, min_age, min_average_rating):
        game = self.get_game(name)
        all_recommended_games_df = self.get_all_recommendations(game)
        recommendations = self.filter_recommendations(all_recommended_games_df, gamelist_length, min_players, max_players,
                            min_playtime, max_playtime, min_age, min_average_rating)
        return recommendations

    # def makePredictions(self, name, gamelist_length, max_players, max_playtime, min_age, min_players, min_playtime, average_):
    #     # create dataframe of one row for inference
        
    #     df = pd.DataFrame()
    #     df["name"] = [name]
    #     df["Age"] = [age]
    #     df["Fare"] = [fare]
    #     df["Has_Cabin"] = [has_cabin]
    #     df["Family_Size"] = [familySize]
    #     df["Pclass"] = [p_class]
    #     df["Embarked"] = [embarked]

    #     # # model
    #     # model = pickle.load(open("titanic_model_pipeline2.h5", 'rb'))
    #     # with open("titanic_model_pipeline2.h5", 'rb') as model_file:
    #     #     model = model_file.read()

    #     # columns in order
    #     df = df.loc[:, ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Has_Cabin', 'Family_Size']]

    #     preds = self.model.predict_proba(df)
    #     return(preds[0][1])
