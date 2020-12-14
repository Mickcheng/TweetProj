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
				sh 'docker run -d -p 5000:5000 --name myapp_c myapp'
			}
		}
		stage('Testing'){
			steps{
				sh 'python test_app.py'
			}
		}
		stage('Stop Container'){
			steps{
				sh 'docker rm -f myapp_c'
			}
		}
	}
}