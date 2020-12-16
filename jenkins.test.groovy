def build_app(){
  sh 'docker build -t myflaskapp .'
  }

def user_acceptance(){
  }

def e2e_test(){
  }

def test_app(){
  sh 'python test_app.py'
  }

def down_app(){
  sh 'docker rm -f $(docker container ls -qa)'
  }

def release_app(){
  }
  
def live_app(){
  }

return this
