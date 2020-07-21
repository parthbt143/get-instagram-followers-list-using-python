import time
from selenium import webdriver

myusername = "" # Enter Your User Name
mypassword = "" # Enter Your Password
driver = webdriver.Chrome(executable_path=r'C:/Driver/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://instagram.com')
time.sleep(5)
print("instagram opened")


username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input') 
username.send_keys(myusername)
print("Username typed")

password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input') 
password.send_keys(mypassword)
print("password typed")


button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
button.click()  
print("Login button clicked")
time.sleep(5)

button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
button.click() 
print("not now click ")
time.sleep(2)


button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
button.click()
print("not now clicked again") 


button = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')
button.click() 
print("image clicked") 
button = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]')
button.click() 
print("myprofile clicked") 
print("profile page opened")
time.sleep(10) 
post = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span')
number_of_post = post.get_attribute("innerHTML")
print("number_of_post :- " + number_of_post)


followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span')
number_of_followers = followers.get_attribute("innerHTML")
print("number_of_followers :- "+number_of_followers)


following = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span')
number_of_following = following.get_attribute("innerHTML")
print("number_of_following :- "+number_of_following)
 
time.sleep(2) 
button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
button.click()
time.sleep(2) 
scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
    time.sleep(2)
    ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        return arguments[0].scrollHeight;
        """, scroll_box)
time.sleep(2)
followers_list = []
for x in range(1, int(number_of_followers)+1): 
	username = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+str(x)+']/div/div[1]/div[2]/div[1]/a')
	print(username.get_attribute("innerHTML")) 
	followers_list.append(username.get_attribute("innerHTML"))
 
close_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button')
close_button.click()

button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
button.click()
time.sleep(2)

scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
    time.sleep(2)
    ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        return arguments[0].scrollHeight;
        """, scroll_box)
time.sleep(2)
following_list = []
for x in range(1, int(number_of_following)+1):  
	username = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+str(x)+']/div/div[1]/div[2]/div[1]/a')
	print(username.get_attribute("innerHTML")) 
	following_list.append(username.get_attribute("innerHTML"))

close_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button')
close_button.click()

#followers

followers = open("followers_"+myusername+".txt", "w")
followers.write("Followers List of :- "+myusername+"\n"+"Total Followers :- "+str(number_of_followers)+"\n")
idx = 1;
for i in followers_list:
	followers.write(str(idx)+") "+i+"\n")
	idx = idx + 1
followers.close()

#follwings 


followings = open("followings_"+myusername+".txt", "w")
followings.write("Following List of :- "+myusername+"\n"+"Total Followings :- "+str(number_of_following)+"\n")
idx = 1;
for i in following_list:
	followings.write(str(idx)+") "+i+"\n")
	idx = idx + 1
followings.close()

#follow each other 
def find_mutual(a, b): 
    a_set = set(a) 
    b_set = set(b) 
  
    common = list(a_set & b_set)
    return (common)
          
mutual_list = find_mutual(followers_list, following_list);  

follow_each_other = open("follow_each_other_"+myusername+".txt", "w")
follow_each_other.write("List of users whom you follow and also who follows you :- "+myusername+"\n"+"Total :- "+str(len(mutual_list))+"\n")
idx = 1;
for i in mutual_list:
	follow_each_other.write(str(idx)+") "+i+"\n")
	idx = idx + 1
follow_each_other.close()


#whom you don't  follow back

you_dont_follow = list((set(followers_list).difference(following_list))) 

dont_follow = open("you_dont_follow_"+myusername+".txt", "w")
dont_follow.write("List of your followers whom you don't follow back :- "+myusername+"\n"+"Total :- "+str(len(you_dont_follow))+"\n")
idx = 1;
for i in you_dont_follow:
	dont_follow.write(str(idx)+") "+i+"\n")
	idx = idx + 1
dont_follow.close()

#who don't follow you back

dont_follow_you = list((set(following_list).difference(followers_list))) 

you_follow = open("dont_follow_you_"+myusername+".txt", "w")
you_follow.write("List of users whom you follow but they don't follow you :- "+myusername+"\n"+"Total :- "+str(len(dont_follow_you))+"\n")
idx = 1;
for i in dont_follow_you:
	you_follow.write(str(idx)+") "+i+"\n")
	idx = idx + 1
you_follow.close()
