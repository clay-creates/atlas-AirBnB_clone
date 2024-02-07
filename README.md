# AirBnb Clone - The Console

## Table of Contents
- [Usage](#usage)
- [Models](#models)
- [Engine](#engine)
- [Testing](#testing)
- [Authors](#authors)

### Usage

To run the console you can execute the following command:  
python console.py  

You should see the console open, and be greeted by the prompt:  
(hbnb)  

After this, you can run the following included commands:  
- create (creates a new instance of BaseModel and saves it to storage)
- show
- destroy
- all
- update
- quit (exits the program)
- EOF (handles EOF and exits)

### Models
- amenity- stores the name of an amenity
- base model- the template from which models inherit attributes
- city- stores the name of a city
- place- stores the location data of a place
- review- stores text about a place and the name of a user
- state- stores the name of a state
- user- stores the name, email, and password of a user

### Engine

![Alt text](AirBnB_storage_flowchart.jpg?raw=true)

### Testing

![Alt text](unittests.png?raw=true)
Tests the saving and loading of all types of data entered through any model
To engage testing use this command outside of the airbnb console:
- python -m unittest discover -s tests


### Authors

Clay Jones - https://github.com/clay-creates  
Jesse Brumley - https://github.com/jessebrumley