def groovyfile
pipeline{
	agent any
	stages{
		stage('Build script'){
			steps{
				script{
					filename = 'jenkins.' + env.BRANCH_NAME + '.groovy'
					groovyfile = load filename
				}
			}
		}
		stage('Build Flask app'){
			steps{
				script{
					echo 'Building the docker image'
					groovyfile.build_app()
				}
			}
		}
		stage('Run Flask app'){
			steps{
				script{
					echo 'Running the docker image'
					groovyfile.run_app()
				}
			}
		}
		stage('Testing'){
			steps{
				script{
					groovy.test_app()
				}
			}
		}
		stage('Docker images down'){
			steps{
				script{
					groovy.down_app()
				}
			}
		}
		stage('Creating Release branch'){
			steps{
				script{
					groovy.release_app()
				}
			}
		}
		stage('Going live'){
			steps{
				script{
					groovy.live_app()
				}
			}
		}
	}
}
