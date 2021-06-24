node(''){
	stage('Preparation'){
		echo "Starting git clone"
		git branch: 'main', url: 'https://github.com/Sanjay2311/currency_exchnage.git' 
	}
	stage('Build docker image'){
		docker.withRegistry('', docker-hub){
		app = docker.build("sanjay23/currency_exchange")
		app.push('main')
		}
	}
}
