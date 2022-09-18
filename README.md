# hackZurich2022
Final repo for Schindler workshop challenge.

# Files in this repo

This repo contains two files, one being the Android Studio project of the elevator, and the second one inlcuding all the servers, jsons, APIs and files needed to run the application.


# Inspiration

We saw it from the moment we arrrived to HackZurich 2022. Too much time was being wasted by finding specific rooms. WIth this in mind, we started thinking of a solution that not only could improve HackZurich 2023 but also be applied to many other use cases such as office buildings and hospitals.

The motivation for doing the workshop in Elevate Passenger Experience by the hand of Schindler was primarily our interest in targeting and improving user experience. For us, this project targeted a broad scope, which could have been from improving social interactions in the lift to personalizing the cabin's design. This allow as to be very innovative, merging not only technology but creativity.

More specifically, we believed in the elevators of the future which will work towards what is known as seamless journey with a completely autonomous performance in your displacement from point A to point B. With this in mind, we aimed to simplify the transportation time providing a solid solution that facilitated the users journey.

# Project application

The solution to the challenge takes advantage of the already existing API provided by Schlinder, which has been used in order to incorporate user experience functions simulating the automatic elevator´s call. The main feature for the project is the Elevating app where the user can have access to the specific locations in a particular facility. With this, the user can directly select in the app "Go to sleeping room" and automatically call the autonomous elevator which will provide the right indications to get there. Additionally, the app can be syncronised to Google Calendar with the elevators in the building, so the lift will take the user directly to the floor where the next meeting is going to take place.

Moreover, a map of the floor will be displayed with the blueprint of the building. Thanks to that, the user will save time trying to find the room and without needing to interact with the elevator because of the real-time communication.

# Workflow and technology used

The app has been developed with Android Studio, where Java has been the main language for programming. Either the backend or frontend are located in the app. For establishing a connection between the app and Schindler API, a python server has been built with the FastAPI framework, which interacts with the GUI provided so as to see the movements of the elevators. Secondly, the Python server also runs the Google Calendar synchronization, where information regarding floors and rooms is taken from requests and sent between the nodes. The Postman tool has been used to test the different APIs and to support code creation.

# CHALLENGES

The challenge of this project has been primarily the time. We are not used to developing full projects within less than two days. Moreover, since we are all from different backgrounds, despite the fact that we have a wide perspective, some technical issues required more time to fix than expected.

# WHAT WE LEARNED

In this Zurich Hackathon 2022 we have learned about new technology such as FastAPI, new functions, and libraries for programming. But most of all, we have realised of the importance of having a good team, not only an experienced one, but more specifically, a creative, fun and supportive one. More than ever we have learned to work as a team since we only had less than two days to develop something functional. Thanks to that, we have needed to be all on the same page and establishing good communication as a team to be able to provide a solution. And last but not least, since most of us were completely new to the hackathon expierence we have lived this oportunity.

# WHAT IS NEXT FOR THE PROJECT

A database with the goal of storing information and providing access to a history could be incorporated into the system. Most likely, a non-SQL database with a proper schema, such as MongoDB, will save information in JSON files.

A dashboard could also be a potentional use case, where a screen placed in the elevator will provide the user the experience of interacting with different functions.

We would like to include user authentication so that the elevator can optimise the passengers journey and offer a more personalised user experience.

The current app can be improved with further functionalities such as full control of the elevators design providing access to the cabin's design involving color and vibes.

We are looking forward to Zurich’s Hackathon 2023 to face new challenges!
