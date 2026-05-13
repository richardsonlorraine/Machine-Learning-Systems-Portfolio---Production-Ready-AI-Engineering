Project 3 — Production Machine Learning Model Deployment System
Highlights: REST API, Docker containerisation and Kubernetes deployment
Tech: Docker and Azure Kubernetes Service

3.1 Introduction This chapter presents the design and implementation of a production-grade machine learning deployment system, enabling trained models to be served reliably in real-time environments. The system is designed to address key challenges in deploying ML models, including:
environment consistency, scalability, reliability and observability
The architecture integrates containerisation, cloud orchestration, and automated CI/CD pipelines to support enterprise-level deployment workflows.

3.2 System Overview The deployment system follows a modular MLOps architecture:
Trained Model -> Inference API -> Containerisation (Docker) -> Orchestration (AKS) -> Client Requests → Predictions
This separation of concerns ensures scalability and maintainability across environments.

3.3 Design Constraints and Objectives The system was engineered to satisfy the following requirements:

3.3.1 Portability Ensures consistent execution across environments using Docker containers.

3.3.2 Scalability Supports horizontal scaling through Azure Kubernetes Service.

3.3.3 Resilience Implements:
health checks, rolling updates, blue/green deployment strategies to minimise downtime.

3.3.4 Efficiency Optimises inference latency through:
lightweight containers
model compression / quantisation

3.4 Inference API System

3.4.1 Objective To expose the trained model as a RESTful service for real-time predictions.

3.4.2 Architecture Client Request → API Endpoint → Model → Prediction → Response

3.4.3 Implementation The inference API was implemented using a lightweight web framework.
from flask import Flask, request, jsonify
import joblib
app = Flask(__name__)
model = joblib.load('iris_model.pkl')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        prediction = model.predict([data['features']])
        return jsonify({'status': 'success', 'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

3.4.4 Technical Analysis
Model is loaded into memory for low-latency inference
API handles structured JSON input
Exception handling ensures robustness

3.4.5 Results
Inference latency (P99): ~150ms
Response format: JSON
Error handling: Implemented

3.4.6 Evaluation The API enables real-time inference with low latency and structured communication. However, performance may degrade under high traffic without scaling.

3.4.7 Engineering Considerations
stateless API design for scalability
input validation required for production
concurrency handling under load

3.5 Containerisation System

3.5.1 Objective To ensure reproducible and portable deployment environments.

3.5.2 Architecture Application Code + Dependencies → Docker Image → Deployment

3.5.3 Implementation
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY model.pkl .
COPY app.py .
EXPOSE 80
CMD ["python", "app.py"]

3.5.4 Technical Analysis
lightweight base image reduces size
dependency pinning ensures consistency
container acts as immutable deployment unit

3.5.5 Results
Image size: Optimised
Deployment reproducibility: High

3.5.6 Evaluation Containerisation eliminates environment mismatch and simplifies deployment workflows.

3.5.7 Engineering Considerations
image size impacts deployment speed
security vulnerabilities must be managed
dependency updates require rebuilds

3.6 Orchestration and Cloud Deployment

3.6.1 Objective To enable scalable and resilient deployment in cloud environments.

3.6.2 Architecture Docker Image → Azure Container Registry → AKS Cluster → Load Balancer

3.6.3 Implementation Deployment uses:
Azure Container Instances (testing)
Azure Kubernetes Service (production)

3.6.4 Technical Analysis
AKS manages scaling and load balancing
ACR stores versioned container images
deployments are automated via CI/CD pipelines

3.6.5 Results
Deployment time: < 15 minutes
Auto-scaling: Enabled
High availability: Achieved

3.6.6 Evaluation Cloud orchestration enables robust, scalable deployment but introduces operational complexity.

3.6.7 Engineering Considerations
cluster configuration impacts cost
scaling policies must be tuned
monitoring is required for stability

3.7 CI/CD Pipeline

3.7.1 Objective To automate the build, testing, and deployment process.

3.7.2 Pipeline Flow Code Commit → Build → Test → Deploy

3.7.3 Implementation
Docker images built on commit
automated validation checks
deployment triggered on successful tests

3.7.4 Evaluation CI/CD improves:
deployment speed
reliability
consistency

3.8 Monitoring and Performance Metrics

3.8.1 Objective To track system performance and detect failures.

3.8.2 Metrics
Latency (P99): < 200ms
Deployment Time: < 15 mins
Data Drift Threshold: >10%
Quantisation Ratio: 4:1

3.8.3 Evaluation Monitoring ensures:
system reliability
early failure detection
performance optimisation

3.9 Repository Structure
03_model_deployment_system
├── api/
├── docker/
├── deployment/
├── model_registry/
└── README.md

3.10 Implemented System Summary
Built REST API for model inference
Containerised application using Docker
Deployed system using Azure Kubernetes Service
Implemented CI/CD pipeline for automated deployment
Monitored performance using latency and drift metrics
3.11 Conclusion This chapter demonstrated the implementation of a production-grade ML deployment system. The system highlights:
the importance of containerisation and orchestration
the role of CI/CD in automation
the need for monitoring in production environments
These components are essential for transitioning machine learning models from experimentation to real-world deployment.
