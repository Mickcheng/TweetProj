def groovyfile

pipeline{
	agent any
	parameters{
		choice(
			choices:['yes', 'no'],
			description: 'Response to the acceptance test',
			name:'RESPONSE'
			)
	}
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
					groovyfile.build_app()
				}
			}
		}
		stage('Testing'){
			steps{
				script{
					resp = groovyfile.test_app()
				}
			}
		}
		stage('Docker images down'){
			steps{
				script{
					groovyfile.down_app()
				}
			}
		}
		stage('Creating Release branch'){
			steps{
				script{
					groovyfile.release_app()
				}
			}
		}
		stage('Going live'){
			if (params.RESPONSE == 'yes'){
				groovyfile.live_app()
			}
			else {
				echo 'Acceptance test failed'
			}
			/*when{
				expression{ params.RESPONSE == 'yes'}
			}
			steps{
				script{
					groovyfile.live_app()
				}
			}
			when{
				expression{ params.RESPONSE == 'no'}
			}
			steps{
				script{
					echo 'Acceptance test failed.'
				}
			}*/
		}
	}
}
