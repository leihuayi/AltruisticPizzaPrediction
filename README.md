# AltruisticPizzaPrediction
The [Reddit Thread "Random Acts of Pizza"](https://www.reddit.com/r/Random_Acts_Of_Pizza/) is made of a bunch of people making posts to request others to offer them a pizza. Other members of the thread can decide to be altruistic and offer them the pizza they queried.
The purpose of this project is to be able to predict, using Machine Learning / NLP, using as input a typical Reddit post requesting a pizza, the likelyness that this person will effectively receive a pizza.

## References
* [Kaggle Challenge](https://www.kaggle.com/competitions/random-acts-of-pizza/overview)
* [Accompanying paper](https://cs.stanford.edu/~althoff/raop-dataset/altruistic_requests_icwsm.pdf) of Tim Althoff, Cristian Danescu-Niculescu-Mizil, Dan Jurafsky. _How to Ask for a Favor: A Case Study on the Success of Altruistic Requests_, Proceedings of ICWSM, 2014.

## Project structure
This project aims at providing an implementation for solving the Random Acts of Pizza prediction as it would have been done in an industrial process. Therefore it is organized in **two folders**:
* datascience
* demo

These 2 folders are completely independant and could have been in 2 different git repos.
I put them on the same for my own convenience and to avoid too many repos on my account :)

### Datascience folder
It encompasses all the code which would have been provided by the data science team of the company.
* research : all the code for exploring the data, train the ML algorithm
* raopred : python package which contains the best model and prediction code, which would be given to the dev team

### Demo folder
It encompasses all the code which would have been provided by the dev team of the company.
* api : python FastApi api for running a ML prediction through the package provided by the data science team
* client : front-end of website
