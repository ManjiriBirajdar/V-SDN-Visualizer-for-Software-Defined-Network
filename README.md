# V-SDN : Visualizer for Software Defined Network

#### Manjiri Birajdar and Marius Faust, TU Darmstadt

We present ”V-SDN”, an interactive web based application for visualizing the Software Defined Network (SDN). 

It includes a backend for processing the client requests based on Flask - a python based web framework including [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) extension for quickly building REST APIs. 

The frontend is built as a web interface based on HTML, CSS, JavaScript library [D3.js](https://d3js.org/). It is built on the [Force-Directed Graph](https://observablehq.com/@d3/force-directed-graph) example. 

The application is capable of displaying network topology with additional node information. We also provide generic REST APIs to interact and build new visualizations.

## Getting Started

### Prerequisites

1. Python 3.7.3

2. Flask

3. Pip

4. virtual environment :  venv

### Installing

#### Python 3.7.3

Use [Python official website](https://www.python.org/downloads/)  for further installation steps as per operating system

#### Flask

```
pip install flask
```

#### venv : virtual environment

```
python -m venv venv
```

## Deployment

Open command prompt and go to the project folder. Go inside the folder using cd

Then run following commands to deply it on server (on windows):

```
set FLASK_APP=v_sdn_visualizer.py

flask fun
```

OR
```
python v_sdn_visualizer.py
```

Then following text will be shown:

```
* Serving Flask app "v_sdn_visualizer.py"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Then open 

```
"http://127.0.0.1:5000/"
```

and you will see black page with heading of project.

Then, now you can create the network you want! Example is given below.

Run the "curl_commands.bat" file using. It contains curl commands to create a network.

The detailed API documentation can be found here : https://docs.google.com/document/d/1HgtIsek_ZMdKP7jtpXRcej4tKfOS2QAHtjDv18b0_Zg/edit#heading=h.pev1tk7dc5pa


Also, there some examples for using curl commands.
