/*
Japanese Cities' Attributes
https://www.hackerrank.com/challenges/japanese-cities-attributes/problem

Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

The CITY table is described as follows:

CITY
FIELD TYPE
ID NUMBER
NAME VARCHAR2(17)
COUNTRYCODE VARCHAR2(3)
DISTRICT VARCHAR2(20)
POPULATION NUMBER
*/

SELECT * FROM CITY 
WHERE COUNTRYCODE = 'JPN';