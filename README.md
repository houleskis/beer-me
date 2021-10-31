# beer-on
A beer recommender for Ontarians

10,000ft architecture & design

1. Data Acquisition - LCBO web crawler
2. Data storage - database (csv for now)
3. API - submit current beer to obtain recommendations
4. Backend - receives requests from API (of current beer) and queries database for recommendations and returns them as API response 

Future
1. Mobile app
2. Label search using machine vision (for use with mobile)
3. Inventory & LCBO search - returns recommendations available at your nearest LCBO
