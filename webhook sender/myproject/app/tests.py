# from django.test import TestCase

# # Create your tests here.
#   // newdata.map((value, id)=>{            // b.append(e.text )
#         // is li ko per styling kerni hai mujhe so how
#         //   // console.log(value.text)  
#         //     document.write(`<h2 style="color: #000; 
#         //     min-height: 80px auto;
#         //     font-size: 17px;
#         //     background-color: lightgrey;
#         //     border: 1px solid #ccc;
#         //     padding: 0.5em;
#         //     width: fit-content;
#         //     border-radius: 10px;
#         //     margin-left: 140px;
#         //     align-items: center;">${"id",value.id, value.text}<h2/>`)
#         // })

<!-- <!DOCTYPE html>
<html>

<head>
    <title>Message Receiver</title>
  
</head>

<body>
    <style>
        .notification {
          font-size: 16px;
          color: #333;
          margin-bottom: 10px;
          list-style: none;
          min-height: 80px auto;
         font-size: 17px;
         background-color: lightgrey;
         border: 1px solid #ccc;
         padding: 0.5em;
         width: fit-content;
        border-radius: 10px;
        margin-left: 140px;
        align-items: center;
        }
        .notification-item {
          color: #333;
          margin-bottom: 10px;
          list-style: none;
          min-height: 80px auto;
         font-size: 17px;
         background-color: lightgrey;
         border: 1px solid #ccc;
         padding: 0.5em;
         width: fit-content;
        border-radius: 10px;
        margin-left: 440px;
        align-items: center;
    }

      </style>
      
    <div id="message-box" class="message-box">
        <div class="message">
            <p>This is a message box.</p>
        </div>
        <div id="adil"></div>
    </div>
    <script>

     
var apiUrl = 'http://127.0.0.1:8005/receiving_chats/';

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    console.log(data.messages);
    var newdata = data.messages;
    console.log(newdata, "newdata")
    var adil = document.getElementById("adil");
    
    const datas = newdata.map(e => {
      let li = document.createElement('li');
      li.textContent = e.text;
      li.classList.add('notification');
      adil.append(li);
      return li;
    });

    console.log("dataa", datas);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
        
// ----------------------------------------------------------------------------------------------------------------------------------------------------------------------


