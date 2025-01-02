import { DateTime } from "./vendored/luxon.min.js";

window.addEventListener("load", () => {
  convertUTCToLocalDate();
  convertUTCToRelativeDate();
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
  const dateSpans = document.querySelectorAll("span.date-local");
  for (const dateSpan of dateSpans) {
    const date = DateTime.fromJSDate(new Date(dateSpan.dataset.date + "Z"));
    const dateString = date.toLocaleString(options);
    dateSpan.textContent = dateString;
  }
}

function convertUTCToRelativeDate() {
  const dateSpans = document.querySelectorAll("span.date-relative");
  for (const dateSpan of dateSpans) {
    const date = DateTime.fromJSDate(new Date(dateSpan.dataset.date + "Z"));
    const dateString = date.toRelative();
    dateSpan.textContent = dateString;
  }
}
