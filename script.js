const API_GATEWAY = "API_GATEWAY_URL";
const API = `${API_GATEWAY}/remembrall`;

let messageInput;
let timeDelayInput;
let emailInput;
let phoneNumberInput;
let notificationOptionButtons;
let form;

document.addEventListener("DOMContentLoaded", () => {
  messageInput = document.querySelector("#message");
  timeDelayInput = document.querySelector("#time_delay");
  emailInput = document.querySelector("#email");
  phoneNumberInput = document.querySelector("#phone_number");
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
    notificationType,
    email: emailInput.value,
    phoneNumber: phoneNumberInput.value,
  });
  clearForm();
  console.log(body);
  console.log(API);
  fetch(API, {
    headers: {
      "Content-type": "application/json",
    },
    method: "POST",
    body,
    mode: "no-cors",
  })
    .then((resp) => console.log(resp))
    .catch((err) => console.log(err.toString()));
}

function clearForm() {
  messageInput.value = "Notification message";
  emailInput.value = "email@email.com";
  timeDelayInput.value = "15";
}
