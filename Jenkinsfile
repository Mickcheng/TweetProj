def groovyfile
def resp

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
		if (resp == 'yes'):
			stage('Going live'){
				steps{
					script{
						groovyfile.live_app()
					}
				}
			}
		else: pass
	}
}
