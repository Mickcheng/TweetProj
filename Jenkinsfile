pipeline{
	agent any
	stages{
		stage('Build'){
			steps{
				echo 'Building the docker image'
				sh 'docker build -t myapp .'
			}
		}
		stage('Run Container'){
			steps{
				echo 'Run flask app'
				sh 'docker run -d -p 5000:5000 myapp'
			}
		}
		/*stage('Testing'){
			steps{
				sh 'python test_app.py'
			}
		}*/
		stage('Stop Container'){
			steps{
				echo 'Stop flask app'
				sh 'docker container rm -f $(docker container ls -qa)'
			}
		}
	}
}
