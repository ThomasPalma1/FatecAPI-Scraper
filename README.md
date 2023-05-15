<h1 align="center"><b>FatecAPI-Scraper: A scraper tool for Money Mind Project</h1></b>
       <p align="center">
         <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css">
         <i class="devicon-bash-plain colored"></i>
         <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50" height="50"/>
         <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="50" height="50"/>	
         <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="50" height="50"/>
</p>


## **Purpose of service**


<p align="justify">A scraper is a method that automates the extraction of data from websites or other online sources to acquire the desired information. Scrapers can be used for various purposes such as data analysis, research, monitoring, or content aggregation. In this project, the scraper is being utilized to extract the data that will be utilized in the machine learning process.</p>


## **Project dependencies**


<table>
    <tr>
        <th align="center">Dependency</th>
        <th align="center">Version</th>
        <th align="center">Description</th>
    </tr>
    <tr>
        <td align="center">python</td>
        <td align="center">>= 3.8</td>
        <td align="center">Programming language used in the development of the service.</td>
    </tr>
    <tr>
        <td align="center">python3-pip</td>
        <td align="center">>= 22.3</td>
        <td align="center">Python's default package manager.</td>
    </tr>
    <tr>
        <td align="center">virtualenv</td>
        <td align="justify">>= 20.13</td>
        <td align="center">A tool that makes it possible to create isolated virtual python environments.</td>
    </tr>
    <tr>
        <td align="center">requests</td>
        <td align="center">>= 2.28</td>
        <td align="center">Dependency that allows you to send HTTP/1.1 requests extremely easily.</td>
    </tr>
    <tr>
        <td align="center">mysql-connector-python</td>
        <td align="center">>= 8.0</td>
        <td align="center">Package that allows you to connect and interact with MySQL databases using Python</td>
    </tr>
    <tr>
        <td align="center">python-dotenv</td>
        <td align="center">>= 1.0</td>
        <td align="center">Library that makes it possible to load environment variables from an `.env` file into the project.</td>
    </tr>
</table>


## **Execution of the service**

<p align="justify">In this project there are two ways of execution, one of them is through Docker and the other is locally. Next you will see the step by step of how to run the project in the two ways mentioned.</p>

> **Note**
> The project is configured to work with environment variables. You need to add your database credentials into the `.env` file located in the `moneymind/src` directory;
> 
> It is important to create the `money_mind` database within MySQL. If you are interested in using another database, just change the name inside the file and environment variables;
> 
> In the environment variable where the host is being specified, it is important to leave the name of the container that is running the database, which in this case is `dbDocker`.

```sh
MYSQL_HOST=dbDocker
MARIADB_DATABASE=money_mind
MARIADB_USER=your_user
MARIADB_PASSWORD=your_password
MARIADB_PASSWORD_ROOT=your_password
```

### **Run the project via Docker**

> **It is important that you have Docker installed on your machine. I won't go into detail on how you can install Docker, but you can follow the steps in the [official Docker documentation](https://docs.docker.com/engine/install/).**

<p align="justify">After downloading the project manually or via Git commands, you should go to the <code>moneymind/</code> directory. You will notice that there is a file called <code>docker-compose.yml</code>, it is through this file that the project will be executed. Open a terminal of your choice, if possible one with <b>administrator/root privileges</b> and run the following command:</p>

```sh
docker compose up
```

<p align="justify">When the command mentioned above is executed, Docker starts creating and starting the containers defined in the <code>docker-compose.yml</code> file. It downloads the necessary images, creates the networks and volumes as specified, and starts the containers based on the provided settings.</p>

<p align="justify">In the case where the execution of the command is carried out successfully, you will notice that your terminal will show you that the values have started to be inserted.</p>


### **Run the project via Localhost**

> ****

<p align="justify"></p>

```sh

```

<p align="justify"></p>

<p align="justify"></p>


> **Note**
> This is a note

> **Warning**
> This is a warning