pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
    }
    stages {
        stage('Install Requirements') {
            steps {
                sh 'bash jenkins/install-requirements.sh'
            }
        }
        stage('Test') {
            steps {
                sh 'bash jenkins/test.sh'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose build --parallel'
            }
        }
        stage('Push') {
            steps {
                sh 'docker-compose push'
            }
        }
        stage('Ansible') {
            steps {
                sh 'echo ansible'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo deploy'
            }
        }
    }
}