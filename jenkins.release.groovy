def build_app(){
  sh 'docker-compose up -d'
  }
def user_acceptance(){
  input 'Proceed with deployment to live?'
  }
def e2e_test(){
  echo 'test test'
  }
def test_app(){
  e2e_test()
  user_acceptance()
  }

def down_app(){
  sh 'docker-compose down'
  }

def release_app(){
  }
  
def live_app(){
  echo 'merge to master'
  }

return this
