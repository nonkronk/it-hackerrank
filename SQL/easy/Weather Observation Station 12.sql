/*
Weather Observation Station 12
https://www.hackerrank.com/challenges/weather-observation-station-12/problem

Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

STATION
Field Type
ID NUMBER
CITY VARCHAR2(21)
STATE VARCHAR2(2)
LAT_N NUMBER
LONG_W NUMBER

where LAT_N is the northern latitude and LONG_W is the western longitude.
*/

SELECT DISTINCT(CITY) FROM STATION 
WHERE LEFT(CITY,1) NOT IN ("A", "I", "U", "E", "O")
AND RIGHT(CITY,1) NOT IN ("A", "I", "U", "E", "O");