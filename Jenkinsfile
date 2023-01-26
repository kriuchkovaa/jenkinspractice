pipeline {
    environment {
        imagename = "ailari2407/jenkinspractice"
        registryCredential = "jenkins_docker"
        dockerimage = ''
    }
    agent any 
    stages {
        stage('Cloning Git') {
            steps {
                git([url: 'https://github.com/kriuchkovaa/jenkinspractice.git', branch: 'main', credentialsId: 'jenk_github_ssh'])
            }
        }
        stage('Building Image') {
            steps {
                script {
                    dockerImage = docker.build imagename 
                }
            }
        }
        stage('Deploy Image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Remove unused docker image') {
            steps {
                sh "docker rmi $imagename:$BUILD_NUMBER"
                sh "docker rmi $imagename:latest"
            }
        }
    }
}