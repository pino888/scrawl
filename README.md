# Scrawl

###  A social media app for the writers, and the readers.
The aim of the app was to create something that connects writers (me being one myself), without distracting their artistic mind with ever
so polluted other social medias.
I chose this project to practice the Django framework and explore web development principles.
This projects provides a functional, although not very styled, version of the app. The features are:
- Creating the account/profile
- Posting the *Scrawls* which appear in the feed
- Liking, commenting, saving public *Scrawls*
- Liking the comments
- Following/Unfollowing other users
- *QuillBoard* - a list of the top 20 Scrawls, which are determined by the number of likes.
- User profile, containing all of their Scrawls, saved Scrawls, lists of followers
- Utilities like password change and logout

### How to use

- Fetch/Fork the repo
- Install the requirements
- Run the migrations
- Make sure to create the .env file which should contain your SECRET_KEY, DEBUG, and EMAIL settings.
I'm using the [python-decouple](https://pypi.org/project/python-decouple/) module to import these. 

### Demo
You can explore the demo version in [here](https://pdani.pythonanywhere.com/) - As the project requires to be logged in, feel free to create your own 
account or login as a *Guest* (user: guest, password: 1bigmountain). I'd be delighted if you add some content
and/or interact with the demo - any feedback would be greatly appreciated too!

### Credits
The initial build was based on this *Real Python* tutorial - [Build a Social Network With Django.](https://realpython.com/django-social-network-1/)
Although, only the part 1 and, I've opted for Bootstrap instead of Bulma.

### License
MIT License. Feel free to use it as a skeleton for any of your projects, either personal or commercial
use. Any credit to my git account would be great and please consider giving this project a star :)