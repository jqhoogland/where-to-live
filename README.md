# Where to live?

There are other places to live besides SF and Austin. I'd like to find out where they are.

Inspired by XKCD's:
![temperature preferences](https://imgs.xkcd.com/comics/temperature_preferences_2x.png)

I want similar plots for other interesting metrics:
- Climate resilience,
- Size of the city,
- Affordability,
- Access to nature,
- etc.

And a lookup tool. And maybe a suggestion tool (once you've weighted all the metrics accordingly).

## The Data

#### Temperature
Source 1: [City monthly average temperatures](https://en.wikipedia.org/wiki/List_of_cities_by_average_temperature)
Source 2: [All the data](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt)

First, the maximum and minimum monthly average temperatures per city. XKCD's used humidex, but this will come close enough.
Note: this doesn't factor in the differences between daily high and low (it averages across the entire day). So some desert places will appear more temperate than they are.

Note: I didn't check each of the references (I didn't check any).


#### [Population](https://population.un.org/wup/Download/)
> United Nations, Department of Economic and Social Affairs, Population Division (2018). World Urbanization Prospects: The 2018 Revision, Online Edition.

See also: https://worldpopulationreview.com/world-cities



#### TODOs
- Environmental
  - [Humidex](https://en.wikipedia.org/wiki/Humidex)
  - [Heat index](https://en.wikipedia.org/wiki/Heat_index) & Wind chill
  - Average of maximum daily temperature vs. average of minimum daily temperature.
  - Precipitation
  - Humidity
  - [Sunshine duration](https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration) & daylight duration
  - Insolation (Solar irradiance) - for those of us who burn easily.
  - Air Quality index
  - Type of climate / biome
  - Estimated future values of all of these.
- Demographic
  - Safety / crime
  - Education quality
  - Population density
  - Population size
  - Home price, cost of living
  - Median income
  - Percentage of foreign origin
  - Health & lifespan
  - Median age
  - [City "type"](https://www.sciencemag.org/news/2014/10/there-are-only-four-types-cities)
  - Distinguish city proper and metropolitan area.
