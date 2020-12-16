def groovyfile

pipeline{
	agent any
	parameters{
		choice(
			choices:['yes', 'no']
			description: 'Response to the acceptance test'
			name:'RESPONSE'
			)
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
		when{
			expression{ params.RESPONSE == 'yes'}
		}
		stage('Creating Release branch'){
			steps{
				script{
					groovyfile.release_app()
				}
			}
		}
		stage('Going live'){
			steps{
				script{
					groovyfile.live_app()
				}
			}
		}
	}
}
