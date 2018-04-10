import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar_movie = media.Movie("Avatar", 
                           "A marine on an alien planet", 
                           "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                           "https://www.youtube.com/watch?v=5PSNL1qE6VY")

infinity_war = media.Movie("Avengers: Infinity War",
                           "The battle that brings together the Avengers defeat Thanos",
                           "http://3ipycv2ugat81cqgps20hwke-wpengine.netdna-ssl.com/wp-content/uploads/2018/03/AIW-Payoff_1_Sheet-SM-e1521209477602.jpg",
                           "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

school_of_rock = media.Movie("School of Rock",
                             "Storyline", 
                             "http://t2.gstatic.com/images?q=tbn:ANd9GcRMRyrfvOfl7RStLTmLNBIf86oc677YSkxdw1XeNHV928aAdL_3",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "Storyline", 
                          "https://image.tmdb.org/t/p/w600_and_h900_bestv2/xVxxSYHAfrEbllyWFQG5df5nwH4.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline", 
                                "http://t3.gstatic.com/images?q=tbn:ANd9GcTk3ssys2bKM5-U6XMgvoD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v")

hunger_games = media.Movie("Hunger Gamers",
                           "Storyline", 
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcS58mYVyiI3LTihImFjn6QBLU_mcHXZP3LaGoWN9u5bzuvW3lvC",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")
movies = [toy_story, avatar_movie, infinity_war, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)