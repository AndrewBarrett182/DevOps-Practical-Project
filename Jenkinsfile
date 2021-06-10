pipeline {
    agent any
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
                sh 'docker-compose build'
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