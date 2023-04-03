const API_GATEWAY = "API_ENDPOINT/remembrall";

let messageInput;
let timeDelayInput;
let notificationOptionButtons;

document.addEventListener("DOMContentLoaded", () => {
  messageInput = document.querySelector("#message");
  timeDelayInput = document.querySelector('input[name="time_delay"]');
  notificationOptionButtons = document.querySelectorAll(".form__button");

  timeDelayInput.addEventListener("change", validateDelayTime());
  notificationOptionButtons.forEach((button) =>
    button.addEventListener("click", function (e) {
      sendData(e, button.dataset.notificationType);
    })
  );
});

function validateDelayTime() {
  return function () {
    const value = parseInt(this.value);
    if (value < 1) {
      this.value = 1;
    } else if (value > 50) {
      this.value = 60;
    }
  };
}

function sendData(e, notificationType) {
  e.preventDefault();
  const body = JSON.stringify({
    message: messageInput.value,
    timeDelay: timeDelayInput.value,
    option: notificationType,
  });
  console.log(body);
  console.log(API_GATEWAY);
  fetch(API_GATEWAY, {
    headers: {
      "Content-type": "application/json",
    },
    method: "POST",
    body,
    mode: "cors",
  })
    .then((resp) => resp.json())
    .then((data) => {
      alert(`Submitted. Result: ${JSON.stringify(data)}`);
    })
    .catch((err) => {
      alert(`Error: ${err.toString()}`);
    });
  clearForm();
}

function clearForm() {
  messageInput.value = "";
  timeDelayInput.value = "0";
  notificationOptionButtons.forEach((button) => (button.value = "0"));
}
