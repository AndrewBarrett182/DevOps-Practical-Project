pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                // run test script
                sh 'bash jenkins/test.sh'
            }
        }
        stage('Build') {
            steps {
                sh 'echo build'
            }
        }
        stage('Push') {
            steps {
                sh 'echo push'
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