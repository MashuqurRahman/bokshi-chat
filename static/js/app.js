let currentRecipient = '';
let chatInput = $('#chat-input');
let chatButton = $('#btn-send');
let userList = $('#user-list');
let messageList = $('#message-list');
// let contactProfile = $("#contact_profile")
let contactProfile = document.getElementById('contact_profile')
let userProfile = document.getElementById('profile')

// Fetch all users from database through api
function updateUserList() {
    $.getJSON('api/v1/user/', function (data) {
        // userList.children('.user').remove();[mashuq commented this]

        for (let i = 0; i < data.length; i++) {
            // const userItem = `<li class="contact">${data[i]['username']}</li>`;
            const userItem = `<li class="contact">
                <div class="wrap">
                <span class="contact-status online"></span>
                <img src="http://emilcarlsson.se/assets/louislitt.png" alt="" />
                <div class="meta">
                    <p class="name" id="name_id">${data[i]['username']}</p>
                </div>
                </div>
            </li>`
            $(userItem).appendTo('#user-list');
        }
        $('.contact').click(function (e) {
            let selected = $(e.target).text();
            setCurrentRecipient(selected);
        });
        // $('.user').click(function () {
        //     userList.children('.active').removeClass('active');//[the previous selected active username er front end er active class remove hobe]
        //     let selected = event.target;
        //     $(selected).addClass('active');
            // setCurrentRecipient(selected.text);
        // });
    });
}

// Receive one message and append it to message list
function drawMessage(message) {
    let position_status = "sent";
    const date = new Date(message.timestamp);
    if (message.user === currentUser) position_status = 'replies';

    const messageItem = `<li class="message ${position_status}">
      <img src="http://emilcarlsson.se/assets/mikeross.png" alt="" />
      <p>${message.body}</p>
      </li>`
    $(messageItem).appendTo('#message-list');
}

// Fetch last 20 conversatio from the database
function getConversation(recipient) {
    $.getJSON(`/api/v1/message/?target=${recipient}`, function (data) {
        messageList.children('.message').remove();
        for (let i = data['results'].length - 1; i >= 0; i--) {
            drawMessage(data['results'][i]);
        }
        // $(".messages").animate({ scrollTop: $(document).height() }, "fast");
        // messageList.animate({scrollTop: messageList.prop('scrollHeight')});
    });

}

// Retrive message by message id and add to messageList
// Access message id from websocket
function getMessageById(message) {
    id = JSON.parse(message).message
    $.getJSON(`/api/v1/message/${id}/`, function (data) {
        if (data.user === currentRecipient ||
            (data.recipient === currentRecipient && data.user == currentUser)) {
            drawMessage(data);
        }
        // messageList.animate({scrollTop: messageList.prop('scrollHeight')});
        // $(".messages").animate({ scrollTop: $(document).height() }, "fast");
    });
}

// Send message to messages api
function sendMessage(recipient, body) {
    $.post('/api/v1/message/', {
        recipient: recipient,
        body: body
    }).fail(function () {
        alert('Error! Check console!');
    });
}

// set clicked user as currentRecipient
// get all conversation of currentRecipient or currentUser
function setCurrentRecipient(username) {
    // console.log(contactProfile);
    username_tag = contactProfile.getElementsByTagName('p')[0]
    // console.log(b[0].innerText);
    username_tag.innerText = username
    currentRecipient = username;
    // console.log(username);
    getConversation(currentRecipient);
    enableInput();
}


// Enable input button
function enableInput() {
    chatInput.prop('disabled', false);
    chatButton.prop('disabled', false);
    chatInput.focus();
}

// Disable input button
function disableInput() {
    chatInput.prop('disabled', true);
    chatButton.prop('disabled', true);
}

$(document).ready(function () {
    updateUserList();
    disableInput();

    userProfile.getElementsByTagName('p')[0].innerText=currentUser
//    let socket = new WebSocket(`ws://127.0.0.1:8000/?session_key=${sessionKey}`);
    var socket = new WebSocket(
        'ws://' + window.location.host +
        '/ws?session_key=${sessionKey}')

    chatInput.keypress(function (e) {
        console.log(chatInput.val());
        if (e.keyCode == 13)
            chatButton.click();
    });

    chatButton.click(function () {
        if (chatInput.val().length > 0) {
            console.log((currentRecipient));
            sendMessage(currentRecipient, chatInput.val());
            chatInput.val('');
        }
    });

    // Receive message from websocket
    socket.onmessage = function (e) {
        getMessageById(e.data);
    };
});


// for testing
// const userItem = `<li class="contact">
//     <div class="wrap">
//     <span class="contact-status online"></span>
//     <img src="http://emilcarlsson.se/assets/louislitt.png" alt="" />
//     <div class="meta">
//         <p class="name" id="name_id">${data[i]['username']}</p>
//         <p class="preview">You just got LITT up, Mike.</p>
//     </div>
//     </div>
// </li>`
