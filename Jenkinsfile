pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
        install = 'true'
    }
    stages {
        stage('Install Requirements') {
            steps {
                script {
                    if (env.install == 'true'){
                        sh 'bash jenkins/install-requirements.sh'
                    }
                }    
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
                sh 'cd ansible && ~/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo deploy'
            }
        }
    }
}