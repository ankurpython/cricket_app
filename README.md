# Cricket App
**This Project is developed for the testing purpose using DRF.**

**Create rest api for cricket app which perform following task:**
1. Signup and login must be there use jwt for login only those who is login can access these api.
2. User can enter first team data player name , player team , player turn(batting or bowling) , player rank ,player score , player sixer , player fours.Once all these data get entered make another api get call showing the result in json format. 
3. If again user enter data with new input it should perform athematic operation should be add or sub.
4. Create second team api player name , player team , player turn(batting or bowling) , player rank .player over, player wickets , player wicket name.Once all these data get entered make another api get call showing the result in json formate
5. Team which has bat should be won or lose after 5 overs and bowling team must be stopped after 5 overs, At the end winner team name should be comes at start.


## Steps to Run 
1. Download or Clone the Repository:    **https://github.com/ankurpython/cricket_app.git**
2. Make sure to install requirements.txt file:   **https://github.com/ankurpython/cricket_app/blob/master/DjangoRest/requirments.txt**
   > **pip install -r requirments.txt**
4. After all the installation complete use the django command to runserver:   **py manage.py runserver**
5. Open the browser: **http://localhost:8000**
6. For the signup use the: **py manage.py createsuperuser**
      > If you don't want to  create the credential, you can use following credential.
      >> 1. username == ankurkashyap635@gmail.com
      >> 2. password == 1234
7. Again open the browser provide the credentials: **http://localhost:8000/token**, 

**After that JWT token will be generate, you can test by using Postmen or Swagger.**

## Screenshots

### 1. **Base_Page**

![base-page](https://user-images.githubusercontent.com/48859058/124356798-af752700-dc35-11eb-8792-70c18e0e34d0.png)


### 2.a. **Signup or login page to generate the JWT Token access**

![signup](https://user-images.githubusercontent.com/48859058/124356840-e6e3d380-dc35-11eb-9895-047d27729ff9.png)

### 2.b. **Signup or login page to generate the JWT Token access**

![token-access_generated](https://user-images.githubusercontent.com/48859058/124356875-375b3100-dc36-11eb-9bf4-7144e985eb11.png)

### 3. **Base-API Page**

![base api page](https://user-images.githubusercontent.com/48859058/124357110-67ef9a80-dc37-11eb-9783-809ecfcca21a.png)

### 4.a. **Result Batting field in JSON format**

![batting json result](https://user-images.githubusercontent.com/48859058/124357118-763db680-dc37-11eb-8e37-865cd9f28bcf.png)

### 4.b. **Updation of Batting field**

![updated-batting-score](https://user-images.githubusercontent.com/48859058/124357246-1c89bc00-dc38-11eb-813e-cd7618a2c77f.png)

### 5.a. **Result Bowling field in JSON format**

![boweling json result](https://user-images.githubusercontent.com/48859058/124357290-64a8de80-dc38-11eb-8035-b77f3e1e1ddb.png)

### 5.b. **Updation of Bowling field**

![updated-bowling-over](https://user-images.githubusercontent.com/48859058/124357336-899d5180-dc38-11eb-88eb-0103f58f1a31.png)

### 6. **Match Score Result**

![match-score-result](https://user-images.githubusercontent.com/48859058/124357397-e436ad80-dc38-11eb-844f-127f144d0cdf.png)

## Thank You, If you have any query please feel free to reach.
