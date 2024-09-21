# Learning Hope Mini Project
### Funding the future, One Project at a time

#### DonorsChoose.org
DonorsChoose stands at the forefront of transforming educational landscapes by providing a unique crowdfunding platform that bridges the gap between passionate teachers and generous donors. Founded in 2000 by Charles Best, a former Bronx public school teacher, the organization has become a beacon of hope for educators seeking to enhance the learning experiences of their students.

The platform operates on a simple yet powerful premise: teachers create project proposals outlining the resources they need, ranging from essential classroom supplies to innovative educational tools. These proposals are then featured on the DonorsChoose website, where potential donors—ranging from individuals and corporations to philanthropic organizations—can pursue projects aligned with their interests and values.

#### Business Problem
DonorsChoose faces the challenge of efficiently predicting the approval status of project proposals submitted by teachers. The current manual review process is time-consuming and may not harness the full potential of available data. To address this, the business problem is to implement a machine learning solution that can accurately predict whether a project will be approved or not based on various project-related features.

#### Key Business Objectives
- Automate Approval Prediction: Use technology to predict whether a given project proposal is likely to be approved.

- Reduce Processing Time: Implementing a predictive model will significantly reduce the time required for manual project review, enabling quicker responses to teachers and enhancing overall operational efficiency.
Improve Decision-Making: Provide decision-makers at DonorsChoose with a data-driven tool to assess the likelihood of project success, allowing for more informed and objective project approval decisions.

- Enhance User Experience: Create a more streamlined and responsive experience for teachers submitting projects by reducing uncertainty and providing timely feedback on the likelihood of their project being approved.

- Optimize Resource Allocation: Direct resources more effectively by focusing attention on projects with a higher predicted probability of approval, thereby increasing the success rate of funded projects on the platform.

#### Machine Learning Problem

The primary objective of this machine learning project is to develop a predictive model that can accurately forecast the approval status of project proposals submitted on the DonorsChoose platform. Leveraging historical data and key project features, the challenge is to implement a classification algorithm that distinguishes between projects likely to be approved and those likely to be rejected.

#### Technical Objectives
- Data Collection and Exploration: Gather and explore the dataset containing historical information on DonorsChoose project proposals, encompassing features such as project descriptions, resource needs, teacher information, and past approval outcomes.

- Feature Engineering: Identify and create relevant features that significantly influence the project approval decision. This may involve extracting insights from project descriptions, analyzing historical approval patterns, and incorporating metadata related to teachers and schools.

- Model Selection: Evaluate and select appropriate machine learning classification algorithms for predicting project approval status. Consideration should be given to factors such as interpretability, accuracy, and the ability to handle imbalanced datasets.

- Training and Validation: Train the selected model using the historical dataset, employing validation techniques to ensure robust performance and the avoidance of overfitting.

- Hyperparameter Tuning: Optimize the model's hyperparameters to achieve the best possible predictive accuracy while maintaining generalizability to new project proposals.

- Evaluation Metrics: Assess the model's performance using relevant metrics such as precision, recall, and F1-score, considering the specific business context of project approval prediction.

#### About the Dataset
The dataset provided for this machine learning project encompasses a comprehensive collection of historical information related to project proposals on the DonorsChoose platform. Each entry in the dataset represents a unique project proposal submitted by educators seeking support for their initiatives. The dataset includes a variety of features that capture crucial aspects of these proposals, teacher details, and contextual information.

#### Download link
The dataset can be downloaded from here
You can download the dataset in your environment using the following code.
```
zip_url = "https://drive.google.com/uc?export=download&id=1KrnpfYRKVxGDnj-R2VZmNscEkR1zr2-4"

dataset_path = os.path.join("./dataset", "donors_choose")
zip_file_path = os.path.join(dataset_path, "donors_choose_dataset.zip")

if not os.path.exists(dataset_path):
  os.makedirs(dataset_path)

if not os.path.exists(zip_file_path):
   gdown.download(zip_url, zip_file_path, quiet=False)

with zipfile.ZipFile(zip_file_path ,"r") as zip_ref:
    zip_ref.extractall(dataset_path)
```

#### Dataset Size and Format
The size of the dataset is about 100k, with each record containing information about a specific project proposal. The data is organized in a structured format, allowing for efficient analysis and model training.
Since the size of the dataset is too large, you may choose to work with a subset of the data in case the training takes too long or you run into memory issues.

#### Deliverables/Evaluation Parameters
You need to prepare a Jupyter Notebook consisting of the following:

#### Details of the Dataset:
Compile a comprehensive overview detailing dataset specifications including size, features, target variables, and data types to establish a foundational understanding of the dataset's structure and context.

#### Exploratory Data Analysis: 
Conduct statistical analyses and visual examinations to uncover patterns, anomalies, and relationships within the dataset. Document findings to inform subsequent modeling decisions.

#### Data Processing, Feature Engineering, and Vectorization: 
Implement preprocessing techniques such as handling missing data, encoding categorical variables, and scaling numerical features. Engage in feature engineering to create predictive features and transform data into a suitable format for model training.

#### Model Training and Hyperparameter Search: 
Select and train machine learning models on the processed dataset. Employ hyperparameter optimization techniques to fine-tune model performance, striving for optimal predictive accuracy.

#### Model Evaluation: 
Assess the performance of trained models using appropriate metrics and validation techniques. Ensure robustness and generalization capability by evaluating models on unseen data.

#### Result Analysis/Future Work: 
Analyze model evaluation results to identify strengths, weaknesses, and areas for improvement. Use insights gained to inform decision-making processes and potentially refine models through iterative iterations.

#### Important Note:
This project will require you to delve into data preprocessing, including some text processing techniques. While this goes beyond what we've covered in the classes so far, we've provided additional resources, including videos and code samples, to help you grasp the basics of text processing.

If you decide to undertake this project, please be prepared to invest extra effort to learn these new concepts. Your dedication to mastering this material will significantly enhance your skills and understanding of machine learning. We will also be covering these concepts later in the program during the NLP classes.

### Duration
![Duration Breakdown](./images/Duration.png)

