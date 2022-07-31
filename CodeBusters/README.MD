# Cryptography Puzzles
This chrome extension enhances toebes.com to allow autogeneration of Cryptographical Puzzles (Code Busters tests for Science Olympiad to help my teammates practice) by simply selecting a type of cipher (affine, ceasar, RSA, Baconian, etc.):
![image](https://user-images.githubusercontent.com/97496861/182004656-c5b93ef0-4b4a-498f-bed1-b61af7a45236.png)

# How it works
There is an API for generating cryptograms in a format acceptable by toebes.com hosted using Pythonanywhere.com. Then the chrome extension calls this API given the user-specified cryptograms and imports the result into toebes.com to be taken as a test.
