# EOS AI Trainer 
🤖 Eos - Enhanced Orienting Space - AI enhanced space to help supported employment coaches to provide interactive trainings and informations for visually impared individuals, enhanced by Microsoft Azure AI Services and clound infraestructure.

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
![cloud architecture diagram](https://raw.githubusercontent.com/JustZeus/eos-ai-trainer/main/img/EOS_Azure_Arch.png "Cloud Architecture")

## Demo