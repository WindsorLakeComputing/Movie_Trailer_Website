import webbrowser
import fresh_tomatoes

class Movie():

    def __init__ (self, movie_title, movie_storyline, poster_image,
                trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
	
	#Open the movie trailer inside of youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

terminator = Movie("Terminator",
                      "A Killer robot comes back in time to kill an attractive young lady",
                      "http://img3.wikia.nocookie.net/__cb20110513152209/terminator/images/c/ca/Terminator_poster.jpg",
                      "https://www.youtube.com/watch?v=lHz95RYUbik")

jurassic_park = Movie("Jurassic Park",
                      "A Dinosaur theme park.",
                      "http://s3-ec.buzzfed.com/static/2014-08/12/12/enhanced/webdr10/enhanced-14020-1407861668-13.jpg",
		      		  "https://www.youtube.com/watch?v=lc0UehYemQA")

e_t = Movie("E. T.",
                      "An Extra Terrestrial has an out of this world experience with a young boy",
                      "http://img3.wikia.nocookie.net/__cb20110426225917/bladerunner/images/d/d0/Et_poster.jpg",
		              "https://www.youtube.com/watch?v=qYAETtIIClk")
					  
sandlot = Movie("The Sandlot",
                      "A pack of down on their luck kids turn to baseball to assuage their fears",
                      "http://www.amfm-magazine.com/wp-content/uploads/2013/06/the-sandlot-movie-poster.jpg",
                      "http://www.youtube.com/watch?v=-QDq-e1GbjE")

total_recall = Movie("Total Recall",
                      "A man pays for the services of \"Recall\" - a company that will \"remember it for you wholesale.\"",
                      "http://images.moviefanatic.com/iu/v1391803830/total-recall-1990-poster.jpg",
		              "https://www.youtube.com/watch?v=WFMLGEHdIjE")
					  

movies = [terminator, jurassic_park, e_t, sandlot, total_recall]

fresh_tomatoes.open_movies_page(movies)
#print("The name is ", Movie.__name__)
#print("The module is ", Movie.__module__)
#terminator.show_trailer()
