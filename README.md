# Jenkins with Docker and Flask

## generate ssh key for Github and Jenkins
```
ssh-keygen -t rsa
#use public key on github
cat /Users/{User dir}/.ssh/id_rsa.pub
#private key
cat /Users/{User dir}/.ssh/id_rsa
```
* Add pub key to https://github.com/settings/keys

## Repository
* Fork PE02 and add `Jenkinsfile` to the repository (On this example already added to folder)

## Running Jenkins Docker
* Open terminal at `Jenkins` directory to run below command
```
docker-compose up
```
* Default docker Jenkins image does not have docker runnable installed within image. The Dockerfile has script to install docker while building custom Jenkins image.
* Using desktop/jenkins-data as Jenkins-data folder. User can delete it after testing.
* In terminal, the initial password(ex. 65637b52XXXXXXXXXXXXXXXXXXXXXXXX) is shwon to be used during ID/PWD setup on web browser.
* Open localhost:8080 to complete installation along with initial password
* Installed default packages(this also installs Github plugin)


## Jenkins setup
* Make sure Github Jenkins plugin is installed by chechking: Go to “Manage Jenkins” –> “Manage Plugins” –> “Available” Tab –> Search for “GitHub plugin” and "GitHub API Plugin" is installed
* Go to "Available plugins" left top menu -> search for "docker" -> select "Docker Pipeline" and "CloudBees Docker Build and Publish" -> click "Install without restart"
* Setup token at github: https://github.com/settings/tokens/new || https://github.com/settings/tokens > temp token: ghp_ZEYtvB4dSpNPtW5IT1Sue4kwXXXXXXXXXXXX
* Go to “Manage Jenkins” –> “Configure System” –> Locate “Github” section and “Add Github Server” -> Add+ -> "Jenkins" -> Select Kind: "Secret text", and ID: something_unique -> click 'Add' -> popup page closes and select just created secret on "Credentials" -> click "Test Connection" to test -> "save"


## Jenkins job setup
* Reference: https://kevalnagda.github.io/jenkins-git-docker-image
* Edit "Jenkinsfile" > "git([url: 'https://github.com/{repo_name}/{repo_name}.git', branch: 'main', credentialsId: 'Github_ssh_private_key'])" line to match up current project status. URL and credentialsId
* At Dashboard -> "Create a job" -> give name -> "Pipeline" / click "ok" -> "General" / GitHub project check / give URL -> Down at "Build Trigger" section / select "Poll SCM" / input `* * * * *` as a schedule to poll every miniute -> Down at "Pipeline" section / select "Pipeline script from SCM" Definition -> SCM: "GIT" / Repository URL: https://github.com/id/repo.git -> add ssh credential by click "+ Add" / "Jenkins" -> Select Kind: "SSH Username with private key", ID: something_unique, Username: git user name, Private Key: "Enter directly" and paste the private key(ex. cat /Users/{User dir}/.ssh/id_rsa to get private key) -> click "Add" -> popup closes / "Credentials" select id we just created -> change branch from "*/master" to "*/main" -> click "save" in the bottom


## Clean up
```
docker stop jenkins-container
docker rm jenkins-container
```