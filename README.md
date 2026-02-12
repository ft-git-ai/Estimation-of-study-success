# Estimation-of-study-success
Final project for the Building AI course

## Summary

The project concerns secondary school studies.
Based on primary school results,
the model estimates future success in studies at the chosen secondary school.


## Background

My idea helps to solve the following problems in particular:
* the problem of choosing a suitable school
* the problem of students' professional orientation
* the problem of students' self-assessment
Every year, entire generations of students solve the problem of their professional orientation and choice of high school.
Often students do not know how to choose a high school. Their teachers try to
advise them in this situation. Students could also get this advice from an artificial intelligence model.

## How is it used?

The input will be grades from the primary school report card and the output will be an estimate of the result of the school-leaving exam. The input and output interface of the application could be part of the school website.
The demo directory contains simple application code in Python. Fictitious data for this simplified demo version is part of the code.

## Data sources and AI methods

The training data would come from the records of schools that would participate in the project.
In the attached demo version of the program, a fictitious set of training and testing data is used.
The artificial intelligence methods used in this project are the nearest neighbor method.
The scikit-learn library uses the KNeighborsRegressor algorithm, which is set to the 3 nearest training samples in the demo version.

## Challenges

There is a relatively long period between the initial assessment and the output in the form of a high school diploma. During this period, various changes in the approach and nature of students can occur, and this will of course affect the actual result.
This is a rough estimate and therefore it is necessary to approach the result this way.

## What next?

The growth of the project would be helped by involving schools so that the training data set does not remain just a demo version, but is real.
I would also welcome help with Python programming and project implementation.

## Acknowledgments
