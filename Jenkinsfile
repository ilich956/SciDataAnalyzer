pipeline {
    agent any

    // Poll GitHub every minute: every new commit starts a build
    triggers {
        pollSCM('* * * * *')
    }

    environment {
        IMAGE_NAME = 'scidataanalyzer'
        IMAGE_TAG  = "${env.BUILD_NUMBER}"
    }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --oneline'
            }
        }

        stage('Install Dependencies') {
            agent {
                docker {
                    image 'python:3.10-slim'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Unit Tests') {
            agent {
                docker {
                    image 'python:3.10-slim'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    . venv/bin/activate
                    pytest test_analyzer.py -v --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG -t $IMAGE_NAME:latest .'
            }
        }

        stage('Smoke Test Image') {
            steps {
                sh 'docker run --rm $IMAGE_NAME:$IMAGE_TAG'
                sh 'docker run --rm $IMAGE_NAME:$IMAGE_TAG pytest test_analyzer.py -q'
            }
        }
    }

    post {
        success {
            echo "Image ${IMAGE_NAME}:${IMAGE_TAG} built and tested successfully."
        }
        failure {
            echo 'Pipeline failed. Check the stage logs above.'
        }
    }
}