var apiUrl = 'http://127.0.0.1:8005/receive_notificationother/';

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    console.log(data.messages);
    var newdata = data.messages;
    console.log(newdata, "newdata")
    var adil = document.getElementById("adil");
    
    const datas = newdata.map(e => {
      let li = document.createElement('li');<!-- <!DOCTYPE html>
<html>

<head>
    <title>Message Receiver</title>
  
</head>

<body>
    <style>
        .notification {
          font-size: 16px;
          color: #333;
          margin-bottom: 10px;
          list-style: none;
          min-height: 80px auto;
         font-size: 17px;
         background-color: lightgrey;
         border: 1px solid #ccc;
         padding: 0.5em;
         width: fit-content;
        border-radius: 10px;
        margin-left: 140px;
        align-items: center;
        }
        .notification-item {
          color: #333;
          margin-bottom: 10px;
          list-style: none;
          min-height: 80px auto;
         font-size: 17px;
         background-color: lightgrey;
         border: 1px solid #ccc;
         padding: 0.5em;
         width: fit-content;
        border-radius: 10px;
        margin-left: 440px;
        align-items: center;
    }

      </style>
      
    <div id="message-box" class="message-box">
        <div class="message">
            <p>This is a message box.</p>
        </div>
        <div id="adil"></div>
    </div>
    <script>

     
var apiUrl = 'http://127.0.0.1:8005/receiving_chats/';

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    console.log(data.messages);
    var newdata = data.messages;
    console.log(newdata, "newdata")
    var adil = document.getElementById("adil");
    
    const datas = newdata.map(e => {
      let li = document.createElement('li');
      li.textContent = e.text;
      li.classList.add('notification');
      adil.append(li);
      return li;
    });

    console.log("dataa", datas);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
        
var apiUrl = 'http://127.0.0.1:8005/receive_notificationother/';

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    console.log(data.messages);
    var newdata = data.messages;
    console.log(newdata, "newdata")
    var adil = document.getElementById("adil");
    
    const datas = newdata.map(e => {
      let li = document.createElement('li');
      li.textContent = e.text;
      li.classList.add('notification-item');
      adil.append(li);
      return li;
    });
    
    console.log("dataa", datas);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
  
    </script>
  

</body>
</html>

bhai mai yeh chata hu k agar (receive_notificationother) ki taraf se koi message ayai tu wo  (receiving_chats) se seperate nahi hu
same agar (receiving_chats) ki taraf se koi message ayai tu wo  (receive_notificationother) se seperate nahi hu
so please code example

i have already said  is form mai aise
hello (receive_notificationother)
                                                                hello (receiving_chats)
  hello (receive_notificationother)
                                                                hello (receiving_chats) 

 message display kerna hai

abhi mera is form mai message display horaha hai 
hello (receive_notificationother)
  hello (receive_notificationother)
  hello (receive_notificationother)
                                                                hello (receiving_chats)
                                                                hello (receiving_chats)
                                                                hello (receiving_chats)


to mujhe is form mai message display kerna hai please solve this issue 
 hello (receive_notificationother)agar mai message (receive_notificationother) is fuction se aise dislay hu
                                                              hello (receiving_chats) agar mai message (receiving_chats) is fuction se karu tu aise dislay hu

  hello (receive_notificationother)agar mai message (receive_notificationother) is fuction se aise dislay hu
                                                                hello (receiving_chats) agar mai message (receiving_chats) is fuction se karu tu aise dislay hu
aise calte rahe 

 


 <!DOCTYPE html>
<html>

<head>
    <title>Message Receiver</title>
  
</head>

<body>
    <style>
        .notification {
          font-size: 16px;
          color: #333;
          margin-bottom: 10px;
          list-style: none;
          min-height: 80px auto;
         font-size: 17px;
         background-color: lightgrey;
         border: 1px solid #ccc;
         padding: 0.5em;
         width: fit-content;
        border-radius: 10px;
        margin-left: 140px;
        align-items: center;
        }
        .notification-item {
          color: #333;
          margin-bottom: 10px;
          list-style: none;
          min-height: 80px auto;
         font-size: 17px;
         background-color: lightgrey;
         border: 1px solid #ccc;
         padding: 0.5em;
         width: fit-content;
        border-radius: 10px;
        margin-left: 440px;
        align-items: center;
    }

      </style>
      
    <div id="message-box" class="message-box">
        <div class="message">
            <p>This is a message box.</p>
        </div>
        <div id="adil"></div>
    </div>
    
    <script>

      
      var apiUrl = 'http://127.0.0.1:8005/receive_notificationother/';

      fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
          console.log(data.messages);
          var newdata = data.messages;
          console.log(newdata, "newdata")
          var adil = document.getElementById("adil")
          
          const datas = newdata.map(e => {
            let li1 = document.createElement('li')
            li1.textContent = e.text;
            li1.classList.add("rec")
            li1.classList.add('notification-item');
            adil.append(li1);
            
            let li2 = document.createElement('li')
            li2.textContent = "";
            li2.classList.add("sent")
            li2.classList.add('notification');
            adil.append(li2);  chatgpt mujhe is api  (http://127.0.0.1:8005/receiving_chats/)ko is li2 ki jagah api ka data append kerwana hai so please code example
            return [li1, li2];
          });
          
          console.log("dataa", datas);
        })
        .catch(error => {
          console.log("error", error);
          console.error('Error fetching data:', error);
        });
  
    </script>
                          
</body>
</html>

ab samjo meri baat sahi se mai yeh chata hu receiving_chats se koi message HELLO HOW THIS IS A TESTING (receiving_chats) aur 
phir koi message HELLO(receiving_chats) se karo aur phir koi message  HELLO HOW THIS IS A TESTING (receiving_chats) karo 
tu mesaage is format mai display hona chahiyai  
HELLO HOW THIS IS A TESTING (receiving_chats)
                                                              HELLO (receive_notificationother)
HELLO HOW THIS IS A TESTING (receiving_chats)

but message is format mai display hu rahe hai 

HELLO HOW THIS IS A TESTING (receiving_chats)
HELLO HOW THIS IS A TESTING (receiving_chats)
                                                                                            HELLO(receive_notificationother)
yai messages sahi order mai display nahi horrahe hai (receiving_chats) ke all message eik jagah display horahe hai aur 
(receive_notificationother) wale messages sare messages eik jagah display horahai hai
please solve this issue with code example











<!DOCTYPE html>
<html>

<head>
  <title>Message Receiver</title>

  <style>
    .notification {
      font-size: 16px;
      color: #333;
      margin-bottom: 10px;
      list-style: none;
      min-height: 80px auto;
      font-size: 17px;
      background-color: lightgrey;
      border: 1px solid #ccc;
      padding: 0.7em;
      width: fit-content;
      border-radius: 10px;
    }

    .notification-item {
      color: #333;
      margin-bottom: 10px;
      list-style: none;
      min-height: 80px auto;
      font-size: 17px;
      border: 1px solid #ccc;
      padding: 0.7em;
      width: fit-content;
      border-radius: 10px;
    }
    
    /* .notification-text {
      margin-bottom: 0.5em;
    } */

    .sent {
      float: right;
      background-color: darkturquoise;
      color: #fff;
      margin-left: 60%;
      margin-right: 22%; /* Reduced from 22% */
      border-radius: 10px;
      overflow-y: auto;
      display: flex;
    }

    .received {
      float: left;
      background-color: gray;
      color: white;
      margin-right: 60%;
      margin-left: 22%; /* Reduced from 22% */
      /* border-radius: 10px; */
      display: flex;
    }
  </style>

</head>

<body>

  <div id="message-box" class="message-box">
    <ul id="message-list"></ul>
  </div>

  <script>
    var apiUrl = 'http://127.0.0.1:8005/receiving_chats/';

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        console.log(data.messages);
        var newdata = data.messages;
        console.log(newdata, "newdata")
        var messageList = document.getElementById("message-list");
        const datas = newdata.map(e => {
  let li = document.createElement('li');
  li.classList.add("notification");

  // Check if the message ID is even or odd
  if (e.id % 2 == 0) {
    li.classList.add("sent");
  } else {
    li.classList.add("received");
  }
  
  let message = document.createElement('p');
  message.textContent = e.text;
  message.classList.add("notification-item");
  message.classList.add("notification-text");

  let datetime = document.createElement('div');
let date = new Date(e.created_at);
let datetimeString = date.getDate() + "/" + date.toLocaleString('default', { month: 'long' }).toUpperCase() + "/" + date.getFullYear() + " " + ("0" + date.getHours()).slice(-2) + ":" + ("0" + date.getMinutes()).slice(-2) + ":" + ("0" + date.getSeconds()).slice(-2);
datetime.textContent = datetimeString;
datetime.classList.add("notification-item");
datetime.classList.add("notification-datetime");

  li.appendChild(message);
  messageList.appendChild(li);
  messageList.appendChild(datetime);

  return li;
});

        console.log("dataa", datas);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  </script>

</body>

</html>

















<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css" integrity="sha512-SzlrxWUlpfuzQ+pcUCosxcglQRNAq/DZjVsC0lE40xsADsfeQoEypE+enwcOiGjk/bSuGGKHEyjSoQ1zVisanQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-1y4OQsMxFI4/p4w+d4+1LgQ2aqVULH9oJr7VdAXp+XPY7Yi+NYFh1tJZ8fLtgkg+fgKbJWeGxR5yPd5DT+71vA==" crossorigin="anonymous" referrerpolicy="no-referrer" />

   <title>Message Receiver</title>
  <style>
    .container {
      max-width: 35% !important;
      margin: auto;
       margin-top: 4%;
        font-family: sans-serif;
        letter-spacing: 0.5px;
    }
    img{
      max-width: 100%;
      border-radius: 50% !important;
      height: 45px;
    }
    .msg-header{
      border: 1px solid #ccc;  
      width: 640px;
      height: 90px;
      border-bottom: none;
      background-color: #007bff;
    }  
    .msg-header-img{
      border-radius: 50% !important;
      /* width: 40px; */
      margin-left: 5%;
      margin-top:12px ;
      float: left;
    }
    .active{
      width: 120px;
      float: left;
      margin-left: 75px;
    }
    .active h4{
      font-size: 20px;
      margin-left: 10px;
      color: #fff;
      margin-top: 3.5%;

    }
    .active h6{
      font-size: 12px;
      line-height: 3px;
      margin-left: 10px;
      color: #fff;  
    }
    .header-icons {
      width: 145px;
      float: right;
      margin-top: 12px;
      margin-right: 10px;
      display: flex;
      margin:  10px;
      color: #fff;
      cursor: pointer;
  }
  .header-icons svg {
      filter: invert(100);
      cursor: pointer;
      padding: 12px 6psx;
      justify-content: space-between;
  }
    .sent {
      float: right;
      background-color: #007bff; 
      color: #fff;
      border-radius: 12px;
      overflow-y: auto;
      display: inline-block;
      font-family: sans-serif; 
      font-weight: 600;
      letter-spacing: 0.5px;
      padding: 12px 12px 0px;
      margin: 0px 80px;
      margin-top: 20px;
      margin-left: 200px;
    }
    .received {
  float: left;
  background-color: #b3cf99;
  margin:  0px 60px ;
  margin-right: 200px;
  /* margin-top: 10px; */
  color: dimgrey;
  border-radius: 12px;
  /* display: inline-block; */
  font-family: sans-serif; 
  padding: 12px 12px 0px; 
  width: fit-content;
  font-size: 14px;
  margin-top: 50px;
  font-weight: 600;
}

    .datetime {
      font-size: 14px;
      color: #111;
    }

    .datetime-right {
      float: right;
      letter-spacing: 1px;
      height: 0px !important;
      font-weight: 500;
      padding: -100px!important;
      color: #CADEC8;
      /* margin-top: 35px; */
      margin: 0px 80px 10px;
      margin-top: 10px;
      margin-left: 200px;
      font-family: sans-serif;
      /* margin-right: -7px; */
      
    }
    .datetime-left {
      letter-spacing: 1px;
      float: left;
      height: 0px;
      font-weight: 500;
      margin-right: 62%;
      margin-left: 26%;
      padding: -100px!important;
      color: #CADEC8;
      margin-top: 10px;
      margin-left:  60.4px;
      font-family: sans-serif;
    }
    /* .chatpage{
      padding: 0 0 50px 0;
    } */
    .msg-box{
      border: 1px solid #ccc;
      /* overflow: hidden; */
      padding-bottom: 25px;
      height: 3050px;
    }
    .newclass{
      position: absolute;
      width: 30%;
      font-size: 22px;
      margin-top: 12px;
    }
    /* .adil{ */
      /* border: 1px solid #000; */
    /* } */
  </style>
</head>
<body>
    <div class="container">
          <div class="msg-header">
            <div class="msg-header-img">
              <img src="https://srcwap.com/wp-content/uploads/2022/08/no-avatar.webp">
                 <div id="adil">
          </div>
    </div> 
    <div class="newclass" >
    <div class="header-icons">
      <i class="fa-solid fa-phone"></i>
      <i class="fa-solid fa-video ml-5"></i>
      <i class="fa-solid fa-circle-info ml-5"></i>

      
    </div>

    <div class="active">
      <h4>Adil Khan</h4> 
          <h6>3 hours ago...</h6>
          
    </div>
  </div>
</div>
  <div class="chat-page">
    
        <div class="msg-box">
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2U2EyRXc_2ReIIX_D4JJrYADPWp_G5Mk3QA&usqp=CAU" height="200px">
        <div id="adil">
  </div>
    </div> 

  </div>
</div>

    <script>
      var apiUrl = 'http://127.0.0.1:8005/receiving_chats/';
      fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
          console.log(data.messages);
          var newdata = data.messages;
          console.log(newdata, "newdata")
          var adil = document.getElementById("adil");
          const datas = newdata.map(e => {
            let div = document.createElement('div');
    
            let messageBox = document.createElement('div');
            messageBox.classList.add("notification");
    
            // Check if the message ID is even or odd
            if (e.id % 2 == 0) {
              messageBox.classList.add("sent");
            } else {
              messageBox.classList.add("received");
            }
    
            let messageText = document.createElement('p');
            messageText.textContent = e.text;
            messageText.classList.add("notification-item");
            messageBox.append(messageText);
    
            div.append(messageBox);
    
            let datetimeBox = document.createElement('div');
            datetimeBox.classList.add("datetime-box");
    
            const datetimeString = e.created_at;
            const datetime = new Date(datetimeString);
            const options = {month: 'long',  day: 'numeric', hour: 'numeric', minute: 'numeric', hour12: true };
            const formattedDatetime = datetime.toLocaleDateString('en-US', options);
            console.log(formattedDatetime); // Output: "Thursday, March 17, 2023, 3:35 PM"

    
            let datetimeText = document.createElement('p');
            datetimeText.textContent = formattedDatetime;
            datetimeText.classList.add("notification-item", "datetime");
    
            // Check if the message is sent or received
            if (messageBox.classList.contains("sent")) {
              datetimeText.classList.add("datetime-right");
              datetimeBox.classList.add("datetime-box-right");
            } else {
              datetimeText.classList.add("datetime-left");
              datetimeBox.classList.add("datetime-box-left");
            }
    
            datetimeBox.append(datetimeText);
    
            div.append(datetimeBox);
    
            adil.append(div);

            return div;
          });
    
    
          console.log("dataa", datas);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    </script>
    

</body>

</html>

