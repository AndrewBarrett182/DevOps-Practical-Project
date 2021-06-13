# DevOps Fundamental Project - Lottery

## Contents

- [Brief](#brief)
  - [Additional Requirements](#additional-requirements)
  - [My Approach](#my-approach)
- [Architecture](#architecture)
  - [Database Structure](#database-structure)
  - [CI Pipeline](#ci-pipeline)
- [Project Tracking](#project-tracking)
- [Risk Assessment](#risk-assessment)
- [Testing](#testing)
  - [Instructions to run Unit Testing](#instructions-to-run-unit-testing)
  - [Instructions to run Integration Testing](#instructions-to-run-integration-testing)
- [Front-End Design](#front-end-design)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [Author](#author)

## Brief

The overall objective for this project is:

> - To create an application that generates "Objects" upon a set of predefined rules using a service-orientated architecture composing of at least 4 services that work together.

This is to demonstrate my capability with the technologies and concepts I have been taught and assessing my development against the SFIA framework. 

### Additional Requirements

A list of the scope/requirements of this project are as follows:

> - An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project. This could also provide a record of any issues or risks that you faced creating your project.
>
> - An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
>
> - If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application.
>
> - The project must follow the Service-oriented architecture that has been asked for.
>
> - The project must be deployed using containerisation and an orchestration tool.
>
> - As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
>
> - The project must make use of a reverse proxy to make your application accessible to the user.

### My Approach

For my project, I decided to create an application for a simple lottery which consists of:

- Service #1

  The core service that renders a Jinja2 template to establish interaction with the application. This is also responsible for the communication between the other 3 services. Data generated is stored into a MySQL database.

- Service #2 + #3

  These are the services that generate a list of random numbers which correspond to a lottery ticket purchased along with the winning numbers for that draw.

- Service #4

  This is the service that creates an object depending on the results of services #2 and #3. The prize determination for the draw is determined here.

- Different Implementations

  Two different implementations were created for the services one of which include more numbers that can be drawn from therefore having increased prize winnings due to the lower odds of getting a match. Also, this second implementation includes showing 10 instances within the database at a time rather than 5 in the first implementation as well as a background colour change. This is so that the rolling update of the application can be seen clearly to the user.

## Architecture

### Database Structure

The database structure for the project is displayed using an Entity Relationship Diagram (ERD). This diagram displays the design of the table associated with the database.

![image](https://user-images.githubusercontent.com/82821693/121809180-b1aa1e00-cc53-11eb-9255-02c4861b2cea.png)

The ERD contains one table: lottery_tickets. Since there is only a single table there are no relationships.

### CI Pipeline

![image](https://user-images.githubusercontent.com/82821693/121809838-5d546d80-cc56-11eb-91bc-180a9e8d2d50.png)

This is the Continuous Integration (CI) pipeline for this project. A flask framework was used working in conjuction with Google Cloud Platform (GCP) Virtual Machine (VM) instances. Continuous Integration enables the development process to be more frequent and more reliable.

This project uses a Jenkins CI server to handle the pipeline. It retrieves the code from the repository on GitHub and then performs these build instructions:

- Install Requirements
- Perform Testing
- Build the Application
- Push the Application to DockerHub
- Run the Ansible Playbook
- Deploy the Application

If there is a fault within the build process, the application will fail to run and the error reasoning can be easily obtained through the console output.

## Project Tracking

To track the progress of the project, Jira was used. 

https://andrewbarrett.atlassian.net/jira/software/projects/LOT/boards/2

![image](https://user-images.githubusercontent.com/82821693/121810142-8aede680-cc57-11eb-9ba6-e0536ab9e33f.png)

The Jira board uses a Kanban format that consists of 3 different columns:
- To Do
- In Progress
- Done

The cards within the board have epics assigned to them so that it is clear what the issue refers to. The epics that make up this board are:
- Documentation
  - This is referring to all the documents that was to be used in the creation of this README.
- User Stories
  - These are the implementations that correspond to a user's actions.
- Database
  - This refers to the table created in the database.
- Testing
  - Everything here refers to the testing process such as the unit testing and results.
- Integration
  - This refers to the deployment of the application.
- Architecture
  - This refers to the implementation of the 4 services used for the application.

## Risk Assessment

![image](https://user-images.githubusercontent.com/82821693/121812960-e9b85d80-cc61-11eb-9a54-c78e5f6308bc.png)

## Testing

To perform the testing for the project, pytest was used. How this works is essentially by creating a dummy test database, performing a function, and then deleting those changes. This process is repeated for as many tests written. Results are obtained through assertion such that the output value would be something known and can be checked with the test values. By explicitly asking, it is possible for the pytest command to yield a coverage report which shows the proportion of the code that has been tested.

### Service 1 Coverage Report

![image](https://user-images.githubusercontent.com/82821693/121814622-f640b400-cc69-11eb-9160-8eadfa1a10c2.png)

### Service 2 Coverage Report

![image](https://user-images.githubusercontent.com/82821693/121814636-08baed80-cc6a-11eb-954c-30344b1bb7a7.png)

### Service 3 Coverage Report

![image](https://user-images.githubusercontent.com/82821693/121814651-18d2cd00-cc6a-11eb-8329-ac05b094bc32.png)

### Service 4 Coverage Report

![image](https://user-images.githubusercontent.com/82821693/121814660-2425f880-cc6a-11eb-9039-ba5a8ffcbd76.png)

## Front-End Design

The front-end design uses a Jinja2 template as the user interface. The design used is simple and easily understandable.

The initial starting point of the application which consists of a title, generate button, and no database shown:

![image](https://user-images.githubusercontent.com/82821693/121814877-3ce2de00-cc6b-11eb-9a89-001c18296d08.png)

Clicking on the Generate button generates a lottery ticket, the winning numbers, prize, and the database:

![image](https://user-images.githubusercontent.com/82821693/121814879-453b1900-cc6b-11eb-804e-972d22f221c0.png)
