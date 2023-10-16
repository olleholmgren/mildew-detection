# Cherry Leaf Mildew Detection

* An app for fast and accurate detection of mildew infection made with a machine learning model

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

* The mildew disease is expected to be identified by distinctive white powdery spots on the leaf surface.
* To validate this, cherry leaves with powdery mildew will be compared to healthy cherry leaves.
* The distinction between a healty leaf and a powdery mildew leaf will be carried out by the trained machine learning model with an accuracy of 97%.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

### User Stories

#### Data visualisation

* As a client, I want to be able to showcase the **mean** and **standard deviation** values of healthy cherry leaf images and those affected by powdery mildew. This presentation will enable me to visually distinguish between the two types of leaves.

* As a client, I want to illustrate the distinctions between a typical healthy cherry leaf and one infected by powdery mildew. This demonstration will provide a clear visual differentiation between the two conditions.

* As a client, I would like to create a visual montage featuring both healthy cherry leaves and cherry leaves infected by powdery mildew. This montage will help me distinguish between the two types of cherry leaves.

#### Image classification

* As a client, I want to be able to make a prediction whether a given leaf is healthy or infected.

* As a client, I want to have a machine learning model app to do this prediction for me.

## ML Business Case

* We aim to build a supervised machine learning model for binary classification using the provided image dataset. This model will predict whether a leaf is infected by powdery mildew or not.

* Our aim is to have a minimum of 97% accuracy of the model.

* The objective of this model is to create a swift and dependable diagnostic application that can identify powdery patches on leaves, thus confirming the health status of cherry plants.

* The client is in need, and will benefit of our product because presently, the disease is detected manually, requiring approximately 30 minutes of inspections for each tree. This method is highly time-consuming and lacks scalability.

* The model works as a flag to signify whether a leaf exhibits features indicating tree infection. Plantation staff capture leaf images and upload them to the app, enabling fast, real-time predictions.

## Dashboard Design

To present the project with its hypothesis, summary, visuliser, detector and machine learning model performance, I created a dashboard app using Streamlit.
A very simple and easy-to-use interface containing a side bar with checkboxes to navigate to all pages within the application.

The project pages are presented as following:

#### Page 1: Quick Project Summary

* Summary
  * Powdery mildew, caused by Podosphaera clandestina, affects cherry trees, leading to white powdery spots on leaves and stems, especially on lower leaves. It thrives in high humidity and moderate temperatures, causing significant damage to plants and reducing harvests.

* Business requirements:
  * The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

  * The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

#### Page 2: Leaf Visualizer

* Business requirement 1:

  * The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

* Three checkboxes with the options:
  * Difference between average and variability image
  * Differences between average powdery mildew and average healthy leaves
  * Image Montage

#### Page 3: Mildew Detection

* Business requirement 2:

  * The client is interested in conducting a study to visually differentiate if a given leaf is containing mildew or not.

  * Text paragraph and a link to Kaggle where the dataset is downloaded from
  
  * A file uploader widget designed for uploading images of leaves. Once the user uploads an image, the interface will promptly display the uploaded image along with a statement predicting the health status of the leaf, specifying whether it is healthy or not.

#### Page 4: Project Hypothesis and Validation

* We have reason to believe that leaves infected by powdery mildew exhibit distinct, visible markings. Typically, powdery mildew-infected leaves display white dots scattered across the surface, distinguishing them from healthy leaves.

* To validate this, cherry leaves with powdery mildew will be compared to healthy cherry leaves.

* The distinction between a healty leaf and a powdery mildew leaf will be carried out by a trained machine learning model with an accuracy of 97%.

#### Page 5: ML Performance Metrics

•	Train - healthy: 1472 images

•	Train - powdery_mildew: 1472 images

•	Validation - healthy: 210 images

•	Validation - powdery_mildew: 210 images

•	Test - healthy: 422 images

•	Test - powdery_mildew: 422 images

## Unfixed Bugs

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

### Content

### Media

## Acknowledgements (optional)

* Thank the people that provided support throughout this project.
