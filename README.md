# CrowdNav

![Banner](https://raw.githubusercontent.com/Starofall/CrowdNav/master/banner.PNG)


### Description
CrowdNav is a simulation based on SUMO and TraCI that implements a custom router
that can be configured using kafka messages or local JSON config on the fly while the simulation is running.
Also runtime data is send to a kafka queue to allow stream processing and logger locally to CSV.

## Dependencies
* Docker
* Docker Compose

### Setup
* Download the CrowdNav code
* Run `docker compose up -d`  to run all the images (CrowdNav, Kafka, API) in detached mode

## Folder structure
* **api**: This contains the HTTP Server which is implemented using FastAPI
* **crowdnav**: This contains CrowdNav

### Getting Started Guide
A first guide on how to use (i.e. adapt, measure, optimize) CrowdNav with the [RTX tool](https://github.com/Starofall/RTX) is available at this [Wiki page](https://github.com/Starofall/RTX/wiki/RTX-&-CrowdNav-Getting-Started-Guide). 

### Operational Modes

* Normal mode (`python run.py`) with UI to Debug the application. Runs forever.
* Parallel mode (`python parallel.py n`) to let n processes of SUMO spawn for faster data generation.
  Stops after 10k ticks and reports values.
  
### Further customization

* Runtime variables are in the knobs.json file and will only be used if `kafkaUpdates = True
` is set to false in `Config.py`. Else the tool uses Kafka for value changes.
* To disable the UI in normal mode, change the `sumoUseGUI = True` value in `Config.py` to false.

### Notes

* To let the system stabilize, no message is sent to kafka or CSV in the first 1000 ticks .

* Errors of the form "Error: Answered with error to command 0xc4: Route replacement failed for car-356" are internal sumo errors that are not of our concern as of now. See this thread for details
https://github.com/eclipse-sumo/sumo/issues/6996 
