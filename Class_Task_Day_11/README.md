# Class Task Day 11

# Class task
* Craete a new class named `Person` with the following properties:
    * `age` 
    * `name`
    * `eye_color`
* Add to the `Person` class 3 functions:
    * `set_age` - gets an age:
        * if the age is not in the range 0-120 - raise an error
        * if the age is in the range 0-120 save it to the instance `age` property
    * `set_name` - gets a name:
        * if the name length is not in the range 3-9 - raise an error
        * if the name length is in the range 3-9 save it to the instance `name` property
    * `set_eye_color` - gets an eye_color:
        * if the eye_color is not `green` / `brown` / `blue` - raise an error
        * if the eye_color is `green` / `brown` / `blue` save it to the instance `eye_color` property

* In the main code create an array with 5 persons
* Run through the array with a loop, and for each element do the following actions:
    * call `set_age` - with a random number (between -20 to 200)
    * call `set_name` - with a random name from this array: `["Tom", "li" , "Bob" , "Alice" , "Clarc" , "Adam" , "Sean"]`
    * call `set_eye_color` - with a random color from this array: `["green", "blue" , "yellow" , "black" ]`   
    
`Note:` : if an error was raised - you must catch the error, and try to assign again a new value
* Run through the array with a loop, and print for each element the `age`,`name` and `eye_color`


* Code:

![picture](https://github.com/ORELxD/Python/blob/master/Class_Task_Day_11/%E2%80%8F%E2%80%8FExceptions.JPG)


![picture](https://github.com/ORELxD/Python/blob/master/Class_Task_Day_11/Set%20age.JPG)


![picture](https://github.com/ORELxD/Python/blob/master/Class_Task_Day_11/%E2%80%8F%E2%80%8FSet%20name.JPG)


![picture](https://github.com/ORELxD/Python/blob/master/Class_Task_Day_11/Set%20eye%20color.JPG)


![picture](https://github.com/ORELxD/Python/blob/master/Class_Task_Day_11/%E2%80%8F%E2%80%8FMain.JPG)


* Result:

![picture](https://github.com/ORELxD/Python/blob/master/Class_Task_Day_11/%E2%80%8F%E2%80%8FResult.JPG)
