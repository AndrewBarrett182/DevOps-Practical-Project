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

The database structure for the project is displayed using an Entity Relationship Diagram (ERD). This diagram displays the design of the table associated with the database. Since there is only a single table there are no relationships.

![image](https://user-images.githubusercontent.com/82821693/121809180-b1aa1e00-cc53-11eb-9255-02c4861b2cea.png)


