document.addEventListener("DOMContentLoaded", () => {
  document
    .querySelector('input[name="time_delay"]')
    .addEventListener("change", function () {
      const value = parseInt(this.value);
      if (value < 1) {
        this.value = 1;
      } else if (value > 50) {
        this.value = 60;
      }
    });
});
