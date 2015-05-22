"""This file contains the various movie data and calls
   the fresh_tomatoes function to build the html page"""

#media contains the classes for Video and Movie
import media
#fresh_tomates contains the function to render the movies page html
import fresh_tomatoes

# make an array to hold the movie instances
movies = []

# make instances of movie class
# then add movie instance to movies array
# and repeat

big_lebowski = media.Movie("The Big Lebowski",
                           "1998",
                           "117 minutes",
                           ("\"The Dude\" Lebowski, mistaken for a millionaire "
                            "Lebowski, seeks restitution for his ruined rug and "
                            "enlists his bowling buddies to help get it."),
                           "http://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y")
movies.append(big_lebowski)


bridesmaids = media.Movie("Bridesmaids",
                          "2011",
                          "125 minutes",
                          ("Competition between the maid of honor and a bridesmaid, "
                           "over who is the bride's best friend, threatens to upend "
                           "the life of an out-of-work pastry chef."),
                          "http://upload.wikimedia.org/wikipedia/en/d/df/BridesmaidsPoster.jpg",
                          "https://www.youtube.com/watch?v=JgacDwgKiZg")
movies.append(bridesmaids)


caddyshack = media.Movie("Caddyshack",
                         "1980",
                         "117 minutes",
                         ("An exclusive golf course has to deal with a brash new "
                          "member and a destructive dancing gopher."),
                         "http://upload.wikimedia.org/wikipedia/en/8/84/Caddyshack_poster.jpg",
                         "https://www.youtube.com/watch?v=5b5RnNf9ShY")
movies.append(caddyshack)

dead_poets_society = media.Movie("Dead Poets Society",
                                 "1989",
                                 "128 minutes",
                                 ("With their teacher's help, students learn "
                                  "to break out of their shells, pursue their "
                                  "dreams and seize the day."),
                                 "http://upload.wikimedia.org/wikipedia/en/4/49/Dead_poets_society.jpg",
                                 "https://www.youtube.com/watch?v=wrBk780aOis")
movies.append(dead_poets_society)


fargo = media.Movie("Fargo",
                    "1996",
                    "98 minutes",
                    ("Jerry Lundegaard's inept crime falls apart due to his and his "
                     "henchmen's bungling and the persistent police work of the quite "
                     "pregnant Marge Gunderson."),
                    "http://upload.wikimedia.org/wikipedia/en/a/ac/Fargo.jpg",
                    "https://www.youtube.com/watch?v=h2tY82z3xXU")
movies.append(fargo)


finding_forrester = media.Movie("Finding Forrester",
                                "2000",
                                "136 minutes",
                                "A young writing prodigy finds a mentor in a reclusive author.",
                                "http://upload.wikimedia.org/wikipedia/en/1/16/Finding_forrester.jpg",
                                "https://www.youtube.com/watch?v=sxvtVBeKX_o")
movies.append(finding_forrester)


gone_girl = media.Movie("Gone Girl",
                        "2014",
                        "149 minutes",
                        ("With his wife's disappearance having become the "
                         "focus of an intense media circus, a man sees the "
                         "spotlight turned on him when it's suspected that "
                         "he may not be innocent."),
                        "http://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
                        "https://www.youtube.com/watch?v=esGn-xKFZdU")
movies.append(gone_girl)


good_will_hunting = media.Movie("Good Will Hunting",
                                "1996",
                                "98 minutes",
                                ("Will Hunting, a janitor at M.I.T., has a "
                                 "gift for mathematics, but needs help from "
                                 "a psychologist to find direction in his "
                                 "life."),
                                "http://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=DyiPHC_VQFY")
movies.append(good_will_hunting)


the_hangover = media.Movie("The Hangover",
                           "2009",
                           "100 minutes",
                           ("Three buddies wake up from a bachelor party in "
                            "Las Vegas, with no memory of the previous night "
                            "and the bachelor missing. They make their way "
                            "around the city in order to find their friend "
                            "before his wedding."),
                           "http://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                           "https://www.youtube.com/watch?v=tcdUhdOlz9M")
movies.append(the_hangover)


legally_blonde = media.Movie("Legally Blonde",
                             "2001",
                             "96 min",
                             ("When a blonde sorority queen is dumped by her "
                              "boyfriend, she decides to follow him to law "
                              "school to get him back and, once there, learns "
                              "she has more legal savvy than she ever imagined."),
                             "http://upload.wikimedia.org/wikipedia/en/a/ac/Legally_blonde.jpg",
                             "https://www.youtube.com/watch?v=E8I-Qzmbqnc")

# add movie instance to movies array
movies.append(legally_blonde)


monty_python_and_the_holy_grail = media.Movie("Monty Python and the Holy Grail",
                                              "1975",
                                              "91 minutes",
                                              ("King Arthur and his knights embark "
                                               "on a low-budget search for the Grail, "
                                               "encountering many very silly obstacles."),
                                              "http://upload.wikimedia.org/wikipedia/en/4/49/Monty_python_and_the_holy_grail_2001_release_movie_poster.jpg",
                                              "https://www.youtube.com/watch?v=urRkGvhXc8w")
movies.append(monty_python_and_the_holy_grail)


moonrise_kingdom = media.Movie("Moonrise Kingdom",
                               "2012",
                               "94 minutes",
                               ("A pair of young lovers flee their New England "
                                "town, which causes a local search party to fan "
                                "out to find them."),
                               "http://upload.wikimedia.org/wikipedia/en/4/4f/Moonrise_Kingdom_FilmPoster.jpeg",
                               "https://www.youtube.com/watch?v=7N8wkVA4_8s")
movies.append(moonrise_kingdom)


princess_bride = media.Movie("The Princess Bride",
                             "1987",
                             "98 min",
                             ("A fairy tale adventure about a beautiful young "
                              "woman and her one true love."),
                             "http://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
                             "http://www.youtube.com/watch?v=VYgcrny2hRs")
movies.append(princess_bride)


ted = media.Movie("Ted",
                  "1987",
                  "98 min",
                  ("As the result of a childhood wish, John Bennett's teddy "
                   "bear, Ted, came to life and has been by John's side ever "
                   "since - a friendship that's tested when Lori, John's "
                   "girlfriend of four years, wants more from their relationship."),
                  "http://upload.wikimedia.org/wikipedia/en/6/62/Ted_poster.jpg",
                  "https://www.youtube.com/watch?v=8YBlnHxkCJc")
movies.append(ted)


terms_of_endearment = media.Movie("Terms of Endearment",
                                  "1983",
                                  "132 min",
                                  ("Follows hard-to-please Aurora looking for "
                                   "love and her daughter's family problems."),
                                  "http://upload.wikimedia.org/wikipedia/en/b/bf/Terms_of_Endearment%2C_1983_film.jpg",
                                  "https://www.youtube.com/watch?v=fsdDeh0M_nk")
movies.append(terms_of_endearment)

#call open_movies_page to generate html and open in browser.
fresh_tomatoes.open_movies_page(movies)
