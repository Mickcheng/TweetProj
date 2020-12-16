def build_app(){
  //sh 'docker-compose up -d'
  sh 'docker build -t myapp .'
  sh 'docker run -d -p 5000:5000 myapp'
  }
  
def test_app(){
  //sh 'python test_app.py'
  }

def down_app(){
  //sh 'docker-compose down'
  sh 'docker rm -f $(docker container ls -qa)
  }

def release_app(){
  echo 'branch into release'
  }
  
def live_app(){
  }

return this
