# EOS AI Trainer 
🤖 Eos - Enhanced Orienting Space - AI enhanced space to help supported employment coaches to provide interactive trainings and information for visually impared individuals, enhanced by Microsoft Azure AI Services and cloud infraestructure.

In the ever-evolving landscape of manufacturing, inclusivity and accessibility and Supported employment are paramount. Our software is at the forefront of this movement, designed specifically to revolutionize the way visually impaired individuals work at manufacturing assembly sites. By integrating LLM, advanced voice recognition and custom vision technologies, we are breaking new ground in creating a more inclusive and efficient work environment.

**Goals:**

🟢 **Inclusion and Equality:** Our primary goal is to create a more inclusive workplace where visually impaired individuals have equal opportunities to contribute and excel in manufacturing roles.

🟢 **Innovation in Assistive Technology:** We aim to push the boundaries of what is possible with assistive technologies, continually enhancing our software to meet the evolving needs of users.

## Topics

- [Project description](#eos-ai-trainer)
- [How does it work?](#how-does-it-work)
- [Used Tools](#used-tools)
- [Cloud Architecture](#cloud-architecture)
- [Demo](#demo)


## How does it work

### There are two key components. 

### Enhanced Assembly Workspace: 
This area will help and guide the individual to receive the appropriate training on how to assemble a manufactured product.  

*(For this demonstration we will simulate an automotive manufacturing assembly site.)*

The user sits in front of a desk with the necessary pieces to complete the assembly, in front of the individual there is a physical action button. At the top of the desktop there is a camera system pointing to the workspace covering the overhead plane. 

Once the training starts EOS will provide the description of each piece to the user by implementing natural conversation techniques and text to speech services. 

EOS will guide the user through the precise steps on the assembly, after each step on the assembly user will be required to place the piece on the validation space and interact with the system through the action button, this will trigger the Vision Validation, which will validate the correct progress of the assembly and enable the next step description and guidance.  

Additionally, EOS will function as an interactive agent enhanced with LLM’s to provide the user with information regarding the current training, the end goal of manufactured pieces, the industry, tracking current progress, among other utilities. 

To illustrate this concept is the following diagram, which describes the key elements of the training station, it’s important to highlight that the user will be receiving audio feedback at all moments through the usage of headphones or speakers. 

![workstation concept](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/eos_workstation_concept.JPG "Workstation Concept")

### Trainer administration portal 

This will be the configuration and administration element of the solution, developed to help supported employment coaches to launch and configure the different trainings, track the progress of users and tweak the system behavior.  

## Used Tools

<table style="text-align:center">
    <tr>
        <td><b>Tool</b></td>
        <td><b>Description</b></td>
    </tr>
    <tr>
        <td>
            Azure AI Foundry
        </td>
        <td>
            Azure AI Foundry is a platform for building, managing, and deploying AI applications. It provides a unified interface for AI developers and data scientists. This project implement LLM functionality, Speech services, Custom Vision from Azure AI Foundry services. 
        </td>
    </tr>
    <tr>
        <td>
           <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white"> 
        </td>
        <td>
            The REST services and administration backend is developed around the node.js environment. 
        </td>
    </tr>
     </tr>
       <tr>
        <td>
            <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
        </td>
        <td>
            Python is used in this project to create the edge scripts at the enhanced workspace station. 
        </td>
    </tr>
    <tr>
        <td>
            <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white">
        </td>
        <td>
            MongoDB is a document database used to build highly available and scalable internet applications. This technology will store user data and progress as well as the training information and configuration.
        </td>
    <tr>
        <td>
            <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
        </td>
        <td>
            GitHub is a code hosting platform for version control and collaboration.
        </td>
    </tr>
</table>

## Cloud Architecture
- The following diagram describes the end-goal architecture of this project which will allow scalability and reliability

![cloud architecture diagram](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/EOS_Azure_Arch.png "Cloud Architecture")


## Demo

### Trainer administration portal

The web application for managing workouts consists of a login and a dashboard, which displays the workouts that have been created, their progress, and execution status. You can also start a new workout and view the one currently running.

First you must authenticate with a login, which will take you to the administration dashboard:

![Frontend Login](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/1-login.png "Frontend")
![Frontend Login](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/2-login.png "Frontend")

Below are images of the dashboard:

![Frontend Dashboard](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/3-dashboard.png "Frontend")

You can select a new workout, which should only be started if no other workout is currently running.

![Frontend Dashboard](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/4-dashboard.png "Frontend")

You can view the current workout and stop it. In the list of created workouts, you can view their information and start or stop them.

![Fronten Dashboard](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/5-dashboard.png "Frontend")

In the following three images you can see that the list of workouts can be filtered by: 
- The number of the workout created (example: 1).

![Frontend Dashboard](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/6-dashboard.png "Frontend")

- The number of the workout (example: "train 2").

![Frontend Dashboard](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/7-dashboard.png "Frontend")

- The name of the workout (example: Assembly A96).

![Frontend Dashboard](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/8-dashboard.png "Frontend")

### Trainer Station
To simulate the assembly of an automotive piece we designed, and 3D printed a small set of pieces, the core piece, a millimetric bolt and the matching nut. 

To simulate the assembly of an automotive component, we designed and 3D printed a set of pieces, including the core piece (A), a millimetric bolt (B), and the matching nut (C). Each piece was painted in different colors to enable our custom computer to easily identify them. 

![Training station demo](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/eos_workstation_concept_2.JPG "Training station demo")

Our Enhanced Orienting Space will provide comprehensive guidance to the user. Initially, EOS will speak to the user, first by presenting industrial safety recommendations to ensure user safety. Following this, EOS will introduce the training session, starting by helping the user to familiarize themselves with each assembly piece. 

Once the user confirms their familiarity with the various pieces, EOS will start the training by offering step-by-step guidance. Utilizing advanced computer vision technology, EOS will verify if the user correctly assembles the piece.This technology offers substantial assistance to visually impaired individuals in performing assembly tasks within manufacturing environments. 

This validation is performed using a trained custom vision model, which can accurately identify whether a piece is disassembled, partially assembled, or fully assembled.

![Training custom vision](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/training_custom_vision.JPG" Training custom vision")

For demonstration purposes, and to simulate a physical action button, we created a graphical user interface that enables the user to provide feedback to the system by clicking the mouse. Ideally, this would be replaced with a physical button featuring haptic feedback. 

Furthermore, the system is potentiated with a Large Language Model (LLM) that provides users with useful information regarding the current process. This integration ensures that users receive real-time insights and detailed explanations, enhancing their understanding and efficiency during the assembly tasks. 