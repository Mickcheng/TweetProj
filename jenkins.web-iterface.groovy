def build_app(){
  sh 'docker build -t myflaskapp .'
  }

def user_acceptance(){
  }

def e2e_test(){
  }

def test_app(){
  sh 'docker run -d -p 5000:5000 myflaskapp'
  }

def down_app(){
  }

def release_app(){
  }
  
def live_app(){
  }

return this
