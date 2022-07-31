# Calculator Programs for It's About Time
It's About Time (IAT) is a Science Olympiad event that requires students to solve physics, trivia, and unit conversion problems related to time. Some things like calendar and timezone conversions are a pain to do/memorize by hand, so I wrote claculator programs to do it. Tested on the TI-84 Plus CE.

## How to use
Download the desired files to your calculator using TI Connect (provided by Texas Instruments) and run the programs by pressing ```pgrm``` > ```EXEC``` > [program name]. Then simply provide the inputs when prompted by pressing ```enter``` to proceed.

## Programs
1. AEASTER
Given the year, prints the month (1=January...12=December) and day in the Gregorian calendar that easter falls on that year. Does not work proleptically (i.e. before 1582 when the Gregorian calendar was introduced).
<img src="https://user-images.githubusercontent.com/97496861/182005108-30b885a5-0fde-4488-be5f-f78f888be674.jpg" width="200">

2. AGREGINFO
Given a Gregorian date, prints out the corresponding Julian Day Number (JD), Julian Date, and day of the week (0=Sunday, 1=Monday...6=Saturday).
<img src="https://user-images.githubusercontent.com/97496861/182005218-04239f8e-4c8c-44ca-8bf5-f9433ee67ca5.jpg" width="200">

3. AJDINFO
Given a JD number, prints out the corresponding Julian Data, day of the week, and Gregorian Date.
<img src="https://user-images.githubusercontent.com/97496861/182005320-7ae7d395-7e22-4e12-b7be-2a563ceaf551.jpg" width="200">

4. AJULINFO
Given a date using the Julian calendar, prints out the corresponding Julian Day Number (JD), Gregorian Date, and day of the week (0=Sunday, 1=Monday...6=Saturday).
<img src="https://user-images.githubusercontent.com/97496861/182005359-989de9e0-6b37-4f85-a33b-36553efc67e7.jpg" width="200">

5. ATIMEZON
Search engine to look up UTC offset of various cities, countries and time zones. Simply use the ```alpha``` button to type in a keyword like the city/country/timezone name and the program will print the first occurence in its database. 
<img src="https://user-images.githubusercontent.com/97496861/182005405-8c1ab6b2-f017-4f68-81cb-886f52cffa9e.jpg" width="200">
Output format is "==UTC{offset: in hours, +/-}--{Timezone}--{Country}--{comma seperated list of cities}" repeated over and over. Look for the one with your keyword:
<img src="https://user-images.githubusercontent.com/97496861/182005483-ed2f9c40-fcd2-4295-829c-83238e55dcf4.jpg" width="200">

6. ASTATS
Quickly calculates statistics for multiple lists and does a regression line. Useful for EXPD.
<img src="https://user-images.githubusercontent.com/97496861/182005563-1556d495-6dc7-43dc-9a9e-48bce5529f34.jpg" width="200">
