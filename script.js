const API_GATEWAY = "";
const API = `${API_GATEWAY}/remembrall`;

let messageInput;
let timeDelayInput;
let notificationOptionButtons;
let form;

document.addEventListener("DOMContentLoaded", () => {
  messageInput = document.querySelector("#message");
  timeDelayInput = document.querySelector('input[name="time_delay"]');
  notificationOptionButtons = document.querySelectorAll(".form__button");
  form = document.querySelector(".form");

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
  form.reportValidity();
  if (!form.checkValidity()) {
    return;
  }
  const body = JSON.stringify({
    message: messageInput.value,
    timeDelay: timeDelayInput.value,
    option: notificationType,
  });
  console.log(body);
  console.log(API);
  fetch(API, {
    headers: {
      "Content-type": "application/json",
    },
    method: "POST",
    body,
    mode: "no-cors",
  }).then((resp) => console.log(resp));
  // .then((data) =>
  //   alert(
  //     `The request was submitted with the result: ${JSON.stringify(data)}`
  //   )
  // )
  // .catch((err) => alert(`The request failed: ${err.toString()}`));
  clearForm();
}

function clearForm() {
  messageInput.value = "";
  timeDelayInput.value = "0";
  notificationOptionButtons.forEach((button) => (button.value = "0"));
}
