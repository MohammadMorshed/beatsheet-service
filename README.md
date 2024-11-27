# BeatSheetService
Allows creators to structure their content into a "beat sheet," a storytelling tool used to outline various
elements like scenes, dialogues, or musical cues.

# Supported APIs 
**To access live api specs, visit:** http://localhost:8000/docs

## BeatSheets
* GET: /beatsheet/ - Get All Beatsheets
* POST /beatsheet/ - Create Beatsheet
* GET /beatsheet/{id} - Get Beatsheet
* PUT /beatsheet/{id} - Update Beatsheet
* DELETE /beatsheet/{id} - Delete Beatsheet

## Beats
* GET /beatsheet/{beatsheet_id}/beat/ - Get Beats
* POST /beatsheet/{beatsheet_id}/beat/ - Create Beat
* GET /beatsheet/{beatsheet_id}/beat/{beat_id} - Get Beat
* PUT /beatsheet/{beatsheet_id}/beat/{beat_id} - Update Beat
* DELETE /beatsheet/{beatsheet_id}/beat/{beat_id} - Delete Beat

## Acts
* GET /beatsheet/{beatsheet_id}/beat/{beat_id}/act/ - Get Acts
* POST /beatsheet/{beatsheet_id}/beat/{beat_id}/act/ - Create Act
* GET /beatsheet/{beatsheet_id}/beat/{beat_id}/act/{act_id} - Get Act
* PUT /beatsheet/{beatsheet_id}/beat/{beat_id}/act/{act_id} - Update Act
* DELETE /beatsheet/{beatsheet_id}/beat/{beat_id}/act/{act_id} - Delete Act
* POST /beatsheet/{beatsheet_id}/beat/{beat_id}/act/suggest-next - Suggest Next act
* POST /beatsheet/{beatsheet_id}/beat/{beat_id}/act/suggest - Suggest multiple next acts

# Docs

Under docs folder
* beat_service_postman_collection.json - Postman Collection for manual API testing.
* open-api.json - OpenAPI Specification (static copy). To access live go to 
this url after the service is up and running: http://localhost:8000/docs 


### **Deploy local with docker-compose:**

From project root directory: <br>
* `docker-compose up --build`

After deploying the service you can access it at http://localhost:8000 and find the api docs at http://localhost:8000/docs


## Project structure 

* app - main python module
  * api - FastAPI modules
  * data - database config, models and data schemas
  * service - Service modules    
  * repository - Repository modules
* tests - Test modules
* config - Configuration modules
* init.sql - SQL init script for database setup
* requirements.txt - Python dependencies
* dockerfile - Dockerfile
* docker-compose.yml - Docker Compose file for local deployment
* README.md - this file

#### Simple AI model - next_act_predictor.py
* Markov Chain Basics: The model uses a transition matrix (self.transitions) to record the frequency of transitions between acts in the training data.
* Training: Each sequence of acts updates the transition matrix to capture the likelihood of moving from one act to the next.
* Prediction: Given a current act, the model predicts the next act by sampling from the weighted probabilities in the transition matrix.
* Suggestions:The suggest_sequence method predicts multiple subsequent acts by chaining predictions.
* config.py - Contains training data that gets loaded into the model during initialization.


## -------------------------------------------

# Untested Functionalities (Work in Progress)

### **Deploy Infrastructure with Terraform:**
Files: main.tf 

From project root directory: <br> 
* `terraform init` 
* `terraform plan`
* `terraform apply`

#### **Deploy Application to Kubernetes:**
Files: deployment.yaml, service.yaml, secrets.yaml 

* `kubectl apply -f deployment.yaml`  
* `kubectl apply -f service.yaml`

#### **Run the CI/CD Pipeline:**
Files: .github/workflows/main.yml

Push the code to GitHub and ensure secrets (`DOCKER_USERNAME`, `DOCKER_PASSWORD`) are set in repository settings.

