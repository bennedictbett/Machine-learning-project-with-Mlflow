# 🍷 Wine Quality Prediction - End to End ML Project

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MLflow](https://img.shields.io/badge/MLflow-tracking-blue)](https://mlflow.org/)
[![DagsHub](https://img.shields.io/badge/DagsHub-experiment%20tracking-green)](https://dagshub.com/bennedictbett/Machine-learning-project-with-Mlflow)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end machine learning project for predicting wine quality using ElasticNet regression with complete MLflow experiment tracking and DagsHub integration.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Architecture](#project-architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Workflows](#workflows)
- [MLflow & DagsHub](#mlflow--dagshub)
- [AWS Deployment](#aws-deployment)
- [Contributing](#contributing)
- [Author](#author)

## 🎯 Overview

This project demonstrates industry-standard ML engineering practices by implementing a complete machine learning pipeline from data ingestion to model deployment. The project predicts wine quality based on physicochemical properties using ElasticNet regression.

**Key Highlights:**
- Modular and scalable architecture
- Complete experiment tracking with MLflow and DagsHub
- Automated CI/CD pipeline with GitHub Actions
- Docker containerization for easy deployment
- Production-ready AWS deployment

## ✨ Features

- **📊 Modular Pipeline Architecture**: Separate components for each ML workflow stage
- **🔬 MLflow Integration**: Complete experiment tracking, model versioning, and reproducibility
- **🚀 DagsHub Integration**: Remote experiment tracking and team collaboration
- **⚙️ Configuration Management**: YAML-based configuration for easy parameter tuning
- **🐳 Docker Support**: Containerized application for consistent deployments
- **☁️ AWS Deployment**: Production-ready deployment on AWS EC2 with ECR
- **🔄 CI/CD Pipeline**: Automated deployment using GitHub Actions
- **📝 Comprehensive Logging**: Detailed logging throughout the pipeline
- **🔒 Type Safety**: Dataclass-based configuration entities
- **🌐 Web Interface**: Flask-based web app for predictions

## 🏗️ Project Architecture

```
Data Ingestion → Data Validation → Data Transformation → Model Training → Model Evaluation
      ↓               ↓                    ↓                   ↓              ↓
   MLflow         MLflow              MLflow             MLflow        MLflow
      ↓               ↓                    ↓                   ↓              ↓
                            DagsHub Experiment Tracking
```

## 🛠️ Tech Stack

**Core Technologies:**
- **Python 3.8+** - Programming language
- **scikit-learn** - Machine learning algorithms
- **pandas & numpy** - Data manipulation and analysis
- **Flask** - Web framework for API and UI

**MLOps & Tracking:**
- **MLflow** - Experiment tracking and model registry
- **DagsHub** - Remote experiment tracking and collaboration
- **python-box** - Advanced configuration management

**Deployment:**
- **Docker** - Containerization
- **AWS EC2** - Cloud compute
- **AWS ECR** - Container registry
- **GitHub Actions** - CI/CD automation

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- Git
- conda or venv
- (Optional) Docker for containerization

### Quick Start

**1. Clone the repository**
```bash
git clone https://github.com/bennedictbett/Machine-learning-project-with-Mlflow.git
cd Machine-learning-project-with-Mlflow
```

**2. Create and activate virtual environment**

Using conda:
```bash
conda create -n mlproj python=3.8 -y
conda activate mlproj
```

Using venv:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Setup environment variables**

Create a `.env` file in the root directory:
```bash
DAGSHUB_REPO_OWNER=your_dagshub_username
DAGSHUB_REPO_NAME=your_repo_name
MLFLOW_TRACKING_URI=https://dagshub.com/your_username/your_repo.mlflow
```

> ⚠️ **Note**: Never commit your `.env` file! It's already in `.gitignore`

**5. Run the application**
```bash
python app.py
```

Access the web interface at `http://localhost:8080`

## 🚀 Usage

### Training Pipeline

Run the complete training pipeline:
```bash
python main.py
```

This executes all stages:
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Evaluation

### Making Predictions

**Via Web Interface:**
1. Start the Flask app: `python app.py`
2. Navigate to `http://localhost:8080`
3. Enter wine features
4. Get quality prediction

**Via Python API:**
```python
from src.mlProject.pipeline.prediction import PredictionPipeline
import pandas as pd

# Prepare input data
data = {
    'fixed_acidity': 7.4,
    'volatile_acidity': 0.7,
    'citric_acid': 0.0,
    'residual_sugar': 1.9,
    'chlorides': 0.076,
    'free_sulfur_dioxide': 11.0,
    'total_sulfur_dioxide': 34.0,
    'density': 0.9978,
    'pH': 3.51,
    'sulphates': 0.56,
    'alcohol': 9.4
}

df = pd.DataFrame([data])
predictor = PredictionPipeline()
prediction = predictor.predict(df)
print(f"Predicted Quality: {prediction[0]}")
```

## 📁 Project Structure

```
Machine-learning-project-with-Mlflow/
│
├── .github/
│   └── workflows/
│       └── main.yaml              # CI/CD pipeline
│
├── artifacts/                     # Generated artifacts (not in git)
│   ├── data_ingestion/
│   ├── data_validation/
│   ├── data_transformation/
│   └── model_trainer/
│
├── config/
│   ├── config.yaml               # Pipeline configuration
│   ├── params.yaml               # Model hyperparameters
│   └── schema.yaml               # Data schema
│
├── logs/                         # Application logs (not in git)
│
├── research/                     # Jupyter notebooks
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_trainer.ipynb
│   └── 05_model_evaluation.ipynb
│
├── src/mlProject/
│   ├── components/               # Pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── config/
│   │   └── configuration.py      # Configuration manager
│   │
│   ├── entity/
│   │   └── config_entity.py      # Configuration entities
│   │
│   ├── pipeline/
│   │   ├── stage_01_data_ingestion.py
│   │   ├── stage_02_data_validation.py
│   │   ├── stage_03_data_transformation.py
│   │   ├── stage_04_model_trainer.py
│   │   ├── stage_05_model_evaluation.py
│   │   └── prediction.py
│   │
│   ├── utils/
│   │   └── common.py            # Utility functions
│   │
│   └── constants/
│       └── __init__.py          # Project constants
│
├── templates/
│   └── index.html               # Web interface
│
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
├── app.py                       # Flask application
├── Dockerfile                   # Docker configuration
├── main.py                      # Main training pipeline
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup
└── README.md                    # This file
```

## 🔄 Workflows

### Development Workflow

1. **Update Configuration Files**
   - `config.yaml` - Update paths and directories
   - `params.yaml` - Tune model hyperparameters
   - `schema.yaml` - Define data schema

2. **Update Entity Classes**
   - Define configuration dataclasses in `entity/config_entity.py`

3. **Update Configuration Manager**
   - Implement config readers in `config/configuration.py`

4. **Develop Components**
   - Implement pipeline components in `components/`

5. **Create Pipeline Stages**
   - Orchestrate components in `pipeline/`

6. **Update Main Pipeline**
   - Integrate all stages in `main.py`

7. **Update Web Application**
   - Implement prediction endpoint in `app.py`

8. **Test & Deploy**
   - Test locally
   - Build Docker image
   - Deploy to AWS

## 📊 MLflow & DagsHub

### MLflow Local Tracking

Start MLflow UI locally:
```bash
mlflow ui
```
Access at `http://localhost:5000`

### DagsHub Integration

This project uses DagsHub for remote experiment tracking.

**View Experiments:**
🔗 [https://dagshub.com/bennedictbett/Machine-learning-project-with-Mlflow](https://dagshub.com/bennedictbett/Machine-learning-project-with-Mlflow)

**Setup DagsHub:**

1. Create account at [DagsHub](https://dagshub.com/)
2. Fork or create a repository
3. Get your credentials from Remote tab
4. Add to `.env` file:
```bash
DAGSHUB_REPO_OWNER=your_username
DAGSHUB_REPO_NAME=your_repo_name
MLFLOW_TRACKING_URI=https://dagshub.com/your_username/your_repo.mlflow
```

**What's Tracked:**
- Model parameters (alpha, l1_ratio)
- Training metrics (RMSE, MAE, R²)
- Model artifacts
- Dataset versions
- Code versions
- Dependencies

## 🐳 Docker

### Build Docker Image
```bash
docker build -t wine-quality-ml:latest .
```

### Run Container
```bash
docker run -p 8080:8080 wine-quality-ml:latest
```

### Push to Docker Hub
```bash
docker tag wine-quality-ml:latest your-username/wine-quality-ml:latest
docker push your-username/wine-quality-ml:latest
```

## ☁️ AWS Deployment

### Prerequisites
1. AWS Account
2. AWS CLI configured
3. GitHub repository secrets configured

### Deployment Steps

**1. Create IAM User**
- Permissions: `AmazonEC2ContainerRegistryFullAccess`, `AmazonEC2FullAccess`

**2. Create ECR Repository**
```bash
aws ecr create-repository --repository-name ml-wine-quality
```

**3. Create EC2 Instance**
- AMI: Ubuntu 20.04 LTS
- Instance Type: t2.medium or higher
- Security Group: Allow ports 22, 8080

**4. Install Docker on EC2**
```bash
sudo apt-get update -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

**5. Configure GitHub Secrets**

Add these secrets to your GitHub repository:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `AWS_ECR_LOGIN_URI`
- `ECR_REPOSITORY_NAME`

**6. Setup Self-Hosted Runner**
- Go to: Settings → Actions → Runners
- Follow instructions to setup runner on EC2

**7. Push to GitHub**
```bash
git add .
git commit -m "Deploy to AWS"
git push origin main
```

GitHub Actions will automatically:
1. Build Docker image
2. Push to ECR
3. Deploy to EC2
4. Start the application

## 🧪 Testing

### Run Unit Tests
```bash
pytest tests/
```

### Test Components Individually
```python
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

pipeline = DataIngestionTrainingPipeline()
pipeline.main()
```

## 📈 Model Performance

Current ElasticNet model metrics:
- **RMSE**: ~0.65
- **MAE**: ~0.50
- **R² Score**: ~0.35

*These metrics are tracked in MLflow and DagsHub*

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards
- Follow PEP 8 style guide
- Add type hints
- Write docstrings
- Include unit tests
- Update documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Benedict Bett**
- GitHub: [@bennedictbett](https://github.com/bennedictbett)
- Email: benedictbett08@gmail.com
- DagsHub: [@bennedictbett](https://dagshub.com/bennedictbett)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/benedict-bett-a9899038a/)

## 🙏 Acknowledgments

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [DagsHub](https://dagshub.com/) for experiment tracking platform
- [Krish Naik](https://github.com/krishnaik06) for ML project inspiration
- [scikit-learn](https://scikit-learn.org/) team
- Wine Quality Dataset from UCI Machine Learning Repository

## 📚 Resources

- [MLflow Tracking Guide](https://mlflow.org/docs/latest/tracking.html)
- [DagsHub Documentation](https://dagshub.com/docs/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## 🐛 Known Issues

- None currently. Please report issues [here](https://github.com/bennedictbett/Machine-learning-project-with-Mlflow/issues)

## 🗺️ Roadmap

- [ ] Add support for multiple ML algorithms (Random Forest, XGBoost)
- [ ] Implement hyperparameter tuning with Optuna
- [ ] Add model interpretability with SHAP
- [ ] Create REST API with FastAPI
- [ ] Add data versioning with DVC
- [ ] Implement A/B testing framework
- [ ] Add monitoring and alerting
- [ ] Create comprehensive unit tests
- [ ] Add integration tests
- [ ] Implement model retraining pipeline

## 📞 Support

For support and questions:
- 📧 Email: benedictbett08@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/bennedictbett/Machine-learning-project-with-Mlflow/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/bennedictbett/Machine-learning-project-with-Mlflow/discussions)

---

<div align="center">

**Made with ❤️ by Benedict Bett**

</div>
