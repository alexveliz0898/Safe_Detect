# Safe_Detect
This code was written at my first hackathon at HackNY Spring 2018

We were inspired by the magic of Clarifai, and its accuracy, to create something that could potentially save lives.
Due to a lot of mass shootings, we thought of a way that we could use this technology to decrease the death toll on 
unsuspecting civilians, and increase the reaction time of law enforcement.

My team used Clarifai’s image detection API to identify guns in images, and Twilio’s API to text people in the vicinity,
warning them of possible danger. We hoped technology like this can save people from shootings in public places.

Using the Clarifai API, the program can detect whether or not a gun is present in the image. If there is a gun present, then 
then another script is executed. The second script is using the Twilio API that send out a mass text alert to all present 
near the incident.

We ended up winning a $100 prize for best use of Clarifai's API.
