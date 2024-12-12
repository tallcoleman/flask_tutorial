window.addEventListener("load", () => {
  convertUTCToLocalDate();
});

function convertUTCToLocalDate() {
  const options = {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "numeric",
    minute: "numeric",
    hour12: true,
  };
  const dateSpans = document.querySelectorAll("span.date");
  for (const dateSpan of dateSpans) {
    const date = new Date(dateSpan.textContent + "Z");
    const dateString = date.toLocaleDateString(undefined, options);
    dateSpan.textContent = dateString;
  }
}
