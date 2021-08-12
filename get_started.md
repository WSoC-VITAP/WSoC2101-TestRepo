## Configuring workspace
- Pace up your terminals, and follow to get started.
- To participate and solve different tasks to let us know that you have skills enough to contribute in this project, you need to execute the following commands to set up the perfect local workspace.

## Step-1: Setting up Django
Before moving ahead, please make sure:

1.) You have python installed on your system, else install from [here](https://www.python.org/downloads/).

2.) pip package installed on your system, else refer [here](https://pip.pypa.io/en/stable/installation/).

We are all set to Install Django.

- To install Django use the following command.
```shell
    $>py -m pip install django 
```
Now, you should have the django components installed into your system and you should be good to move on to the next step.
This is an intro to those who use the default package manager, i.e. pip. If you use any other kind of package manager, look into their documentation in order to install Django.


## Step-2: Cloning the existing test project from GitHub

- Before you begin with the setup, it is to be noted that you need to install [git-cli](https://git-scm.com/downloads) tool.

### Cloning the project

```shell
    $> git clone https://github.com/WSoC-VITAP/WSoC2101-TestRepo.git
```
The above command will clone or download all the files from various snapshots into the current directory from where you
run this command (remember to setup your directory location first). This should be enough for cloning but if you want to know more about git cloning then
checkout [git cloning documentation](https://github.com/git-guides/git-clone).

### Creating a new branch

Git lets you create branches and work on different branches with different versions of the same project. We want you to
create a branch so that we can recognize your work and distinguish it from other submissions.

```shell
    Command:
      $> git checkout -b <yourname_reg>
    Example:
      $> git checkout -b ojasva_20bcn7062
```

The above command will create a new branch, and you will be automatically switched to that branch. So whatever changes
you make will be saved to the newly made branch on every commit.



## Step -3: You need to run the django server first to know the tasks. Refer the following section on how to run the server.
- First, set the directory to the folder that contains manage.py file.
- Now, run the following command: 
```shell
   $> py manage.py runserver
```
If an output like this is displayed : 

![Capture](https://user-images.githubusercontent.com/44553464/129101294-636683f6-c087-4122-b811-1d4de3100442.PNG)

`use (ctrl + c) to break first` use command : 
```shell
   $> py manage.py migrate
```
and with successful migration, again use the runserver command to finally get the desired output as:

![Capture2](https://user-images.githubusercontent.com/44553464/129101554-682cb10b-27bb-476d-b46b-f4f23d7724c2.PNG)

- Now, copy paste the server "http://XXXX" URL on your browser to see the webpages. 

The Home Page would look like :
![Capture3](https://user-images.githubusercontent.com/44553464/129102261-da47e8b7-5b98-40ed-a399-ba2a46ed3102.PNG)


Now, you can start working on the given tasks ,get started with solving this test tasks by completing the most of
them. 
`The more you score, greater the chance of you being selected to work on this project with us`
