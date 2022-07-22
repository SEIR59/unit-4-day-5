# Bird Collector

* Project Setup
1. Create the database
 * createdb birdcollector2

 2. Start the project
 * django-admin startproject birdcollector2

3. Change into the birdcollector directory and open the project in VScode
* cd birdcollector
* code .

4. Create the app
* python3 manage.py startapp main_app

5.Add main_app to the list of INSTALLED_APPS in settings.py

6. Check that your project starts up
 * python3 manage.py runserver

 7. Connecting to the Database

8. Run the initial migration
 * python3 manage.py migrate

# User Story
* AAU, I want to be able to navigate to separate pages for About and All Birds using a navbar.

* AAU, when I visit the About page, I want to view some details about the birdcollector application.

* AAU, when I visit the All  Birds page, I want to view a list of all birds that displays each of the attributes of a bird.

* AAU, when I visit the All Birds page, I want to view a list of all birds from the database that displays each of the attributes of the bird.

* AAU, when I click on a bird card on the index page, I want to be taken to a details page where I can see all attributes of the bird.

* AAU, I want to be able to add a Bird to my list of Birds.

* AAU, I want to be able to add edit the attributes of a Bird.

* AAU, I want to be able to remove a Bird from my list of Birds.

* AAU, when I visit the detail page for a bird, I want to see a list of feedings for that bird.

* AAU, when I visit the detail page for a bird, I want to be able to add a feeding for a bird.

* AAU, when I visit the detail page for a bird, I want to see a message displaying a status of 'hungry' or 'fed'.

* AAU, I want to see a list displaying all of the toys in the database.

* AAU, I want to be able to add a Toy to list of Toys.

* AAU, when I visit the detail page for a bird, I want to see a list of toys belonging to the bird, and also any available toys that I can add to the bird.

